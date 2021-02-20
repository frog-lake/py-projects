"""
practice flask web application using materials from https://runestone.academy/runestone/books/published/thinkcspy/index.html
"""
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    # if name in args, else world
    name = request.args.get('name', 'world')
    return hello_html.format(name)

hello_html = """<html><body>
        <h1>Hello {0} :]</h1>
        The time is <a href="/time">here</a>
        </body></html>"""


@app.route('/time')
def time():
    return time_html.format(datetime.now())
    
time_html = """<html><body>
        the time is {0}
    </html></body>
    """

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
