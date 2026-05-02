import hashlib
import unittest
from e_voting import server as server_module


class TestServerModule(unittest.TestCase):
    def test_decrypt_candidate(self):
        encrypted = hashlib.sha256(b'Candidate 1').hexdigest()
        self.assertEqual(server_module.decrypt_candidate(encrypted), 'Candidate 1')
        self.assertEqual(server_module.decrypt_candidate('invalidhash'), 'Invalid candidate')

    def test_blockchain_validate_chain(self):
        chain = server_module.Blockchain()
        self.assertTrue(chain.validate_chain())
        chain.add_vote('abc')
        chain.create_block(previous_hash=chain.hash(chain.get_last_block()))
        self.assertTrue(chain.validate_chain())


if __name__ == '__main__':
    unittest.main()
