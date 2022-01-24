# Benzín Brno - bbLog.py - logovani data a casu

# from bbCFG import *

# Log object
class oLog:
  ''' class oLog '''
  def __init__(self, znak='x'):
    ''' konstruktor '''
    from bbCFG import bbDateLog

    import time
    import inspect
    import socket
    import getpass
    import sys

    self.zz = '-' * 2  # '--'
    self.z3 = '-' * 3  # '---'
    self.tilda = '~' * 2  # '~~'
    self.znak = znak
    self.date = time.strftime(bbDateLog)
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

# ---08.11.2021--14:22--PC5406257--pegerle--LogOpen/main: ---{~~
# ---06.11.2021--06:16--PC5406257--proj_sw_backup--T_TmChk-2.bat---{~~
def LogOpen():
  print()
  log = oLog('{')
  log.print()

# ---05.11.2021--06:30--PC5406257--proj_sw_backup--T_TmChk-2.bat--- ~~}
def LogClose():
  print()
  log = oLog('}')
  log.print()
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
