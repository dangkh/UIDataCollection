import numpy as np
import json
import os

def readData(link = "./DataVIN/", prefixName = "Data"):
	if os.path.isdir(link):
		onlyfiles = [f for f in os.listdir(link) if os.path.isfile(link+f)]
		jsonFiles = [link+x for x in onlyfiles if x[-4:] == 'json']
		print(jsonFiles)
	else:
		print("imported link is not exist")
		print("DataVIN folder is created, run again!")
		os.makedir(link)
		onlyfiles = [f for f in os.listdir(link) if os.path.isfile(link+f)]
		jsonFiles = [link+x for x in onlyfiles if x[-4:] == 'json']
		print(jsonFiles)
	return jsonFiles

if __name__ == "__main__":
	readData()