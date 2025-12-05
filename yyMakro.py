import asyncio
import re
import subprocess
import json
from pathlib import Path


URL = "https://www.makro.cz/prodejny/brno"
CACHE_FILE = Path("makro_price_cache.txt")


async def fetch_makro_price() -> str | None:
  """
  Fallback přístup když všechno ostatní selže:
  1. Zkusí curl s --http2
  2. Pokud selže, použije manuální cache
  """

  # Metoda 1: Zkus curl s HTTP/2 (méně detekce než Python knihovny)
  try:
    result = await asyncio.create_subprocess_exec(
        "curl",
        "-s",
        "-L",
        "--http2",
        "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "-H", "Accept-Language: cs-CZ,cs;q=0.9",
        URL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await result.communicate()

    if result.returncode == 0 and stdout:
      html = stdout.decode("utf-8", errors="ignore")

      # Regex pro Natural 95 cenu
      m = re.search(
          r"Natural\s*95[\s\S]{0,200}?(\d{1,3}[.,]\d{2})",
          html,
          re.IGNORECASE,
      )

      if m:
        price = m.group(1)
        # Ulož do cache
        CACHE_FILE.write_text(price, encoding="utf-8")
        return price
  except Exception as e:
    print(f"Curl failed: {e}")

  # Metoda 2: Přečti z cache (pokud existuje)
  if CACHE_FILE.exists():
    try:
      cached = CACHE_FILE.read_text(encoding="utf-8").strip()
      if cached and re.match(r"^\d{1,3}[.,]\d{2}$", cached):
        print("⚠️ Používám cached cenu (curl selhal)")
        return cached
    except Exception:
      pass

  # Metoda 3: Hardcodovaný fallback (aktualizuj ručně)
  print("⚠️ Všechny metody selhaly. Vraťte cenu z cache nebo aktualizujte ručně.")
  return None
async def main():
  price = await fetch_makro_price()
  if price:
    print(f"Makro cena: {price.replace('.', ',')}")
  else:
    print("Makro cena: nenalezena")


if __name__ == "__main__":
  asyncio.run(main())
