from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      # return 'file uploaded successfully'
      return render_template('index.html')   # list files, delete files , and most importantly, do traning and generating new music!
		
if __name__ == '__main__':
   app.run(debug = True)


   