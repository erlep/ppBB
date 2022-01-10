@echo off
  : Benzín Brno - git synchronizace
  :
  : git synchronizace

  Echo.
  Echo %0 - git git synchronizace
  Echo.

  : Refresh
  git status
  git pull
  git status
  : Modifikace obsahu
  @REM echo su tu >> bbCeny.csv

  : Nahrani na git
  git commit -a  -m "Win cmd line"
  git push
  git pull
  git status

:Pause
