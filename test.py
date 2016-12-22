
# !/usr/bin/env python
import webbrowser
import os
import sys

def addTab():
	file = open(path, "a")
	checker = "http"
	if len(sys.argv) == 2:
		if checker in sys.argv[1]:
			file.write(sys.argv[1]+ "\n")
			print("File Updated! " +sys.argv[1]+ " added.")
	else:	
		newTab = input("Enter URL to add: ")
		if checker in newTab:
			file.write(newTab+ "\n")
			print("File Updated! " +newTab+ " added.")
		else:
			print("Is this a URL? Does not contain " +checker+ " Try again.")
#--------------------Begin--------------------------
#Remove all irrevelant
'''
def chrome(url):
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
'''
#change path to recover.txt location
# path = "C:/Users/Alex Wang/projects/GoogSearch/recover.txt"
path = "./recover.txt"
# path = "G:/session_buddy_export_2016_10_14_02_08_43.txt"
totalLines = 0
my_urls = []

# if not os.path.exits security concerns
if not os.path.isfile(path):
	file = open("recover.txt", "w")
	file.close()

if len(sys.argv) == 2:
	addTab()
	


else :
	cnt = 0
	file = open(path, "r+")
	for line in file:
		if line != "\n":
			my_urls.append(line)
			print("{} : {}".format(cnt, line))
			cnt += 1
			totalLines = totalLines + 1


	ans = ""
	while ans.lower() != "oa" and ans.lower() != "o" and ans.lower() != "a" and ans.lower() != "d" and ans.lower() != "x":
		ans = input("Open All (OA) | Open Entry (O) | Add Entry (A) | Delete Entry (D) | Cancel (X): ")
		ans = ans.lower()
	
	if ans.lower() == "oa":
		for line in my_urls:
			os.startfile(line)	

	elif ans.lower() == "o":
		ans = input("Enter an Entry Num: ")
		entry = int(ans)
		os.startfile(my_urls[entry])

	elif ans.lower() == "a":
		file.close()
		addTab()

	elif ans.lower() == "d":
		file.close()
		file = open(path, "w+")
		ans = 999

		while (int(ans) > totalLines):
			ans = input("Enter Entry Num: ")
			ans = int(ans)
		print(my_urls.pop(ans) + "--= Removed =--")
		file.writelines(my_urls)
		
	elif ans.lower() == "x":
		print("")
		# ans = input("Press Enter to exit.")

	else:
		ans = input("Invalid option. Exiting.....press Enter")

	file.close()

	
	