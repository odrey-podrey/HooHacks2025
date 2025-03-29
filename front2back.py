from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    link = request.form.get('link')
    artist = source_image(link)
    print(link)
    print(artist)

    return Response(artist, status = 200, mimetype ="text/html")

if __name__ == '__main__':
    app.run()