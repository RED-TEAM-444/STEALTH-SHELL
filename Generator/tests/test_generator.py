import unittest
from src.generator import generate_reverse_shell

class TestGenerator(unittest.TestCase):
    def test_generate_reverse_shell(self):
        ip = "127.0.0.1"
        port = 4444
        shell_code = generate_reverse_shell(ip, port)
        self.assertIn(ip, shell_code)
        self.assertIn(str(port), shell_code)

if __name__ == "__main__":
    unittest.main()

