from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        return 'Welcome to Python Flask World automate trigger 2'

if __name__ =='__main__':
        app.run(host='0.0.0.0', port=8080)
