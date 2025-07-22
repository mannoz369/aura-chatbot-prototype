import json
import os
import time
from datetime import datetime

from .nlp_service import NlpService
from .resource_manager import ResourceManager
from . import exercises

class AuraBot:
    """
    The main class for the Aura chatbot, handling user interaction,
    data management, and orchestrating services.
    """
    def __init__(self, profile_path='data/user_profile.json', logs_path='data/mood_logs.json'):
        self.profile_path = profile_path
        self.logs_path = logs_path
        self.user_profile = self._load_json(self.profile_path)
        self.mood_logs = self._load_json(self.logs_path, default=[])
        self.nlp = NlpService()
        self.resources = ResourceManager()

    def _load_json(self, filepath: str, default=None):
        """Safely loads a JSON file."""
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
        return default if default is not None else {}

    def _save_json(self, data, filepath: str):
        """Saves data to a JSON file."""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def start(self):
        """Starts the main interaction loop of the chatbot."""
        if not self.user_profile.get("name"):
            self._onboarding()

        print(f"\nWelcome back, {self.user_profile['name']}! I'm here for you.")
        self._show_menu()

    def _onboarding(self):
        """Handles the first-time user setup."""
        print("Hello! I'm Aura, your personal mental well-being companion.")
        name = input("To get started, what should I call you? ")
        self.user_profile['name'] = name
        self._save_json(self.user_profile, self.profile_path)
        print(f"It's nice to meet you, {name}.")

    def _show_menu(self):
        """Displays the main menu and handles user choices."""
        while True:
            print("\nHow can I help you today?")
            print("  1. Check-in with my mood")
            print("  2. Get helpful resources")
            print("  3. View my progress")
            print("  4. Exit")
            choice = input("Enter the number of your choice: ")

            if choice == '1':
                self.mood_checkin()
            elif choice == '2':
                self.get_resources()
            elif choice == '3':
                self.show_progress()
            elif choice == '4':
                print(f"Take care, {self.user_profile['name']}. I'm here whenever you need me.")
                break
            else:
                print("That's not a valid option. Please choose a number from 1 to 4.")

    def mood_checkin(self):
        """Handles the mood check-in and journaling process."""
        print("\nLet's check in. How are you feeling today?")
        journal_entry = input("Feel free to write as much as you like: ")

        if self.nlp.detect_crisis(journal_entry):
            self._handle_crisis()
            return

        sentiment_label = self.nlp.get_sentiment_label(journal_entry)
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "entry": journal_entry,
            "sentiment": sentiment_label
        }
        self.mood_logs.append(log_entry)
        self._save_json(self.mood_logs, self.logs_path)

        print("\nThank you for sharing.")
        if sentiment_label == 'negative':
            print("It sounds like you're having a tough time.")
            if input("Would you like to try a quick relaxation exercise? (yes/no): ").lower() == 'yes':
                exercises.guided_breathing_exercise()
        elif sentiment_label == 'positive':
            print("I'm really glad to hear you're feeling positive today!")
        else:
            print("It's good to take a moment to reflect.")
        time.sleep(1)

    def get_resources(self):
        """Provides resources on various topics."""
        print("\nI have resources on the following topics:")
        topics = self.resources.get_available_topics()
        for topic in topics:
            print(f"- {topic.capitalize()}")

        choice = input("Which topic are you interested in? ").lower()
        if choice in topics:
            articles = self.resources.get_resources_by_topic(choice)
            print(f"\nHere are some resources on {choice}:")
            for article in articles:
                print(f"  - Title: {article['title']}\n    Summary: {article['summary']}")
        else:
            print("I'm sorry, I don't have resources on that topic right now.")

    def show_progress(self):
        """Shows a conversational summary of the user's mood trends."""
        if not self.mood_logs:
            print("\nI don't have any mood logs for you yet. Try using the 'Check-in' feature first!")
            return

        print("\nLet's look at your recent progress...")
        time.sleep(1)
        # Show the last 5 entries
        recent_logs = self.mood_logs[-5:]
        pos_count = sum(1 for log in recent_logs if log['sentiment'] == 'positive')
        neg_count = sum(1 for log in recent_logs if log['sentiment'] == 'negative')

        print(f"In your last {len(recent_logs)} entries, you've shared:")
        print(f"  - {pos_count} positive moment(s)")
        print(f"  - {neg_count} negative moment(s)")

        if pos_count > neg_count:
            print("It's great to see more positive moments recently. Keep it up!")
        else:
            print("Remember that every day is different, and it's okay to have tough moments.")
        time.sleep(2)

    def _handle_crisis(self):
        """Provides a crisis message and resources."""
        crisis_info = self.resources.get_crisis_info()
        print("\n" + "="*50)
        print("IMPORTANT:")
        print("It sounds like you are in significant distress.")
        print(crisis_info.get("disclaimer", ""))
        print(crisis_info.get("info", "Please reach out to a professional for help immediately."))
        print("="*50)
        time.sleep(3)