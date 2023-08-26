from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

url_mapping = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return render_template('index.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_mapping:
        long_url = url_mapping[short_url]
        return redirect(long_url)
    else:
        return "Short URL not found."

if __name__ == '__main__':
    app.run(debug=True)