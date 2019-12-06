import flask
from flask import Flask, render_template, request,send_file
import os
from werkzeug import secure_filename
from photoOutput import photo
from pdftoimg import pdftoimage
app = flask.Flask(__name__)

results=[  'arch.jpg','blockchain.jpg','book.png','database.png','arch.jpg' ,'output.png'] #has the file names
@app.route("/")
def home():
    return flask.render_template("home.html",results=results)

@app.route("/upload")
def upload():
    return flask.render_template("upload.html")

@app.route("/view")
def view():
    return flask.render_template("view.html",results=results)

@app.route("/download")
def download():
    path = "report.pdf"
    return send_file(path, as_attachment=True)
def parser():#run the parser here
    pass

def pdfimg(path):
    pdftoimage(path)
    pass
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      parser()
    #   obj=photo()     Sample calls to generate
    #   obj.generateImage()
    #   results.append('output.png')
      return 'file uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True)
