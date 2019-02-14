from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import os
#for getting the file list:
import glob
types1 = ('*.pdf', '*.py','*.mp3') # the tuple of file types 
types2 =('*.mp3',)
#https://stackabuse.com/python-list-files-in-a-directory/

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static"



@app.route('/')
def index():
   return render_template('index.html')

# @app.route('/upload')
# def upload():
#    return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      # f.save(secure_filename(f.filename))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      print('file uploaded successfully')
   
      
      files_grabbed1 = []
      for files in types1:
         files_grabbed1.extend(glob.glob(files))
      files_grabbed1 
      print("files_grabbed1=",files_grabbed1)  

      files_grabbed2 = []
      for files in types2:
         files_grabbed2.extend(glob.glob("./static/"+files))
      files_grabbed2=[file.split('/')[-1] for file in files_grabbed2]
      print("files_grabbed2=",files_grabbed2) 

      return render_template('index.html', x1=files_grabbed1,x2=files_grabbed2)   # list files, delete files , and most importantly, do traning and generating new music!
		
if __name__ == '__main__':
   app.run(debug = True)

