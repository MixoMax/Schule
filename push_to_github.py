import datetime
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().strftime("%m")
year = datetime.datetime.now().strftime("%Y")

git_commit_message = str(day) + "/" + str(month) + "/" + str(year) + " - " + str(input("Commit message: "))

git_commit_str = "git commit -m " + '"' + git_commit_message + '"'

print(os.system("git add ."))
print(os.system(git_commit_str))

t = str(input("Push to GitHub? (y/n): "))

if t.lower() in ["y", "yes", "1", "j", "ja"]:
    os.system("git push")
    print("Pushed to GitHub!")