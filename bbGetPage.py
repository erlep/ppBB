# Benzín Brno - bbGetPage.py - stahne stranku

# Scrape a Dynamic Website with Python - https://bit.ly/3Dm2GPs
# BeautifulSoup, Selenium, Pyppeteer, Playwright, and Web Scraping API + requests_html
# Hybrid verze muze pouzivat selenium | playwright | requests_html

# pip install selenium
# pip install playwright
# playwright install
# pip install requests-html
# cmd:> python bbGetPage.py

# playwright vs selenium - https://bit.ly/3aA7UuI
# Puppeteer, Selenium, Playwright, Cypress – how to choose? - https://bit.ly/3aCUMVJ

# from bbCFG import *
# # from bbLST import *  # nemuze tady byt jinak je cyklicky odkaz
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import os
# import asyncio
# from playwright.async_api import async_playwright
# from requests.sessions import session
# from requests_html import AsyncHTMLSession

# selenium
def page_content_selenium(url):
  from selenium import webdriver
  options = webdriver.ChromeOptions()
  options.add_argument('--ignore-ssl-errors=yes')
  options.add_argument('--ignore-certificate-errors')
  driver = webdriver.Chrome('d:/Utils/chromedriver/chromedriver.exe', options=options)
  driver.get(url)
  page_content = driver.page_source
  driver.close()
  return page_content

# playwright
def page_content_playwright(url):
  # Use async version of Playwright
  from playwright.async_api import async_playwright
  import asyncio

  async def page_get():
    async with async_playwright() as p:
      browser = await p.chromium.launch()
      page = await browser.new_page()
      await page.goto(url, timeout=0)
      page_content = await page.content()
      await browser.close()
      return page_content
  # page_content
  page_content = asyncio.run(page_get())
  return page_content

# requests_html
def page_content_requests_html(url):
  from requests_html import AsyncHTMLSession
  asession = AsyncHTMLSession()
  # JavaScript Support async

  async def get_page():
    r = await asession.get(url)
    await r.html.arender()
    page_content = r.html.html
    return page_content
  # musi se prevest na string
  page_content = str(asession.run(get_page))
  return page_content

# GetPage
def GetPage(url):
  from bbCFG import brint, bbRender
  brint('GetPage:', 'url', url)
  # selenium | playwright | requests_html
  # bbRender = 'requests_html'
  # print('bbRender:', bbRender)
  if bbRender == 'selenium':
    page_content = page_content_selenium
  elif bbRender == 'playwright':
    page_content = page_content_playwright
  else:
    page_content = page_content_requests_html
  # get page_content()
  return page_content(url)

# main
def main():
  url = r'https://bit.ly/3izRnLE'
  print('def GetPage(): ', GetPage(url))
  print('OkDone.')

# __name__
if __name__ == '__main__':
  main()
