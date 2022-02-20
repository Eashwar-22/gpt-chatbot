from flask import Flask,render_template

app = Flask(__name__)
# app.config['SECRET_KEY']='tsadw3hwewfwo9e0203e'

@app.route('/')
def home_page():
    return render_template('home.html')


if __name__=='__main__':
    app.run(debug=True)