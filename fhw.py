import dis
import json

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route('/song/<songtitle>')
def return_sentiment(songtitle):
	ans = dis.calc(songtitle)
	k = dict(ans)
	#print json.dumps(k)
	return '%s' % (json.dumps(k))

if __name__ == "__main__":
	app.run()
