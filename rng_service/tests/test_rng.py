import unittest
import socket
import rng_service


class rngTests(unittest.TestCase):

    def setUp(self):
        rng_service.app.testing = True
        self.app = rng_service.app.test_client()

    def testHostName(self): 
        hostname = socket.gethostname()
        response = self.app.get('/')
        self.assertEqual(response.data, "rng_service running on {}\n".format(hostname))

    def testRandomBytes(self):
        num_bytes = 32
        response = self.app.get('/' + str(num_bytes))
        self.assertEqual(len(response.data), num_bytes)

    def testMimeType(self):
        num_bytes = 32
        response = self.app.get('/' + str(num_bytes))
        self.assertEqual(response.mimetype, 'application/octet-stream')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
