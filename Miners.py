# import libraries
import hashlib


class Miner:

    def mine(message, difficulty=1):
        assert difficulty >= 1
        prefix = '1' * difficulty
        for i in range(1000):
            digest = hashlib.sha256(str(hash(message)) + str(i))
            if digest.startswith(prefix):
                print("after " + str(i) + " iterations found nonce: " + digest)
            return digest
