import asyncio
from playwright.async_api import Playwright, async_playwright, expect
async def run(playwright: Playwright) -> None:
  browser = await playwright.chromium.launch(headless=False)
  context = await browser.new_context()
  # Open new page
  page = await context.new_page()
  # Go to https://mapy.cz/zakladni?id=454777&source=firm&x=16.6152384&y=49.1856277&z=17
  await page.goto("https://mapy.cz/zakladni?id=454777&source=firm&x=16.6152384&y=49.1856277&z=17")
  # Click td:has-text("Benzín")
  await page.locator("td:has-text(\"Benzín\")").click()
  # ---------------------
  await context.storage_state(path="c:\\aac\\f1.txt")
  await context.close()
  await browser.close()
async def main() -> None:
  async with async_playwright() as playwright:
    await run(playwright)
asyncio.run(main())
