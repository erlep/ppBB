@echo off
  : Benzín Brno - git git synchronizace
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
  echo su tu >> bbCeny.csv
  : Nahrani na git
  git commit -a  -m "win cmd line"
  git push
  git pull
  git status

:Pause
