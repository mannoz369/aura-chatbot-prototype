
# Aura Chatbot - Prototype

This repository contains a working command-line prototype of "Aura - Your Personalized Mental Well-being Chatbot," as specified in the "Maple - ComSoc.pdf" hackathon proposal.

The prototype is built in Python and simulates the core features using a simple command-line interface (CLI). Only for the prototype purpose

## How Features Are Implemented

This prototype maps the requirements from the document to a tangible implementation:

| Feature from Document [cite] | Prototype Implementation |
| --- | --- |
| **Conversational Interface** [23, 74] | A Command-Line Interface (CLI) in `main.py` simulates the chat flow. |
| **Mood & Journaling Dialogue** [36, 44] | The `mood_checkin` function in `aura_bot.py` accepts free-form text from the user. |
| **AI Sentiment Analysis** [45, 91] | The `nlp_service.py` module uses NLTK's VADER model to perform sentiment analysis on user input. |
| **Personalized Exercises** [37, 47] | The `exercises.py` module contains a guided breathing exercise. The bot recommends it conversationally after a negative mood entry. |
| **Curated Resources** [38, 49] | `resource_manager.py` loads articles from `data/resources.json` and provides them based on user queries. |
| **Progress Insights** [39, 61] | The `show_progress` function reads from `data/mood_logs.json` to generate a conversational summary of recent moods. |
| **Crisis Detection** [60, 146] | `nlp_service.py` scans user input for crisis-related keywords and triggers a special message with a helpline. |
| **Python Backend** [77] | The entire application logic is written in Python, structured into modules within the `chatbot/` directory. |
| **Database Simulation** [81, 84] | User data and logs are stored in `data/mood_logs.json` (simulating MongoDB), and curated content is in `data/resources.json` (simulating PostgreSQL). |

## Setup and Installation

1.  **Clone the repository or create the files** as listed in the project structure.
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Download NLTK Data:**
    Run Python in your terminal and execute the following commands to download the necessary NLTK models:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('vader_lexicon')
    ```

## How to Run the Prototype

1.  Navigate to the root directory of the project (`aura-chatbot-prototype/`).
2.  Run the main application:
    ```bash
    python main.py
    ```
3.  Follow the on-screen prompts to interact with Aura. The first time you run it, it will ask for your name. Subsequent runs will remember you.


