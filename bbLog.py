# Benzín Brno - bbLog.py - logovani data a casu

# from bbCFG import *
import time
import getpass
import inspect
import socket
import sys
from datetime import datetime
import pytz  # $ pip install pytz
from bbCFG import bbDateLog, bbTimeZone, bbFmt2


# Log object
class oLog:
  ''' class oLog '''
  def __init__(self, znak='x'):
    ''' konstruktor '''
    self.start_time = time.perf_counter()
    self.zz = '-' * 2  # '--'
    self.z3 = '-' * 3  # '---'
    self.tilda = '~' * 2  # '~~'
    self.znak = znak
    # Now with TimeZone
    # self.date = time.strftime(bbDateLog)
    self.date = datetime.now(pytz.timezone(bbTimeZone)).strftime(bbDateLog)
    # Getting name of windows computer running python script? - https://bit.ly/3wxEjw7
    self.PcNm = socket.gethostname()
    # current user - https://bit.ly/2ZXSfmW
    self.UsNm = getpass.getuser()
    # script name - https://bit.ly/3EZT65T
    self.PyNm = inspect.stack()[1][0].f_code.co_name + '/' + inspect.stack()[2][0].f_code.co_name + ': '
    # print(inspect.stack()[1][3])
    # print(inspect.stack()[1].function)
    # Module Name - https://bit.ly/301VWIR -     print(sys.argv[0])
    self.PyNm = sys.argv[0]
    # ---06.11.2021--06:16--PC5406257--proj_sw_backup--T_TmChk-2.bat---{~~
    self.msg = self.z3 + self.date + self.zz + self.PcNm + self.zz + self.UsNm + self.zz + \
        self.PyNm + self.z3 + self.znak + self.tilda
  def print(self):
    ''' funkce print '''
    print(self.msg)
    print()

# globalni promenna
# log_start_time = time.time()
log_start_time = time.perf_counter()

# ---08.11.2021--14:22--PC5406257--pegerle--LogOpen/main: ---{~~
# ---06.11.2021--06:16--PC5406257--proj_sw_backup--T_TmChk-2.bat---{~~
def LogOpen():
  # start time
  global log_start_time
  log_start_time = time.perf_counter()
  print()
  log = oLog('{')
  log.print()

# ---05.11.2021--06:30--PC5406257--proj_sw_backup--T_TmChk-2.bat--- ~~}
def LogClose():
  print()
  log = oLog('}')
  log.print()
  # Execution time
  print("Total time:", bbFmt2.format(time.perf_counter() - log_start_time), 'seconds.')
  zz = '=' * 79
  print(zz)
  print(zz)

# main
def main():
  LogOpen()
  print('su tu - Log')
  LogClose()
  print()
  print('OkDone.')

# __name__
if __name__ == '__main__':
  main()
