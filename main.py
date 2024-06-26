from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True 

@app.route("/")
def hello_world():
    return "<p>Hello, I'm trying the Flask GitHub Actions with heroku CI!</p>"

if __name__ == "__main__":
    app.run(debug=True)
