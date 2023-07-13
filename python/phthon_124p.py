from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('login_124p.html')
@app.route('/login',methods = ['POST', 'GET'])
def login():
  if request.method == 'POST':
    if request.form['profName'] == 'WoongSup' :
      return redirect(url_for('success'))
    else:
      abort(401)
  else:
    return redirect(url_for('index'))

@app.route('/success')
def success():
  return 'You have logged in successfully'

if __name__ == '__main__':
  app.run(debug = True)
