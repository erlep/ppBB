#!/bin/bash
#
# Ls2LstW.sh - Skript na vytvoreni file listu
# by peg
#
#           sudo -i
# Spusteni: sh /home/osboxes/aaPeg/ls2LstW/ls2LstW.sh  > /home/osboxes/aaPeg/ls2LstW/ls2LstW.log  2>&1

# Prefer US English and use UTF-8
export LC_ALL="en_US.UTF-8"
export LANG="en_US"

# Prac. adresar
cd /home/osboxes/aaPeg/ls2LstW
whoami                          >  All.Txt
pwd                             >> All.Txt

echo
echo "ls2Lst v1.0  App: ${0##*/}  Path: ${0} "

# Dump all file names 
ls -Ra -l -Q --time-style=full-iso / >> All.Txt

# Start Perl
perl ls2LstW.pl <  All.Txt  >  All.LstW

# Zip
zip -9 -v -o All_Lst  All.LstW
zip -9 -v -o All_Txt  All.Txt

# End
