#dice rolling simulation 


import random as ra 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   num = round(ra.random() *10 )
   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


# 
# print(num)