from playwright.async_api import async_playwright
import asyncio

async def main():
  async with async_playwright() as pw:
    browser = await pw.chromium.launch(
        headless=False  # Show the browser
    )
    page = await browser.new_page()
    await page.goto('https://www.makro.cz/prodejny/brno')
    # Data Extraction Code Here
    await page.wait_for_timeout(10000)  # Wait for 1 second
    page_content = await page.content()
    print(page_content)
    await browser.close()

if __name__ == '__main__':
  asyncio.run(main())
