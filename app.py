from flask import Flask 
app = Flask(__name__)

@app.route('/')
def home ():
    return " HI  from talia Welcome to the CI/CD Project!"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)