"""
flask application with a ui interface using the materials provided in chapter 14 of https://runestone.academy/runestone/books/published/thinkcspy/index.html
this is app is written to be passive-aggressive/just plain aggressive
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return HOME_HTML


HOME_HTML = """
    <html><body>
        <h2>Hi. Hello. Hi.</h2>
            <form action="/greet">
                Your name. <input type='text' name='username'><br>
                Food? Yes or no. <input type='text' name='food'><br>
                <input type='submit' value='Continue'>
            </form>
        </body></html>"""


@app.route('/greet')
def greet():
    username = request.args.get('username', '')
    food = request.args.get('food', '')

    if username == '':
        name_msg = "you are as nameless as you are useless"
    else:
        name_msg = "hi " + username + " :]"

    # python doesn't have switch statements? cringe
    if food == '':
        msg = 'i hate you so much. contempt is flowing through my veins right now.'
    elif food.lower() == 'yes':
        msg = 'i like you :]'
    elif food.lower() == 'no':
        msg = 'you will shrivel away soon.'
    else:
        msg = 'you can\'t read?'

    return GREET_HTML.format(name_msg, msg)


GREET_HTML = """
    <html><body>
        <h2>{0}</h2>
        {1}
    </html></body>
    """


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
