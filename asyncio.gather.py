# Getting values from functions that run as asyncio tasks - https://bit.ly/3yMaxXJ
#!/usr/bin/env python3
import asyncio

@asyncio.coroutine
def func_normal():
  print('A')
  yield from asyncio.sleep(5)
  print('B')
  return 'saad'

@asyncio.coroutine
def func_infinite():
  for i in range(10):
    print("--%d" % i)
  return 'saad2'

loop = asyncio.get_event_loop()
tasks = func_normal(), func_infinite(), func_normal()
l = loop.run_until_complete(asyncio.gather(*tasks))
print('l', l)
loop.close()
