#!/usr/bin/python
#easy_install pyechonest and also get the Echo-print codegen to over-ride binaries
import sys
import os

import pyechonest.config as config
import pyechonest.song as song

config.CODEGEN_BINARY_OVERRIDE = os.path.abspath("../echoprint-codegen")

# Put your API key in a shell variable ECHO_NEST_API_KEY, or put it here
config.ECHO_NEST_API_KEY='DSQRMLEGPIFC1XRWN'

def lookup(file):
    # song.identify reads  the first 30 seconds of the file
    fp = song.util.codegen(file)
    if len(fp) and "code" in fp[0]:
        # The version parameter to song/identify indicates the use of echoprint
        result = song.identify(query_obj=fp, version="4.11")
        print "Got result:", result
        if len(result):
            print "Artist: %s (%s)" % (result[0].artist_name, result[0].artist_id)
            print "Song: %s (%s)" % (result[0].title, result[0].id)
        else:
            print "No match. This track may not be in the database yet."
    else:
        print "Couldn't decode", file
from flask import Flask,request,redirect,url_for 
from werkzeug import secure_filename
UPLOAD_FOLDER='./'
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'png', 'jpg', 'jpeg', 'gif'])
app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
	file.save(os.path.join('./',secure_filename(file.filename)))
        return redirect('/lookup_music')
        
		
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
   
            

'''if __name__ == "__main__":
    if len(sys.argv) < 2:
        print >>sys.stderr, "Usage: %s <audio file>" % sys.argv[0]
        sys.exit(1)
    lookup(sys.argv[1])'''
@app.route('/lookup_music')
def lookup_music():
	lookup('file.mp3')
    

if __name__ == "__main__":
	app.run()

