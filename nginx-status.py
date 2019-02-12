import time
import datetime
import os
import socket


def oldfile(path):
	hostname = socket.gethostname()
	datetime2 = time.time()
	datetime1 = time.localtime(datetime2)
	files = os.listdir(dir)
	for file in files:
		filePath = dir + "/" + file
		if os.path.isfile(filePath):
			last1 = os.stat(filePath).st_mtime
			filetime = time.localtime(last1)
			if datetime1.tm_year - filetime.tm_year >= 1:
				print ("[{\"endpoint\":\"%s\",\"tags\":\"%s\",\"timestamp\":%s,\"step\":61,\"value\":1,\"counter     Type\":\"GAUGE\",\"metric\":\"check_httpsfile\"}]"%(hostname,filePath,datetime2))
			elif datetime1.tm_year - filetime.tm_year == 0 and datetime1.tm_mon - filetime.tm_mon >= 3:
				print ("[{\"endpoint\":\"%s\",\"tags\":\"%s\",\"timestamp\":%s,\"step\":60,\"value\":1,\"counter     Type\":\"GAUGE\",\"metric\":\"check _ttpsfile\"}]"%(hostname,filePath,datetime2))
			else:
				print ("[{\"endpoint\":\"%s\",\"tags\":\"%s\",\"timestamp\":%s,\"step\":60,\"value\":0,\"counter     Type\":\"GAUGE\",\"metric\":\"check_httpsfile\"}]"%(hostname,filePath,datetime2))
		else:
			oldfile(filePath)

if __name__ == "__main__":
	dir = '/home/xpmotors/test'
	datetimenow = time.localtime(time.time())
	oldfile(dir)