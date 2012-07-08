from os import listdir
from os.path import isfile

import htmlparse
import sentiment

if __name__ == '__main__':

	htmlparser = htmlparse.HTMLParserHandler()

	onlyfiles = [f for f in listdir("/home/omega9/Songs")]

	dir = "/home/omega9/Songs/"

	fr = open("values", "w")

	for i in onlyfiles:
		
		f = dir + i

		file = open(f, "r")

		inp = ' '.join(file.readlines())

		htmlparser.feed(inp)

		Title, Lyrics = htmlparser.getData()

		ly = ''.join(Lyrics)

		if len(ly) != 0:

			l = []

			l = sentiment.curlTextProcessing(''.join(Lyrics))

			j = [str(i) for i in l]

			k = ' '.join(j)

			print Title, k
			fr.write(Title + " " + k + '\n')
