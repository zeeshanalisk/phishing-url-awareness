import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from phishing_checker import inspect_url, has_warnings


class PhishingCheckerTests(unittest.TestCase):
    def test_normal_https_example_has_no_listed_warning(self):
        result = inspect_url("https://www.example.com/login")
        self.assertEqual(result, ["No listed warning signs found. This does NOT prove safety."])
        self.assertFalse(has_warnings(result))

    def test_ip_hostname_and_http_are_flagged(self):
        result = inspect_url("http://192.0.2.10/account")
        self.assertIn("Uses an IP address instead of a familiar domain.", result)
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", result)
        self.assertTrue(has_warnings(result))

    def test_at_symbol_and_http_are_flagged(self):
        result = inspect_url("http://example.com@sample.invalid/login")
        self.assertIn("Contains an @ symbol; inspect carefully.", result)
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", result)

    def test_many_hostname_segments_are_flagged(self):
        result = inspect_url("https://a.b.c.d.e.example.invalid/path")
        self.assertIn("Contains many hostname segments/subdomains.", result)

    def test_punycode_marker_is_flagged(self):
        result = inspect_url("https://xn--example.invalid/")
        self.assertIn("Contains a punycode-style hostname.", result)

    def test_long_url_is_flagged(self):
        long_url = "https://example.com/" + ("a" * 110)
        self.assertIn("Unusually long URL (over 100 characters).", inspect_url(long_url))

    def test_empty_input_is_handled(self):
        result = inspect_url("   ")
        self.assertEqual(result, ["No URL entered."])
        self.assertFalse(has_warnings(result))

    def test_malformed_bracketed_host_does_not_crash(self):
        result = inspect_url("http://[bad")
        self.assertEqual(result, ["This text is not a valid URL format."])
        self.assertFalse(has_warnings(result))


if __name__ == "__main__":
    unittest.main(verbosity=2)
