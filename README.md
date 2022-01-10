# ppBB
Python Project Benzin Brno

pridano

verze z pc

bbNmVR = 0.26
bbNmVR = 0.25
vGitv8v
vGitv9v
vGitv10v
vGitv11v
---

## odkazy

https://share.streamlit.io/erlep/ppbb/main/bbWeb.py

picture


<iframe src="https://share.streamlit.io/erlep/ppbb/main/bbWeb.py"></iframe>


---

# Benzin_Brno - Natural 95 prices in Brno - Python Version

Google Sheet script to monitor petrol prices in Brno city.

[![Benzin-Akt](https://docs.google.com/spreadsheets/d/e/2PACX-1vStPblBtmg4O4ddc6pOF9edeu-IzfsjxmynNpqzs3me9czw5K1aIIBw4HW9Cni9vM7Kse8QQTh0GG8a/pubchart?oid=678203108&format=image)](https://docs.google.com/spreadsheets/d/e/2PACX-1vStPblBtmg4O4ddc6pOF9edeu-IzfsjxmynNpqzs3me9czw5K1aIIBw4HW9Cni9vM7Kse8QQTh0GG8a/pubchart?oid=678203108&format=interactive)

[![Benzin-Vyvoj](https://docs.google.com/spreadsheets/d/e/2PACX-1vStPblBtmg4O4ddc6pOF9edeu-IzfsjxmynNpqzs3me9czw5K1aIIBw4HW9Cni9vM7Kse8QQTh0GG8a/pubchart?oid=451896964&format=image)](https://docs.google.com/spreadsheets/d/e/2PACX-1vStPblBtmg4O4ddc6pOF9edeu-IzfsjxmynNpqzs3me9czw5K1aIIBw4HW9Cni9vM7Kse8QQTh0GG8a/pubchart?oid=451896964&format=interactive)

## Benzin - Google Sheet https://cutt.ly/benzin

Aktuální graf cen: https://cutt.ly/Benzin-Akt

Vývoj cen: https://cutt.ly/Benzin-Vyvoj

Google Sheet: https://cutt.ly/benzin

Benzin_Brno na Mapy.Cz: https://frame.mapy.cz/s/lohezoreba

## GitHub URL - https://github.com/erlep/Benzin_Brno

## made by peg - https://GitHub.com/ErleP

## --

--

History:
07.01.2022 14:00
bbNmVR = 0.25
- CSV file
- cmd a bash scripts
----
- new Python Version
- v4 klikaci obrazek
--

--
Cannot get cron to work on Amazon EC2? - https://bit.ly/3JPuyzH
crontab -l
crontab
https://crontab-generator.org
  vi - Esc and enter :wq).
crontab -e
  kazdy den 8:08
8 8 * * * /home/ec2-user/xGit/ppBB/shGit.sh > /home/ec2-user/xGit/ppBB/shGit.log
  kazdou hodinu v 11 minut
11 * * * * /home/ec2-user/xGit/ppBB/shGit.sh > /home/ec2-user/xGit/ppBB/shGit.log

*/15 * * * * /home/ec2-user/xGit/ppBB/shGit.sh > /home/ec2-user/xGit/ppBB/shGit.log

--
--
set the current working dir to the dir of the script in Bash? - https://bit.ly/3r4yHHu
#!/bin/bash
cd "$(dirname "$0")"
--
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

