from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/dongguk')
def hello_dongguk():
  return 'Hello Dongguk University!_2020112084제보민'

@app.route('/student/<stdName>')
def hello_student(stdName):
  return 'Hello %s!_2020112084제보민' % stdName
@app.route('/user/<userName>')
def hello_user(userName):
  if userName =='dongguk':
    return redirect(url_for('hello_dongguk'))
  else:
    return redirect(url_for('hello_student',stdName = userName))
if __name__ == '__main__':
  app.run(debug = True)