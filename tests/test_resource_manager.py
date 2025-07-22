import unittest
import os
from chatbot.resource_manager import ResourceManager

class TestResourceManager(unittest.TestCase):

    def setUp(self):
        # Use a temporary file for testing
        self.test_filepath = 'data/test_resources.json'
        # Ensure the data directory exists
        if not os.path.exists('data'):
            os.makedirs('data')
        # Clean up any old test files
        if os.path.exists(self.test_filepath):
            os.remove(self.test_filepath)
        self.rm = ResourceManager(filepath=self.test_filepath)

    def tearDown(self):
        # Clean up the created test file
        if os.path.exists(self.test_filepath):
            os.remove(self.test_filepath)

    def test_default_file_creation(self):
        self.assertTrue(os.path.exists(self.test_filepath))

    def test_get_crisis_info(self):
        info = self.rm.get_crisis_info()
        self.assertIn("disclaimer", info)
        self.assertIn("info", info)

    def test_get_resources_by_topic(self):
        stress_resources = self.rm.get_resources_by_topic("stress")
        self.assertIsInstance(stress_resources, list)
        self.assertEqual(len(stress_resources), 2)
        self.assertEqual(stress_resources[0]['title'], "Understanding Stress")

    def test_get_invalid_topic(self):
        invalid_resources = self.rm.get_resources_by_topic("unicorns")
        self.assertEqual(len(invalid_resources), 0)

if __name__ == '__main__':
    unittest.main()