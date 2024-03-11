# Benzín Brno - testovaci soubor

# Is asyncio too hard to use? Try Trio! - https://bit.ly/37yRrZN
import asks  # misto requests pro async
import time
import trio


asks.init("trio")

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
  response = await asks.get(url)
  print("Finished: ", url, len(response.content))

async def main(urls):
  start_time = time.time()
  async with trio.open_nursery() as nursery:
    for url in urls:
      nursery.start_soon(fetch, url)
  print("Total time:", time.time() - start_time)


if __name__ == "__main__":
  trio.run(main, urls)
