from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)

# For local MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
portfoli=db['varsha']


@app.route('/',methods=['GET','POST'])
def home():
    
    return render_template("text.html")

if __name__ == "__main__":
    app.run(debug=True,port=5001)
