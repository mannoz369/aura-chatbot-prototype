import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure necessary NLTK data is available
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except nltk.downloader.DownloadError:
    print("Downloading VADER lexicon for sentiment analysis...")
    nltk.download('vader_lexicon')
    print("Download complete.")

class NlpService:
    """
    Handles NLP tasks like sentiment analysis and crisis detection.
    """
    def __init__(self):
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.crisis_keywords = [
            "kill myself", "suicide", "can't go on", "end my life",
            "overwhelmed", "hopeless", "want to die", "harm myself"
        ]

    def analyze_sentiment(self, text: str) -> dict:
        """
        Analyzes the sentiment of a given text.
        Returns a dictionary with sentiment scores.
        """
        return self.sentiment_analyzer.polarity_scores(text)

    def get_sentiment_label(self, text: str) -> str:
        """
        Returns a simple sentiment label (positive, negative, neutral).
        """
        scores = self.analyze_sentiment(text)
        if scores['compound'] >= 0.05:
            return 'positive'
        elif scores['compound'] <= -0.05:
            return 'negative'
        else:
            return 'neutral'

    def detect_crisis(self, text: str) -> bool:
        """
        Detects crisis keywords in the user's input.
        Returns True if a crisis keyword is found, False otherwise.
        """
        lower_text = text.lower()
        return any(keyword in lower_text for keyword in self.crisis_keywords)