from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


if __name__ == '__main__':
    app.run(debug=True)
