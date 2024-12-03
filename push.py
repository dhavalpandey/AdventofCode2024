import os
import datetime

def push(day):
    os.system("git add .")
    os.system(f'git commit -m "Day {day} complete"')
    os.system("git push origin main")

day = datetime.datetime.now().day
push(day)