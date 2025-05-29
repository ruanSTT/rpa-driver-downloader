from .base import BaseDriver
import platform
import requests


class Chromium(BaseDriver):
    def __init__(self, version: str = None):
        self.version = version
        super().__init__(version=version)


    @property
    def key_name(self) -> str:
        return "chromiumdriver_path"


    def get_latest_version(self) -> str:
        url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
        data = requests.get(url).json()
        return data["channels"]["Stable"]["version"]
    

    def get_download_url(self) -> str:
        os_name = platform.system()

        if self.version:
            version_url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
            data = requests.get(version_url).json()
            versions = data["versions"]
            version_info = next((v for v in versions if v["version"] == self.version), None)
            if not version_info:
                raise ValueError(
                    f"❌ Chromium version '{self.version}' not found.\n"
                    f"🔗 See all versions at: https://googlechromelabs.github.io/chrome-for-testing/"
                )
            
            # DEBUG: conferir as chaves
            print("Available download keys:", version_info["downloads"].keys())

            # A chave pode variar, tente acessar 'chromedriver' ou 'chromedriver_win64'
            downloads = version_info["downloads"].get("chromedriver")
            if downloads is None:
                downloads = version_info["downloads"].get("chromedriver_win64")
            
            if downloads is None:
                raise KeyError("Could not find 'chromedriver' or 'chromedriver_win64' keys in downloads.")

        else:
            url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
            data = requests.get(url).json()
            downloads = data["channels"]["Stable"]["downloads"]["chromedriver"]

        for item in downloads:
            if os_name == "Windows" and item["platform"] == "win64":
                return item["url"]
            elif os_name == "Linux" and item["platform"] == "linux64":
                return item["url"]
            elif os_name == "Darwin" and item["platform"] == "mac-x64":
                return item["url"]

        raise FileNotFoundError("Chromium driver download URL not found.")