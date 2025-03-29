from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('frontEnd.html')

if __name__ == '__main__':
    app.run()