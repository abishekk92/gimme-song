import subprocess
import json
from pprint import pprint


def curlTextProcessing(text):

	curl = "curl -d " + "\"text=" + text + "\"" + " http://text-processing.com/api/sentiment/"

	child = subprocess.Popen(curl, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

	commsout, commserr = child.communicate()

	data = json.loads(commsout)
	#pprint(data)
	#print "NEG: ", data["probability"]["neg"]

	return [data["probability"]["pos"], data["probability"]["neg"], data["probability"]["neutral"]]

#if __name__ == '__main__':
#	text = "Hey Jude, don't make it bad."

#	l = []
#	l = curlTextProcessing(text)

#	print l
