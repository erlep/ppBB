@echo off
  : Benzín Brno - Web - streamlit app
  :
  : streamlit run bbWeb.py


  Echo.
  Echo %0
  Echo DoWeb.bat - Web - streamlit app
  Echo.

: Files
  set PyFile=bbWeb.py

: vEnv
  set vEnv=c:\aaC\vEnv\vEnvPy\vEnv\Scripts\
  set Pyth=python.exe
  set Pyth=streamlit.exe
  set PyEx=%vEnv%%Pyth%

: Nastaveni cesty
  set BatAppPath=%~dp0
  :pushd  \\192.168.123.10\vse\BatTool\
  cd /d %~dp0

  : python
  :c:\aaC\vEnv\vEnvPy\vEnv\Scripts\python.exe bbDoChk.py
  start %PyEx%  run  %PyFile%  >> %~dpn0.Log 2>&1
  Echo End.
:Pause
