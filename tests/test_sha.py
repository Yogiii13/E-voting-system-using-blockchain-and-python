import hashlib
import unittest
from e_voting.sha import generate_hash


class TestSha256(unittest.TestCase):
    def test_generate_hash_str(self):
        self.assertEqual(generate_hash("abc").hex(), hashlib.sha256(b"abc").hexdigest())

    def test_generate_hash_bytes(self):
        self.assertEqual(generate_hash(b"hello world").hex(), hashlib.sha256(b"hello world").hexdigest())

    def test_generate_hash_empty(self):
        self.assertEqual(generate_hash("").hex(), hashlib.sha256(b"").hexdigest())

    def test_generate_hash_invalid_type(self):
        with self.assertRaises(TypeError):
            generate_hash(123)


if __name__ == "__main__":
    unittest.main()
