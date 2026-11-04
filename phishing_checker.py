"""EWB Phishing URL Awareness Checker.

This educational program inspects URL text only. It never opens a link,
contacts a website, scans for malware, or proves that a URL is safe.
"""

import re
from urllib.parse import urlparse

INFO_PREFIXES = (
    "No URL entered.",
    "Could not identify a hostname.",
    "This text is not a valid URL format.",
)


def inspect_url(raw_url):
    """Return messages for the six warning signs listed in the EWB workbook."""
    if not isinstance(raw_url, str):
        return ["No URL entered."]

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    # A missing scheme is treated as HTTP, matching the workbook's starter logic.
    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
    except ValueError:
        # For example, urlparse raises ValueError for a malformed bracketed host.
        return ["This text is not a valid URL format."]

    host = (parsed.hostname or "").lower()
    if not host:
        return ["Could not identify a hostname."]

    # 1. An @ symbol can make the real destination easy to overlook.
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    # 2. Long URLs can hide the destination in a large amount of text.
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # 3. An IPv4-shaped hostname is flagged for manual review.
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    # 4. Five or more hostname labels are flagged.
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    # 5. xn-- is the common Punycode marker.
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # 6. Plain HTTP does not encrypt the connection.
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")

    return findings


def has_warnings(findings):
    """Distinguish warning findings from input/format/no-warning messages."""
    return any(not item.startswith(INFO_PREFIXES + ("No listed warning signs found.",)) for item in findings)


def main():
    """Run an interactive loop; type q, quit, or exit to stop."""
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    while True:
        try:
            raw_url = input("\nEnter a sample URL (or type q to quit): ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! Stay alert online.")
            break

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for item in findings:
            print("- " + item)

        if has_warnings(findings):
            print(f"\nREVIEW CAREFULLY: {len(findings)} warning sign(s) found.")
        elif findings[0].startswith("No listed warning"):
            print("\nNo listed warning signs were detected; this is not a safety guarantee.")

        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
