from flask import Flask, redirect, render_template, request
import string
import random

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'  # Replace with your server name or domain
urls = {}  # Dictionary to store the original and shortened URLs

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['url']
    short_code = generate_short_code()
    short_url = request.host_url + short_code
    urls[short_code] = long_url
    return render_template('result.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    if short_code in urls:
        long_url = urls[short_code]
        return redirect(long_url)
    else:
        return "Invalid URL"

def generate_short_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(6))
    return code

if __name__ == '__main__':
    app.run()
