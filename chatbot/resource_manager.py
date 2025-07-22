import json
import os

class ResourceManager:
    """
    Manages loading and providing curated content from a JSON file.
    """
    def __init__(self, filepath='data/resources.json'):
        self.filepath = filepath
        self._load_resources()

    def _load_resources(self):
        """Loads resources from the JSON file into memory."""
        if not os.path.exists(self.filepath):
            self.resources = self._create_default_resources()
        else:
            with open(self.filepath, 'r') as f:
                self.resources = json.load(f)

    def _create_default_resources(self) -> dict:
        """Creates a default resources file if one doesn't exist."""
        default_data = {
            "topics": {
                "stress": [
                    {"title": "Understanding Stress", "summary": "A brief overview of what stress is and how it affects the body."},
                    {"title": "5-Minute Stress Relief", "summary": "Quick techniques to calm down when you feel stressed."}
                ],
                "anxiety": [
                    {"title": "Managing Anxiety", "summary": "Practical tips for managing anxious thoughts."},
                    {"title": "Grounding Techniques", "summary": "Learn about the 5-4-3-2-1 grounding method to manage anxiety."}
                ]
            },
            "crisis_helpline": {
                "name": "Emergency Support",
                "info": "For immediate support, please contact a crisis helpline. In India, you can reach Vandrevala Foundation at 9999666555.",
                "disclaimer": "Aura is a supportive tool, not a replacement for crisis intervention."
            }
        }
        with open(self.filepath, 'w') as f:
            json.dump(default_data, f, indent=4)
        return default_data

    def get_resources_by_topic(self, topic: str) -> list:
        """Returns a list of resources for a given topic."""
        return self.resources.get("topics", {}).get(topic.lower(), [])

    def get_crisis_info(self) -> dict:
        """Returns crisis helpline information."""
        return self.resources.get("crisis_helpline", {})

    def get_available_topics(self) -> list:
        """Returns a list of available resource topics."""
        return list(self.resources.get("topics", {}).keys())