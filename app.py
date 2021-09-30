from flask import Flask,render_template,redirect, url_for, request
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "I am running a Hello from flask application!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/institute')
def institute():
    return render_template('Institutions.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/twitter')
def twitter():
    return render_template('twitter.html')

@app.route('/facebook')
def facebook():
    return render_template('facebook.html')

@app.route('/instagram')
def instagram():
    return render_template('instagram.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/testimony')
def testimony():
    return render_template('testimony.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)