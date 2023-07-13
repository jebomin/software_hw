from flask import Flask, render_template
app = Flask(__name__)

@app.route('/score')
def score():
  dict = {'YeHyun':30,'JiYoung':70,'WoongSup':90}
  return render_template('score_hw1.html', result = dict)
if __name__ == '__main__':
  app.run(debug = True)