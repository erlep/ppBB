#!/bin/sh
#

  # : Benzín Brno - git git synchronizace
  # :
  # : git synchronizace

  echo
  echo "shGit.sh v1.0 App: ${0##*/}  Path: ${0} "


  # : Refresh
  git status
  git pull
  git status
  # : Modifikace obsahu
  echo su tu vGitv8v >> bbCeny.csv
  # : Nahrani na git
  # git commit -a  -m "AWS bash cmd line"
    git commit .  -m 'AWS bash cmd line'
  git push
  git pull
  git status

:Pause


# End
