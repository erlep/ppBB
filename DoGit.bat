@echo off
  : Benzín Brno - Update - ceny + GIT
  :

  Echo.
  Echo %0
  Echo DoGit.bat - Update - ceny + GIT
  Echo.

: Nastaveni cesty
  set BatAppPath=%~dp0
  cd /d %~dp0

  : Refresh
  git status
  git pull
  git status

  : Update ceny
  call DoChk.bat

  : Nahrani na git
  git commit -a  -m "Win cmd line"
  git push
  git pull
  git status

  Echo End.
:Pause
