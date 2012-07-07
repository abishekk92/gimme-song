from operator import itemgetter

def calc(title):

	f = open("values", "r")

	val1 = []

	k = []

	for line in f:
		a = line.split()

		Title = ' '.join(a[:-3])

		if Title == title:

			val3 = a[-3:]

			val1 = [float(i) for i in val3]

			break

	ans = []

	for line in f:
		a = line.split()

		Title = ' '.join(a[:-3])

		val4 = a[-3:]

		val = [float(i) for i in val4]


		if Title != title:
	
			dis = pow(pow(val[0] - val1[0], 2) + pow(val[1] - val1[1], 2) + pow(val[2] - val1[2], 2), 0.5)

			ans.append([Title, dis])

	sorted(ans, key=itemgetter(1))

	for i in xrange(5):
		print ans[i]

	return ans

#if __name__ == "__main__":

	#calc("Enter Sandman Lyrics - Metallica")
