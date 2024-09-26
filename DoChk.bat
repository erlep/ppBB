@echo off
  : Benzín Brno - Kontrola cen na benzinkach
  : python3 bbDoChk.py

  Echo.
  Echo %0
  Echo DoChk.bat - Kontrola cen na benzinkach
  Echo.

: Files
  set PyFile=bbDoChk.py

: vEnv
  set vEnv=c:\aaC\vEnv\vEnvPy\vEnv\Scripts\
  set Pyth=python.exe
  set PyEx=%vEnv%%Pyth%

: Nastaveni cesty
  set BatAppPath=%~dp0
  :pushd  \\192.168.123.10\vse\BatTool\
  cd /d %~dp0

  : python
  :c:\aaC\vEnv\vEnvPy\vEnv\Scripts\python.exe bbDoChk.py
  %PyEx%  %PyFile%  >> %~dpn0.Log 2>&1

  Echo End.
:Pause
