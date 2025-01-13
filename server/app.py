#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Flask has to parse "string" and "username" from the route. How can you use Python to remove brackets and get parameters out of a string?
# str methods or the re module.
# With str methods:
# url = '/<string:username>'
# url = url.replace('/<', '')
# url = url.replace('>', '')
# type, parameter = url.split(':')
# With re:
# exp = re.compile('[A-z]+')
# type, parameter = exp.findall(url)
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

