import unittest
from chatbot.nlp_service import NlpService

class TestNlpService(unittest.TestCase):

    def setUp(self):
        self.nlp = NlpService()

    def test_positive_sentiment(self):
        text = "I feel amazing and wonderful today!"
        label = self.nlp.get_sentiment_label(text)
        self.assertEqual(label, 'positive')

    def test_negative_sentiment(self):
        text = "This is a horrible and dreadful experience."
        label = self.nlp.get_sentiment_label(text)
        self.assertEqual(label, 'negative')

    def test_neutral_sentiment(self):
        text = "The book is on the table."
        label = self.nlp.get_sentiment_label(text)
        self.assertEqual(label, 'neutral')

    def test_crisis_detection_positive(self):
        text = "I am so overwhelmed I can't go on anymore."
        self.assertTrue(self.nlp.detect_crisis(text))

    def test_crisis_detection_negative(self):
        text = "I'm going to the store."
        self.assertFalse(self.nlp.detect_crisis(text))

if __name__ == '__main__':
    unittest.main()