import web
import dis

urls = (
	'/', 'ini',
)

class ini:
	def PUT(self):

		ans = []

		title = web.input()

		ans = dis.calc(title)

		web.output("Heckles!")

		return ans

if __name__ == '__main__':
	app = web.application(urls, globals())

	app.run()
