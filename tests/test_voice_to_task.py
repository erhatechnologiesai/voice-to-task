import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestVoiceToTask(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_memo_parsing(self):
        res = self.client.post("/parse-memo", json={"memo_id": "VM-001", "audio_transcript": "Hey remind me to review Q4 AWS billing by tomorrow 5pm."})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(len(data["extracted_tasks"]), 2)
        self.assertEqual(data["extracted_tasks"][0]["priority"], "HIGH")

if __name__ == "__main__":
    unittest.main()
