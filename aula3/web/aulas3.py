from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index():
    return 'hello world'


@app.route('/login')
def get_login():
    return render_template('index.html')

if __name__  == "__main__":
     app.run(host='0.0.0.0', port=5000, debug=true)