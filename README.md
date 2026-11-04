# EWB Phishing URL Awareness Checker

## Overview

This is a beginner-friendly, command-line project for phishing awareness. It reads a URL as plain text and checks for a small set of visible warning signs. It does **NOT** open a link, contact a website, scan for malware or decide whether a website is trustworthy.

## Features

- Detects an `@` symbol in the URL text.
- Flags URLs longer than 100 characters.
- Flags IPv4-shaped hostnames.
- Flags hostnames with five or more dot-separated labels.
- Flags the `xn--` Punycode marker in a hostname.
- Flags the HTTP scheme.
- Handles empty input and malformed bracketed hostnames with a friendly message.
- Allows several checks in one run; type `q`, `quit`, or `exit` to stop.
- Shows a `REVIEW CAREFULLY` summary when warning signs are detected.

## Requirements

- Python 3.10 or later.
- No additional Python packages. Only Python's built-in `re` and `urllib.parse` modules are used.

## How to Run

Open a terminal in the project folder.

**Windows**

```bash
python phishing_checker.py
```

If `python` is not recognised, try `py phishing_checker.py`.

**macOS / Linux**

```bash
python3 phishing_checker.py
```

Enter one of the fictional sample URLs from the sample. Enter `q` to quit. The program checks the text only; it never visits the address.

## Example Output

```text
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Never enter passwords from unexpected links.
```

## Testing

The five required workbook examples and the extra checks are recorded in [`tests/test_samples.md`](tests/test_samples.md).

To run the automated tests from the project folder:

```bash
python -m unittest discover -s tests -v
```

On macOS / Linux, use `python3` instead of `python` if required. The automated test file checks the five workbook examples plus long input, empty input and malformed input.

## Screenshots

The workbook asks for two genuine screenshots: `screenshots/sample_run.png` and `screenshots/test_results.png`.

## Improvements

1. **Repeat checks with a quit command:** a `while` loop lets the user inspect several sample strings without restarting the program. `q`, `quit`, or `exit` ends the loop.
2. **Review summary:** the `has_warnings()` helper distinguishes actual warning findings from informational messages and prints a count for flagged inputs.
3. **Malformed-input handling:** URL parsing is protected with `try/except`, so a malformed bracketed hostname returns a readable message rather than terminating the program.

After making any changes, re-run all five samples and the automated tests.

## Limitations

These six checks are clues, not proof. A URL with no listed warning signs may still be dangerous, and a flagged URL may be legitimate. HTTPS encrypts a connection but does not prove that the site belongs to the organisation it claims to represent. This program does not check domain ownership, reputation, page content, certificates, redirects, malware or live website behaviour.

## Ethical Use

Use only fictional sample strings for this exercise. Do not enter real suspicious links, passwords OTPs or personal data. Do not send phishing messages, visit suspicious links, scan websites, or probe networks. Use any broader security testing only with written authorisation.

## Author

**Zeeshan Ali Sheikh** , Ewb AI POWERED CYBERSECURITY Batch 1 , EWB Courses
