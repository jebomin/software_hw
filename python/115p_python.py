from flask import Flask, render_template, request, make_response
app = Flask(__name__)
@app.route('/')
def homepage():
  return render_template('115p_homepage.html')

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
  if request.method == 'POST':
    user = request.form['username']
    resp = make_response(render_template('115p_readcookie.html'))
    resp.set_cookie('userName',user)
    return resp 

@app.route('/getcookie')
def getcookie():
  name = request.cookies.get('userName')
  return '<h1>welcome '+name+'!</h1>'
if __name__ == '__main__':
  app.run(debug=True)
