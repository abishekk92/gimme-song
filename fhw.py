import dis

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route('/song/<songtitle>')
def return_sentiment(songtitle):
	ans = dis.calc(songtitle)
	print ans
	return 'Sentiment is %s' % (ans)

if __name__ == "__main__":
	app.run()
