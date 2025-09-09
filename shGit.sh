#!/bin/sh
#

  # : Benzín Brno - git git synchronizace
  # :
  # : git synchronizace

  echo
  echo "shGit.sh v1.0 App: ${0##*/}  Path: ${0} "

  # set the current working dir to the dir of the script in Bash? - https://bit.ly/3r4yHHu
  cd "$(dirname "$0")"

  # : Refresh
  git status
  git pull
  git status
  # : Modifikace obsahu
  # echo su tu vGitv11v >> bbCeny.csv
  # Ceny aktualizace
  python3 bbDoChk.py

  # : Nahrani na git
  # git commit -a  -m "AWS bash cmd line"
    git commit .  -m 'AWS bash cmd line'
  git push
  git pull
  git status

# End
