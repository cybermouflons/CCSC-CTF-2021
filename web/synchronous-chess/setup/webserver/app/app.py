#!/usr/bin/env python3

import os
import sqlite3
from flask import Flask, make_response, request, session, redirect, url_for, render_template
from flask_talisman import Talisman

# Config app
_cwd = os.path.dirname(os.path.abspath(__file__))

# Initialize app
app = Flask(__name__)
app.secret_key = "xl3]0+;EbPF#H``9CZ?*[}TRELLAOEOEOEOEOE{3JSxzCmp7#0>"

SELF = "'self'"
csp = {
    'default-src': SELF,
    'script-src': SELF,
    'img-src': SELF,
    'object-src': '\'none\'',
}
talisman = Talisman(
    app,
    frame_options='DENY',
    force_https=False,
    content_security_policy=csp,
    content_security_policy_nonce_in=['script-src']
)


# Index Page
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    ipAddr = request.remote_addr
    ua = request.headers.get('User-Agent')
    return render_template('404.html', userAgent=ua), 404


# Login Page
@app.route('/login', methods=['POST'])
def login():
    # Get Params from request
    username = request.form.get('username')
    password = request.form.get('password')

    # Connect to db
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Set parameters for query
    params = (username, password)
    # Execute query
    c.execute('''SELECT * from users WHERE username=? AND password=?''', params)
    result = c.fetchall()
    conn.commit()
    conn.close()

    if result:
        session['username'] = username
        return redirect(url_for('admin'))
    else:
        return render_template('index.html', errorMessage="Invalid Username and / or Password")


@app.route('/admin', methods=['GET'])
def admin():
    if request.headers.getlist("1438d1266a964a60f057e77b4f8cc4a7"):
        ip_address = request.headers.getlist("1438d1266a964a60f057e77b4f8cc4a7")[0]
    else:
        ip_address = request.remote_addr

    if (ip_address == "172.16.4.1"):
        return render_template('admin.html')
    else:
        return "You are not allowed to access this resource. Protected by IP Access Controls."


@app.before_request
def before_request():
    """
    Sets the "wsgi.input_terminated" environment flag, thus enabling
    Werkzeug to pass chunked requests as streams; this makes the API
    compliant with the HTTP/1.1 standard.  The gunicorn server should set
    the flag, but this feature has not been implemented.
    """
    request.environ["wsgi.input_terminated"] = True


@app.after_request
def after_request(response):
    response.headers.add('Cache-Control', 'no-cache')
    response.headers.add('Cache-Control', 'no-store')
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
