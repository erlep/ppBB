from playwright.sync_api import Playwright, sync_playwright
from playwright.sync_api import expect

# Playwright test runner config (if using `pytest` or `playwright test`)
# If you're using Playwright directly in a script, this config is optional.

def pytest_configure(config):
  config.option.headless = True

# Optional: for direct use in scripts
BROWSER_ARGS = [
    "--no-sandbox",
    "--disable-gpu",
    "--disable-software-rasterizer",
    "--disable-dev-shm-usage",
    "--disable-setuid-sandbox",
    "--disable-accelerated-2d-canvas",
    "--disable-accelerated-video-decode",
    "--disable-features=UseOzonePlatform",
    "--disable-background-networking",
    "--disable-default-apps",
    "--disable-extensions",
    "--disable-sync",
    "--metrics-recording-only",
    "--mute-audio",
    "--no-first-run",
    "--no-zygote",
    "--single-process",
    "--headless=new"
]
