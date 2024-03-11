import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
  browser = await playwright.chromium.launch(headless=False)
  context = await browser.new_context()
  page = await context.new_page()
  # await page.goto("https://en.mapy.cz/zakladni?x=16.6036034&source=firm&id=13189726&y=49.1410562&z=17")
  await page.goto("https://mapy.cz/zakladni?x=16.6036034&source=firm&id=13189726&y=49.1410562&z=17")
  await page.locator(".szn-cmp-dialog-container").click()
  await page.locator(".szn-cmp-dialog-container").click()

  # ---------------------
  await context.close()
  await browser.close()


async def main() -> None:
  async with async_playwright() as playwright:
    await run(playwright)


asyncio.run(main())
