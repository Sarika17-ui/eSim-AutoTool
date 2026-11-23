
import unittest

from modules.version_checker import (
    extract_version,
    compare_versions,
    check_version
)


class TestVersionChecker(unittest.TestCase):

    def test_extract_version(self):
        self.assertEqual(
            extract_version("Python 3.12.6"),
            "3.12.6"
        )

    def test_extract_missing_version(self):
        self.assertIsNone(extract_version(None))

    def test_compatible_version(self):
        self.assertTrue(compare_versions("10.0.8", "8.0"))

    def test_incompatible_version(self):
        self.assertFalse(compare_versions("7.0", "8.0"))

    def test_missing_tool(self):
        tool = {
            "name": "KiCad",
            "installed": False,
            "version": None
        }

        result = check_version(tool)

        self.assertEqual(result["status"], "NOT INSTALLED")

    def test_installed_compatible_tool(self):
        tool = {
            "name": "Python",
            "installed": True,
            "version": "Python 3.12.6"
        }

        result = check_version(tool)

        self.assertEqual(result["status"], "COMPATIBLE")


if __name__ == "__main__":
    unittest.main()
