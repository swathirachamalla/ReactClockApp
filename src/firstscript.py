from github import Github
from datetime import datetime,timedelta
import os
import pytz
print("Executing First script")
g = Github("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")
repo = g.get_repo("swathirachamalla/ReactClockApp")
Branch= repo.get_branch("Development")
sha =Branch.commit.sha  
commit = repo.get_commit(sha=sha)
start_time = commit.commit.author.date
print(start_time)
end_time =datetime.now(pytz.timezone('GMT'))
print(end_time)
c = datetime(end_time.year,end_time.month,end_time.day,end_time.hour,end_time.minute,end_time.second)- datetime(start_time.year,start_time.month,start_time.day,start_time.hour,start_time.minute,start_time.second)
print("c")
if c > timedelta(minutes=5):
    print("Executing Script.sh")
    os.system("bash script.sh")