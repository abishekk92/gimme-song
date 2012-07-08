from HTMLParser import HTMLParser

class HTMLParserHandler(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.titleflag = 0
		self.lydivflag = 0
		self.SongTitle = ""
		self.Lyrics = []


	def handle_starttag(self, tag, attrs):

		if tag == 'title':
			self.titleflag = 1

	
		if tag == 'div':
			for name, value in attrs:
				if name == 'id' and value == 'content_h':
					self.lydivflag = 1

		if tag == 'span':
			self.lydivflag = 0

	def handle_endtag(self, tag):
		if tag == 'div' and self.lydivflag == 1:
			self.lydivflag = 0



	def handle_data(self, data):
		if self.titleflag == 1:

			self.SongTitle = data

			self.titleflag = 0

		if self.lydivflag == 1:

			self.Lyrics.append(data)


	def getData(self):
		return self.SongTitle, self.Lyrics


#if __name__ == '__main__':

#	htmlparse = HTMLParserHandler()

#	file = open("in+the+light_20082112.html", "r")

#	inp = ' '.join(file.readlines())

#	htmlparse.feed(inp)

#	Title, Lyrics = htmlparse.getData()

#	print 'Title', Title, '\n', ''.join(Lyrics)
