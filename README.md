# 🧩 rpa-driver-downloader

**rpa-driver-downloader** is a lightweight Python package that automatically downloads and manages the latest WebDriver binaries (Gecko, Chromium, Edge) for browser automation using **Selenium**, **BotCity**, or any other RPA tool.

Whether you're automating browsers on Linux, Windows, or macOS, this library ensures that the required driver is downloaded and ready to use — with just one line of code.

---

## 🚀 Features

- ✅ Automatically downloads GeckoDriver, ChromeDriver, and EdgeDriver
- 💾 Stores drivers locally in a /drivers/ folder
- 📍 Saves driver paths in settings.json for future reuse
- 🧠 Detects your OS and architecture automatically
- 🔁 If a newer version of the driver is detected, the old one is automatically replaced
- 🔄 Returns absolute path to be used with Selenium or BotCity
- ⚙️ Supports optional version selection → pass a specific version if needed!
  - 📌 If not provided, the latest stable version is used by default
  - 🔗 If an invalid version is passed, a clear error is raised with a link to available versions
- 🧪 Great for testing and RPA automation workflows



## 📦 Installation

```bash
pip install rpa-driver-downloader
```


## ⚙️ Usage

```bash
from rpa_driver_downloader import Gecko, Chromium, Edge

# 1) Using instance method (old way, still works)
gecko_path = Gecko(version="0.34.0").path_for_the_driver()
chrome_path = Chromium(version="122.0.6261.95").path_for_the_driver()
edge_path = Edge(version="124.0.2478.0").path_for_the_driver()

# 2) Using class method (recommended for simplicity)
gecko_path = Gecko.get_driver_path(version="0.34.0")
chrome_path = Chromium.get_driver_path(version="122.0.6261.95")
edge_path = Edge.get_driver_path(version="124.0.2478.0")

# 3) Assigning to variables for reuse
gecko = Gecko(version="0.34.0")
gecko_path = gecko.path_for_the_driver()
```
This will:
- Check if the driver exists locally
- If not *found* or **outdated**, it will download and **replace** it
- Return the full absolute path to the binary

If a version is specified:
- It will try to download the requested version, **otherwise it will try to download the latest available version**
- If the version is invalid or not found, it will raise an error with a link to the available versions


## Example: Using with Selenium

```bash
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from rpa_driver_downloader import Gecko

# Instantiate the Options
firefox_options = Options()

# ✅ Using a specific version
driver = webdriver.Firefox(
    options=firefox_options,
    executable_path=Gecko.get_driver_path(version="0.34.0")
)
driver.get("https://github.com/ruanSTT/rpa-driver-downloader")

# ✅ Using the latest available version (default behavior)
driver = webdriver.Firefox(
    options=firefox_options,
    executable_path=Gecko.get_driver_path()  # <- Don’t pass any parameter!
)
driver.get("https://github.com/ruanSTT/rpa-driver-downloader")
```


## Example: Using with BotCity

```bash
from botcity.web import WebBot
from rpa_driver_downloader import Gecko

# Instantiate the WebBot
bot = WebBot()

# ✅ Using a specific version
bot.driver_path(driver_path=Gecko.get_driver_path(version="0.34.0"))
bot.browse("https://github.com/ruanSTT/rpa-driver-downloader")

# ✅ Using the latest available version (default behavior)
bot.driver_path(driver_path=Gecko.get_driver_path())  # <- Don’t pass any parameter!
bot.browse("https://github.com/ruanSTT/rpa-driver-downloader")
```


## 🌐 Supported Browsers & Platforms

| Browser | Windows | Linux | macOS |
| ------- | ------- | ----- | ----- |
| Firefox | ✅       | ✅     | ✅     |
| Chrome  | ✅       | ✅     | ✅     |
| Edge    | ✅       | ✅     | ✅     |


## 📁 Project Structure

```bash
rpa-driver-downloader/
├── rpa_driver_downloader/
│   ├── __init__.py
│   ├── base.py
│   ├── gecko.py
│   ├── chromium.py
│   └── edge.py
├── settings.json          # Created automatically
├── drivers/               # Driver binaries stored here
├── setup.py
└── README.md
```


## ⚠️ Python Compatibility

This library is compatible with:

✅ Python 3.7 up to **3.12.3** (inclusive)

Versions higher than 3.12.3 are currently **not supported** due to instability and possible incompatibilities.

Internally, the library depends on `requests>=2.31.0`, which does not rely on the deprecated `cgi` module.

If you are using Python 3.12.3 or lower, you should not encounter compatibility issues.

Please note that support for Python versions greater than 3.12.3 will be considered once those versions stabilize.


## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

rpa-driver-downloader is a Python package that automatically downloads and manages the latest Gecko, Chrome, and Edge WebDriver binaries. Designed for use with Selenium and RPA tools like BotCity, it detects the OS and ensures the correct driver is always available — no manual download required.


## 🤝 Contributing
Contributions, issues and feature requests are welcome!
Feel free to check the issues page or submit a pull request.