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
################################################################################
# 18.05.2022 - zmena na asyncio, trio nelze s playwright
import asyncio
################################################################################
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
################################################################################
# playwright
async def page_content_playwright(url):
  # Use async version of Playwright
  from playwright.async_api import async_playwright
  import json
  # page_get

  async def page_get():
    async with async_playwright() as pw:
      browser = await pw.chromium.launch(headless=True)  # Show the browser True / False  , slow_mo=50
      # context https://bit.ly/3PBmrZ7
      context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36')
      page = await context.new_page()
      # cookie file
      cookie_file = open('bbMakro.cookies.json')
      cookies = json.load(cookie_file)
      await context.add_cookies(cookies)
      # get page
      await page.goto(url, timeout=30000)  # Wait for 10 second
      page_content = await page.content()
      await browser.close()
      return page_content
  # page_content
  page_content = await page_get()
  return page_content
################################################################################
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
################################################################################
# GetPage
async def GetPage(url):
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
  return await page_content(url)

# main
async def main():
  url = r'https://bit.ly/3izRnLE'
  tst = await GetPage(url)
  print('def GetPage(): ', tst)
  print('OkDone.')

# __name__
if __name__ == '__main__':
  # main()
  asyncio.run(main())
