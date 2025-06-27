from flask import Flask  #For web app and web hooks
app = Flask(__name__)

@app.route('/')
def home():
    return "Testing for Jenkins Project - Muhammad Karim's"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
