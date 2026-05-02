import hashlib
import unittest
from e_voting.blockchain import Blockchain


class TestBlockchain(unittest.TestCase):
    def test_genesis_block_exists(self):
        chain = Blockchain()
        self.assertEqual(len(chain.chain), 1)
        self.assertEqual(chain.chain[0]['index'], 1)

    def test_new_vote_and_new_block(self):
        chain = Blockchain()
        vote = chain.new_vote('voter1', {'candidate_id': '1'})
        self.assertEqual(vote['vote'], {'candidate_id': '1'})
        expected_id = hashlib.sha256(str('voter1').encode()).hexdigest()
        self.assertEqual(vote['voter_id'], expected_id)

        block = chain.new_block(proof=123, previous_hash=chain.hash(chain.chain[-1]))
        self.assertEqual(block['index'], 2)
        self.assertEqual(block['votes'], [vote])
        self.assertEqual(chain.current_votes, [])

    def test_proof_of_work(self):
        chain = Blockchain()
        proof = chain.proof_of_work(chain.chain[-1]['proof'])
        self.assertTrue(chain.valid_proof(chain.chain[-1]['proof'], proof))


if __name__ == "__main__":
    unittest.main()
