import os #build file paths
import cv2
import pytesseract
from flask import Flask, render_template , request

from Main import extracted_text

app = Flask(__name__) #creates an instance of flask application
UPLOAD_FOLDER = os.path.join("static","uploads") #sets the target directory path uploaded images will be stored depending on the os (yk cause python is goated)

@app.route("/",methods=["GET","POST"]) #maps the root url to the function immediately beneath it(flask convention? -mechanism)

def home():
    text_result = ""

    if request.method == "POST":
        file = request.files["image"] #
        if file and file.filename !="":
            save_path = os.path.join(UPLOAD_FOLDER,file.filename)
            file.save(save_path)

            image = cv2.imread(save_path)
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            text_result = pytesseract.image_to_string(gray)


    return render_template("index.html",extracted_text = text_result) #flask render_template looks for adjacent files on the same directory containing the templates folder

if __name__ == "__main__":
    app.run(debug=True)