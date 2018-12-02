import os
import threading, time, datetime
from github import Github #pip install PyGithub

g = Github('willie-isom', "isom1005")
repo = g.get_user().get_repo('willie-isom')
commits = repo.get_commits(sha = 'master', since = datetime.datetime.now() - datetime.timedelta(days = 7), until = datetime.datetime.now())
repo = g.get_repo("willie-isom/isom-Line")

#contents = repo.get_contents("1.txt")
#repo.update_file(contents.path, "more tests1", 'None', contents.sha, branch="master")

def job():
	while 1:
		contents = repo.get_contents("2.txt")
		contents = str(contents.decoded_content, encoding = "utf-8")
		print('[*]---',contents)
		time.sleep(1)

def main():
	while 1:
		time.sleep(1)
		
t = threading.Thread(target = job)
t.setDaemon(True)
t.start()	

main()						
