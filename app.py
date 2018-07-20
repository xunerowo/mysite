from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/contact')
def contact():
	return render_template('contact.html')
@app.route('/folder')
def folder():
	return render_template('folder.html')
@app.route('/music')
def music():
	return render_template('music.html')
@app.route('/about')
def about():
	return render_template('about.html')
if __name__ == '__main__':
	app.run(debug=True)
