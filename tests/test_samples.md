# Test Results

Python version Used: `Python 3.13.5` | Operating system: Windows |  Date: 11/05/26

| # | Input | Expected result | Actual result | PASS/FAIL (Status) |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | May show no listed warning signs; not a safety guarantee | `No listed warning signs found. This does NOT prove safety.` | PASS |
| 2 | `http://192.0.2.10/account` | IP-address hostname and HTTP | `Uses an IP address instead of a familiar domain.<br>Uses HTTP. HTTPS alone does not prove trust.` | PASS |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol and HTTP | `Contains an @ symbol<br>inspect carefully.<br>Uses HTTP. HTTPS alone does not prove trust.` | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | `Contains many hostname segments/subdomains.` | PASS |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | `Contains a punycode-style hostname.` | PASS |

## Additional improvement checks

| Check | Input | Expected result | Status |
|---|---|---|---|
| Long URL | `https://example.com/` followed by 110 `a` characters | Long URL warning | PASS |
| Empty input | spaces only | Friendly `No URL entered.` message; no crash | PASS |
| Malformed host | `http://[bad` | Readable invalid-format message; no crash | PASS |
