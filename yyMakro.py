import asyncio
import re

import cloudscraper
from bs4 import BeautifulSoup


URL = "https://www.makro.cz/prodejny/brno"


async def fetch_makro_price() -> str | None:
  # Use cloudscraper in async context
  loop = asyncio.get_event_loop()

  def _fetch():
    scraper = cloudscraper.create_scraper(
        browser={
            "browser": "chrome",
            "platform": "windows",
            "desktop": True,
        }
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "cs-CZ,cs;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    response = scraper.get(URL, headers=headers, timeout=30)
    response.raise_for_status()
    return response.text

  # Run in executor to avoid blocking
  html = await loop.run_in_executor(None, _fetch)

  # Parse with BeautifulSoup
  soup = BeautifulSoup(html, "html.parser")

  # Find all price cards
  cards = soup.select(".price.slide.element-position")
  price = None

  for card in cards:
    name_el = card.select_one(".field-name")
    if name_el:
      name = name_el.get_text(strip=True)
      if "Natural" in name and "95" in name:
        card_text = card.get_text()
        m = re.search(r"(\d{1,3}[.,]\d{2})", card_text)
        if m:
          price = m.group(1)
          break

  # Fallback: regex search in full HTML
  if not price:
    m = re.search(
        r"Natural\s*95[\s\S]*?Kč/l[\s\S]*?(\d{1,3}[.,]\d{2})",
        html,
        re.IGNORECASE,
    )
    price = m.group(1) if m else None

  return price
async def main():
  price = await fetch_makro_price()
  if price:
    print(f"Makro cena: {price.replace('.', ',')}")
  else:
    print("Makro cena: nenalezena")


if __name__ == "__main__":
  asyncio.run(main())
