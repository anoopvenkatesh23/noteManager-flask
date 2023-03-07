from flask import *
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
import pymongo
import os
from dotenv import load_dotenv



# loading environment from .env file

app_path = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(app_path, '.env')
load_dotenv(dotenv_path)


app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")
Bootstrap(app)
mongo = PyMongo(app)



@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        allNotes = mongo.db.notes.find()
        return render_template('home.html', notes = allNotes)
    elif request.method == "POST":
        note = request.form['note_text']
        print(note)
        mongo.db.notes.insert_one({'note' : note})
        return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)

