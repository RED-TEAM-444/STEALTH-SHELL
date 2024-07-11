import unittest
from src.obfuscator import obfuscate_script

class TestObfuscator(unittest.TestCase):
    def test_obfuscate_script(self):
        script = "Hello, World!"
        obfuscated_script = obfuscate_script(script)
        self.assertIn("powershell -EncodedCommand", obfuscated_script)

if __name__ == "__main__":
    unittest.main()

