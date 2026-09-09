import io
import json
import sys
import unittest
from unittest.mock import patch

from wordfreq.__main__ import main


class WordfreqCliTest(unittest.TestCase):
    def test_json_output_preserves_sort_order(self):
        stdin = io.StringIO("banana apple banana cherry apple apple")
        stdout = io.StringIO()
        with patch.object(sys, "stdin", stdin), patch.object(sys, "stdout", stdout), patch.object(
            sys, "argv", ["wordfreq", "--json"]
        ):
            self.assertEqual(main(), 0)

        self.assertEqual(
            list(json.loads(stdout.getvalue()).items()),
            [("apple", 3), ("banana", 2), ("cherry", 1)],
        )


if __name__ == "__main__":
    unittest.main()
