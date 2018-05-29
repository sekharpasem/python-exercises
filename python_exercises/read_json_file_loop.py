import json
from pprint import pprint

def readJsonFile(filePath):
	print filePath
	json_object = json.load(open(filePath))

	pprint json_object.items()


if __name__ == '__main__':
    readJsonFile()