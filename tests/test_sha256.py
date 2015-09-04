import hashlib
import sha256
import unittest


sha = sha256.sha256
hsha = hashlib.sha256

test_vectors = [
    (
        '',
        'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    ),
    (
        'abc',
        'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
    ),
    (
        'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq',
        '248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1'
    ),
    (
        'a' * 129,
        'c12cb024a2e5551cca0e08fce8f1c5e314555cc3fef6329ee994a3db752166ae',
    ),
    (
        'a' * 1000000,
        'cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0'
    ),
]


class TestSHA256(unittest.TestCase):
    def test_normal(self):
        for input, hash in test_vectors:
            self.assertEquals(sha(input).hexdigest(), hash)

    def test_hashlib(self):
        for input, hash in test_vectors:
            self.assertEquals(sha(input).hexdigest(), hsha(input).hexdigest())

    def test_getset(self):
        for input, hash in test_vectors:
            s = sha()
            for i, c in enumerate(input):
                s.update(c)
                if i % 64 == 63:
                    new = sha()
                    new.state = s.state
                    s = new
            self.assertEquals(s.hexdigest(), hash)


if __name__ == '__main__':
    unittest.main()
