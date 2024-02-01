# -*- coding: UTF-8 -*-
from decimal import Decimal, getcontext
from datetime import timedelta,date
import os
import sys

ENABLE      = False # PLEASE SET TO "True" TO TURN ON THE SCRIPT!
START_DATE  = date(2023,1,1) # Date of your first commit, WARNING: IF this >= 20 years, it will take ~30s to calcuate pi.
COMMIT_TIME = "12:00:00+00:00" # Time of your commits will make
MESSAGE     = 'Hi👋,我是癫佬😋,这是我的看片神器😍.' # Commit message, you can change it to whatever you want.

FAKE_COMMIT = False #Development mode, will not commit to git, and print the command to the console.

def get_days(to_date = None):
    if to_date is None:
        to_date = date.today()
    return (to_date - START_DATE).days

def git_commit(date = None):
    if date is None:
        date = date.today()
    commit_command = f'git commit --allow-empty -m "{MESSAGE}" --date "{date.isoformat()}T{COMMIT_TIME}"'
    if FAKE_COMMIT:
        print(commit_command)
    else:
        os.system(commit_command)
    return 

def get_pi(n):
    getcontext().prec = n + 10
    pi = Decimal(0)
    for k in range(n + 10):
        pi += (Decimal(1) / 16**k) * ((Decimal(4) / (8*k + 1)) - (Decimal(2) / (8*k + 4)) - (Decimal(1) / (8*k + 5)) - (Decimal(1) / (8*k + 6)))
    pi_str = str(pi)
    return pi_str[:n+2].replace('.', '')[n - 1]

def main():
    if not ENABLE and not FAKE_COMMIT:
        sys.stderr.write("To prevent wrong commits, PLEASE SET \"ENABLE\" to \"True\" to turn on the script!\n")
        return
    if '--back' in sys.argv:
        commit_date = date.today()
        while get_days(commit_date) >= 0:
            for _i in range(int(get_pi(get_days(commit_date + timedelta(days=1))))):
                git_commit(commit_date)
            commit_date = commit_date + timedelta(days=-1)
    for _i in range(int(get_pi(get_days(date.today() + timedelta(days=1))))):
        git_commit(date.today())
if __name__ == '__main__':
    main()
