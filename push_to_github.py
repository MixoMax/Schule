import datetime
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().strftime("%m")
year = datetime.datetime.now().strftime("%Y")

git_commit_message = str(day) + "/" + str(month) + "/" + str(year)

git_commit_str = "git commit -m " + '"' + git_commit_message + '"'

print(os.system("git add ."))
print(os.system(git_commit_str))