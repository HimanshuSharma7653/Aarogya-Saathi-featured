import unittest
from services.exercise_service import get_yoga_poses, get_exercise_plan
from services.exercise_api import search_wger_exercises

class ExerciseFeatureTests(unittest.TestCase):
    def test_yoga_library_contains_requested_poses(self):
        names = {p['name'] for p in get_yoga_poses()}
        for name in ['Warrior I', 'Warrior II', 'Bridge Pose', 'Cat-Cow Stretch']:
            self.assertIn(name, names)

    def test_every_pose_has_instructions_and_art(self):
        for pose in get_yoga_poses():
            self.assertTrue(pose['steps'], pose['name'])
            self.assertTrue(pose['svg'].startswith('<svg'), pose['name'])
            self.assertTrue(pose['caution'], pose['name'])

    def test_local_exercises_exist_without_api(self):
        self.assertGreaterEqual(len(get_exercise_plan()), 3)

    def test_wger_client_handles_offline_or_returns_list(self):
        result = search_wger_exercises('squat', limit=3)
        self.assertIsInstance(result, list)
        self.assertLessEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()
