import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="Testing", pattern="Test*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)