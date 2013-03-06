from flask import Flask,render_template,request,redirect
from art import hangman
from game import *
app = Flask(__name__)

app.vars = {}

@app.route('/index',methods=['GET','POST'])
def welcome():
  if request.method == 'GET':
    return render_template('index.html', art = hangman[-1], methods=['GET','POST'])
  else:
    return redirect('/start')

@app.route('/start',methods=['GET','POST'])
def start():
  if request.method == 'POST':
    secretWord = getSecretWord()
    return render_template('start.html', art = hangman[0], length = len(secretWord), numguesses = guessesLeft, methods=['GET','POST'])
  else:
    app.vars['lettersGuessed'] = request.form['guess']
    return redirect('/main')

@app.route('/main')
def gameOn():
    if guessesLeft==0:
      return render_template('end.html')
    return redirect('/guess')

@app.route('/guess',methods=['GET','POST'])
def play():
  return render_template('guess.html', art = hangman[-guessesLeft], numguesses = guessesLeft, methods=['GET','POST'])

if __name__ == "__main__":
    app.run(debug=True)
