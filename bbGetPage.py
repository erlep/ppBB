# Benzín Brno - bbGetPage.py - stahne stranku

# Scrape a Dynamic Website with Python - https://bit.ly/3Dm2GPs
# BeautifulSoup, Selenium, Pyppeteer, Playwright, and Web Scraping API + requests_html
# Hybrid verze muze pouzivat selenium | playwright | requests_html

# pip install playwright
# playwright install
# playwright open   --save-storage c:\aac\f1.txt  https://mapy.cz/s/megolelafe

# pip install selenium
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
# 20.12.2023 - How to save and load cookies in Playwright? - https://bit.ly/48otNJb
import asyncio
import sys
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
# playwright - https://playwright.dev/python/docs/locators
async def page_content_playwright(url):
  # Use async version of Playwright
  from playwright.async_api import async_playwright
  from playwright_config import BROWSER_ARGS  # playwright konfigurace

  import json
  from bbCFG import bbTimeGet, bbHeadLes, bbUsrAgnt
  # print('url', url)

  # page_get
  async def page_get():
    async with async_playwright() as pw:
      # Reuse signed in state - https://bit.ly/3C4IjIO
      # Create a new context with the saved storage state.
      # context = await browser.new_context(storage_state='bbMakro.cookies.json')
      # 20.12.2023 - How to save and load cookies in Playwright? - https://bit.ly/48otNJb
      # BrowserContext - https://bit.ly/473ClUN
      # Playwright => Allow all cookies automatically - https://bit.ly/3Tu6Vny
      cookies_name = ''
      if 'mapy' in url:
        # mapy.cz
        cookies_name = 'bbMapy.cookies.json'
        browser = await pw.chromium.launch(headless=bbHeadLes)  # Don't Show the browser True / False  , slow_mo=50
        try:
          # context = await browser.new_context()
          context = await browser.new_context(
              user_agent=bbUsrAgnt,
              storage_state=cookies_name
          )
        except:  # catch *all* exceptions # pylint: disable=bare-except
          e = sys.exc_info()[0]
          print("Error v bbGetPage.py. new_context: url", url, '\t\t', e)
          return ''
        # Open new page
        try:
          page = await context.new_page()
        except:  # catch *all* exceptions # pylint: disable=bare-except
          e = sys.exc_info()[0]
          print("Error v bbGetPage.py. new_page: url", url, '\t\t', e)
          return ''
        # await context.storage_state(path='bbMapy.cookies.json') # ukladani cookies vypnuto 20.06.2024 17:23
        await page.goto(url, timeout=bbTimeGet)  # Wait for 10 second
        # hledam zda je na strance tlacitko ' I agree' - Full Xpath /html/body/div[2]//div/div/div[2]/button[2]
        mapyTxt = ".szn-cmp-dialog-container"
        # oprava 27.06.2025 13:35 - nezna .is_visible(timeout=bbTimeGet)):
        # if (await page.locator(mapyTxt).is_visible(timeout=bbTimeGet)):
        if (await page.wait_for_selector(mapyTxt, timeout=bbTimeGet)):
          if (await page.locator(mapyTxt).is_visible()):
            # print('jsem v ', mapyTxt)
            try:
              await page.locator(mapyTxt).click(timeout=bbTimeGet)
              # zavru prohlizec
              page_content = await page.content()
              await context.close()
              await browser.close()
              return page_content
            except:  # catch *all* exceptions # pylint: disable=bare-except
              e = sys.exc_info()[0]
              print("Error v bbGetPage.py. Neni povoleno cookies: url", url, '\t\t', e)
              return ''
        # await page.locator("text=Benzín").click()
        # Click td:has-text("Benzín")
        # hledam zda je na strance  'Benzín'
        # try:
        #   await page.locator("td:has-text(\"Benzín\")").click()
        # except:  # catch *all* exceptions # pylint: disable=bare-except
        #   e = sys.exc_info()[0]
        #   print("Error v bbGetPage.py. Neni Benzin: url", url, '\t\t', e)
      elif 'makro' in url:
        # makro.cz
        cookies_name = 'bbMakro.cookies.json'
        browser = await pw.chromium.launch(
            headless=bbHeadLes,
            args=['--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage'])  # Don't Show the browser True / False  , slow_mo=50
        try:
          # context = await browser.new_context()
          context = await browser.new_context(
              user_agent=bbUsrAgnt,
              storage_state=cookies_name
          )
        except:  # catch *all* exceptions # pylint: disable=bare-except
          e = sys.exc_info()[0]
          print("Error v bbGetPage.py. Neni povoleno cookies: url", url, '\t\t', e)
          return ''
        # Open new page
        try:
          page = await context.new_page()
        except:  # catch *all* exceptions # pylint: disable=bare-except
          e = sys.exc_info()[0]
          print("Error v bbGetPage.py. new_page: url", url, '\t\t', e)
          return ''
        # Nastavení viewportu
        await page.set_viewport_size({'width': 1280, 'height': 720})
        # await context.storage_state(path='bbMapy.cookies.json') # ukladani cookies vypnuto 20.06.2024 17:23
        # Navigace na stránku
        await page.goto(url, timeout=bbTimeGet)  # Wait for 10 second

        # Čekání na načtení stránky
        await page.wait_for_load_state('load')

        # # Čekání na konkrétní prvek
        # await page.wait_for_selector('#some-element')

        # Kontrola síťových požadavků
        page.on('requestfailed', lambda request: print(f'Request failed: {request.url}'))

        # Evaluace skriptu
        await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')

      else:
        # jine nez mapy a makro
        browser = await pw.chromium.launch(headless=bbHeadLes)  # Don't Show the browser True / False  , slow_mo=50
        context = await browser.new_context()
        # Open new page
        page = await context.new_page()
        await page.goto(url, timeout=bbTimeGet)  # Wait for 10 second
      # get page
      page_content = await page.content()
      # print('page_content', page_content)
      # # save the cookies
      # if cookies_name != '':
      #   with open(cookies_name, "w", encoding='UTF-8') as f:
      #     await f.write(json.dumps(page_content.cookies()))

      await context.close()
      await browser.close()
      return page_content
      # page_get(): - end
  # page_content
  page_content = await page_get()
  return page_content
  # page_content_playwright(url): - end
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
  # url = r'https://bit.ly/3izRnLE'
  url = 'https://bit.ly/3izRnLE'        # 'Tesco - mapy.cz        ', 'https://bit.ly/3izRnLE'
  url = 'https://mapy.cz/s/megolelafe'  # 'Shell Olomoucká        ', 'https://mapy.cz/s/megolelafe'
  url = 'https://mapy.cz/s/kepegubeve'  # 'MOL Olomoucká          ', 'https://mapy.cz/s/kepegubeve'
  url = 'https://mapy.cz/s/jatejehoda'  # 'OMV IKEA               ', 'https://mapy.cz/s/jatejehoda'
  url = 'https://mapy.cz/s/cutobofugo'  # 'EuroOil Opuštěná       ', 'https://mapy.cz/s/cutobofugo'
  # url = 'https://mapy.cz/s/rodokobesa'  # 'AVIA                   ', 'https://mapy.cz/s/rodokobesa'
  # url = 'https://mapy.cz/s/jajularama'  # 'Eurobit                ', 'https://mapy.cz/s/jajularama'
  tst = await GetPage(url)
  print('def GetPage(): ', type(tst), '  length', len(tst))
  print('OkDone.')

# __name__
if __name__ == '__main__':
  print('\n\nmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
  # main()
  asyncio.run(main())
