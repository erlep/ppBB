# playwright.config.py

# Argumenty pro Chromium při asynchronním použití Playwrightu
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
