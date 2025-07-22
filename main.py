import os
import time
from chatbot.aura_bot import AuraBot

def main():
    """
    Main function to run the Aura chatbot CLI.
    Initializes the bot and handles the main interaction loop.
    """
    if not os.path.exists('data'):
        os.makedirs('data')

    bot = AuraBot()
    bot.start()

if __name__ == "__main__":
    main()