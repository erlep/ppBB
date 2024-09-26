# Web Scraping With Playwright - https://bit.ly/3PEM6S6
# Asynchronous Web Scraping with Python, aiohttp, and asyncio - https://bit.ly/39wZsPM
# asyncio: collecting results from an async function in an executor - https://bit.ly/3LvUe46

import asyncio
from asyncio.windows_events import NULL
import time

from playwright.async_api import async_playwright

urls = [
    # 'http://www.facebook.com',
    # 'http://www.twitter.com',
    # 'http://www.instagram.com',
    # 'http://www.google.com',
    # 'http://www.youtube.com',
    'http://www.medium.com',
    'https://git-scm.com',
    'http://www.github.com',
    'http://www.gitlab.com',
    'http://www.python.org',
    'http://python-requests.org',
    'http://trio.readthedocs.io'
]

async def fetch(url):
  print("Start: ", url)
  response = NULL
  async with async_playwright() as pw:
    browser = await pw.chromium.launch()
    page = await browser.new_page()
    await page.goto(url, timeout=0)
    response = await page.content()
    await browser.close()
  print("Finished: ", url, len(response))
  return len(response)

def main(urls):
  start_time = time.time()
  loop = asyncio.get_event_loop()
  tasks = []
  for url in urls:
    task = asyncio.ensure_future(fetch(url))
    tasks.append(task)
  res = loop.run_until_complete(asyncio.gather(*tasks))
  print('res', res)
  print("Total time:", time.time() - start_time)

if __name__ == '__main__':
  main(urls)
