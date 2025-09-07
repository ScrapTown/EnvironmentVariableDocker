from flask import Flask,render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    epath=os.environ.get("epath")
    fpd=os.environ.get("fpd")
    return render_template("index.html",epath=epath,fpd=fpd)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)