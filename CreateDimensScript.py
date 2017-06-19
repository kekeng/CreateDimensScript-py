#!/usr/bin/env python3
#for Eclipse project

from sys import argv
import os

#const str
RES_DIR = 'res'
DIR_PREFIX = 'values-sw'
FILE_NAME = 'dimens.xml'
LINE_PREFIX = '<dimen'

#default dp
DEFAULT_DP = 432

#createNewFiles func
def createNewFiles(defaultFile, targetFile, targetDp):
	for line in defaultFile.readlines():
		if line.strip().startswith(LINE_PREFIX):
			index1 = line.find('>')
			index2 = line.rfind('<')
			if index2-2 > index1+1 and index1 != -1:
				num = int(int(line[index1+1: index2-2]) * targetDp / DEFAULT_DP)
				if num == 0:
					num = 1
				print(num)

				newLine = line[0: index1+1] + str(num) + line[index2-2: len(line)]
				print(newLine)

				targetFile.writelines(newLine)
		else:
			targetFile.writelines(line)

#start func
def start():
	try:
		defaultFile = open('res/values/dimens.xml', 'r')
		dirNames = os.listdir(RES_DIR)
		print(dirNames)
		for dirName in dirNames:
			if dirName.startswith(DIR_PREFIX):
				filePath = os.getcwd() + os.path.sep + RES_DIR + os.path.sep + dirName + os.path.sep + FILE_NAME
				print(filePath)
				targetDp = int(dirName[len(DIR_PREFIX): len(dirName)-2])#-2 for suffix 'dp'
				print(targetDp)
				targetFile = open(filePath, 'w')
				createNewFiles(defaultFile, targetFile, targetDp)
				targetFile.close()
		defaultFile.close()
	except IOError:
		print('error by \'has no res/values/dimens.xml file\'')

#if cmd has argv, set it to default dp
if len(argv) > 1:
	DEFAULT_DP = int(argv[1])

start()

