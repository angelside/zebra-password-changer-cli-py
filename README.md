# Zebra Password Changer CLI

[![maintenance-status](https://img.shields.io/badge/maintenance-as--is-yellow.svg?style=for-the-badge)](https://gist.github.com/angelside/364976fbcf7001a5da7e79ad8ed91fec)
[![maintenance-status](https://img.shields.io/static/v1?label=maintenance&message=internal-tool&style=for-the-badge&color=blue)](https://gist.github.com/angelside/364976fbcf7001a5da7e79ad8ed91fec) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciICB2aWV3Qm94PSIwIDAgNDggNDgiIHdpZHRoPSI0OHB4IiBoZWlnaHQ9IjQ4cHgiPjxwYXRoIGZpbGw9IiM0Y2FmNTAiIGQ9Ik0yNCw1QzEzLjUsNSw1LDEzLjYsNSwyNC4xYzAsOC4yLDUuMSwxNS4xLDEyLjMsMTcuOWw0LjItMTEuNUMxOC44LDI5LjUsMTcsMjcsMTcsMjQgYzAtMy45LDMuMS03LDctN3M3LDMuMSw3LDdjMCwzLTEuOCw1LjUtNC41LDYuNUwzMC43LDQyQzM3LjksMzkuMiw0MywzMi4zLDQzLDI0LjFDNDMsMTMuNiwzNC41LDUsMjQsNXoiLz48cGF0aCBmaWxsPSIjMmU3ZDMyIiBkPSJNMTcuOSw0My4zbC0wLjktMC40QzkuMiw0MCw0LDMyLjQsNCwyNC4xQzQsMTMsMTMsNCwyNCw0YzExLDAsMjAsOSwyMCwyMC4xIGMwLDguMy01LjIsMTUuOS0xMi45LDE4LjhsLTAuOSwwLjRsLTQuOC0xMy4zbDAuOS0wLjRjMi4zLTAuOSwzLjgtMy4xLDMuOC01LjZjMC0zLjMtMi43LTYtNi02cy02LDIuNy02LDZjMCwyLjUsMS41LDQuNywzLjgsNS42IGwwLjksMC40TDE3LjksNDMuM3ogTTI0LDZDMTQuMSw2LDYsMTQuMSw2LDI0LjFjMCw3LjEsNC4zLDEzLjcsMTAuNywxNi41bDMuNS05LjZDMTcuNiwyOS43LDE2LDI3LDE2LDI0YzAtNC40LDMuNi04LDgtOCBzOCwzLjYsOCw4YzAsMy0xLjYsNS43LTQuMiw3bDMuNSw5LjZDMzcuNywzNy44LDQyLDMxLjMsNDIsMjQuMUM0MiwxNC4xLDMzLjksNiwyNCw2eiIvPjwvc3ZnPg==)](./LICENSE)
[![GitHub-Sponsors](https://img.shields.io/badge/Sponsor-EA4AAA.svg?style=for-the-badge&logo=GitHub-Sponsors&logoColor=white)](https://github.com/sponsors/angelside)

> Zebra Password Changer CLI is a _"blazingly fast 🤣"_ Python CLI tool that allows changing Zebra printer's web interface password with socket protocol.

## 📦 Installation

No installation, no dependencies, it's pure Python.

## 🔨 Usage

CLI app has two parameters: the printer's IP address and the new password (4 digits, only numbers). _We don't have to know the current password._

```bash
python main.py <IP_ADDRESS> <PASSWORD>
```

or

```bash
chmod +x main.py
./main.py <IP_ADDRESS> <PASSWORD>
```

### 📋 Sample results

successful

```bash
> ./main.py <IP_ADDRESS> <PASSWORD>
== Zebra password changer ==

[OK] 172.18.197.202 : password has been changed.
```

with errors

```bash
> ./main.py <IP_ADDRESS> <PASSWORD>
== Zebra password changer ==

[ERROR] IP address is invalid.
[ERROR] Please enter a 4-digit number!
```

request timeout

```bash
> ./main.py <IP_ADDRESS> <PASSWORD>
== Zebra password changer ==

[ERROR] Request timed out while connecting to remote host 172.18.197.2
```

simple help

```bash
> ./main.py help
== Zebra password changer ==

zebra-zpl-send-cli-py

Usage: python main.py <IP_ADDRESS> <PASSWORD (4 digit, only numbers)>
```

## 💥 Features

- Simple cli colours
- Argument checks & simple help argument
- Ip address validation
- Password validation
- Request timed-out exception

## 🎯 Tested Zebra printer models

- ZD 620
- ZD 621
- GK 420d

## 🤝 Contributing

Before contributing issues or pull requests, could you review the [Contributing Guidelines](./.github/CONTRIBUTING.md) first?

## 💬 Questions?

Feel free to [open an issue](http://github.com/angelside/zebra-password-changer-cli-py/issues/new).

## 🤩 Support

💙 If you like this project, give it a ⭐ and share it with friends!

[![GitHub-Sponsors](https://img.shields.io/badge/GitHub%20Sponsor-EA4AAA.svg?style=for-the-badge&logo=GitHub-Sponsors&logoColor=white)](https://github.com/sponsors/angelside)

## 🏛️ License

This project is open-sourced software licensed under the [MIT license](./LICENSE).
