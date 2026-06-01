import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotions(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for text, expected_emotion in test_cases:
            with self.subTest(text=text):
                result = emotion_detector(text)
                dominant = result.get('dominant_emotion')
                self.assertEqual(dominant, expected_emotion, f"Failed for text: {text}")

if __name__ == '__main__':
    unittest.main()