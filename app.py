from flask import Flask, render_template, request, redirect, url_for,flash
from werkzeug import secure_filename
import os
#for getting the file list:
import glob
types1 = ('*.pdf', '*.py','*.mp3') # the tuple of file types 
types2 =('*.mp3','*.mid','*.pdf', '*.py',"*.wav")

our_list=['StarWars100.mp3', 'StarWars25000.mp3', 'StarWarsOriginal.mp3', \
    'GuitarSolo100.mp3', "GuitarSolo25000.mp3", "GuitarSoloOriginal2.mp3",\
       'TwoFountainsOriginal.mp3', 'TwoFountains100.mp3','TwoFountains25000.mp3']
#https://stackabuse.com/python-list-files-in-a-directory/

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static"

import multiprocessing

bind = "127.0.0.1:5000"
workers = multiprocessing.cpu_count() * 2 + 1

@app.route('/')
def index():

      # files_grabbed1 = []
      # for files in types1:
      #    files_grabbed1.extend(glob.glob(files))
      # files_grabbed1 
      # print("files_grabbed1=",files_grabbed1)  
      
      files_grabbed2 = []
      for files in types2:
         files_grabbed2.extend(glob.glob(app.config['UPLOAD_FOLDER'] +'/'+files))
      files_grabbed2=[file.split('/')[-1] for file in files_grabbed2]
      files_grabbed2=list(set(files_grabbed2)-set(our_list))
      print("files_grabbed2=",files_grabbed2) 
      files_size=[round(os.stat(os.path.join(app.config['UPLOAD_FOLDER'],file2)).st_size/(1000*1000.0),2) for file2 in  files_grabbed2]
      
      files_grabbed2_dict=[]
      for i,file2 in enumerate(files_grabbed2):
         ss=dict();ss[file2]=files_size[i]
         files_grabbed2_dict.append(ss)
       

      # return render_template('index.html', x1=files_grabbed1,x2=files_grabbed2)   # list files, delete files , and most importantly, do traning and generating new music!
		# return render_template('index.html', x2=files_grabbed2) 
      return render_template('index.html',x2=files_grabbed2_dict)


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      # f.save(secure_filename(f.filename))
      file_path=os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
      # print("file_path=",file_path,"%%%%%%%%%%%%")
      f.save(file_path)
      file_size=os.stat(file_path).st_size
      print('the file size is',file_size)
   
      if file_size/(1000*1000.0)>10:
         os.remove(file_path)
         sentence="this file is larger than 10M, please choose a smaller one!!"
         return render_template('index.html',file_message=sentence)  
      elif len([name for name in os.listdir(app.config['UPLOAD_FOLDER'])])>15:
            os.remove(file_path)
            sentence="the number of your uploaded files is exceeding max=6, please delete some!!"
            return render_template('index.html',file_message=sentence)  
      else:
               #f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
               print('file uploaded successfully')
  
   
      
      # files_grabbed1 = []
      # for files in types1:
      #    files_grabbed1.extend(glob.glob(files))
      # files_grabbed1 
      # print("files_grabbed1=",files_grabbed1)  

      # files_grabbed2 = []
      # for files in types2:
      #    files_grabbed2.extend(glob.glob("./static/"+files))
      # files_grabbed2=[file.split('/')[-1] for file in files_grabbed2]
      # files_grabbed2=list(set(files_grabbed2)-set(our_list))
      # print("files_grabbed2=",files_grabbed2) 

      # return render_template('index.html', x1=files_grabbed1,x2=files_grabbed2)   # list files, delete files , and most importantly, do traning and generating new music!
		# return redirect("/", code=302)
      return redirect("/")                      
   return None

# @app.route("/generated/lookback")
# def generated():
#    subprocess.call("./generate_lookback.sh", shell=True)



#    return render_template('index.html')




# @app.route('/train', methods = ['GET', 'POST'])
# def train_file():     
#    if request.method == 'POST':

#      return render_template('index.html', x1=files_grabbed1,x2=files_grabbed2)   # list files, delete files , and most importantly, do traning and generating new music!


if __name__ == '__main__':
   app.run(debug = True)
 




# melody_rnn_create_dataset \
# --config='basic_rnn' \
# --input=/tmp/notesequences.tfrecord \
# --output_dir=/tmp/melody_rnn/sequence_examples \
# --eval_ratio=0.10


# melody_rnn_train \
# --config='basic_rnn' \
# --run_dir=/tmp/melody_rnn/logdir/run1 \
# --sequence_example_file=/tmp/melody_rnn/sequence_examples/training_melodies.tfrecord \
# --hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
# --num_training_steps=20000