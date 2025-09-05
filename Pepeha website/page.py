from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    with open('homepage.html') as f:
        return f.read()

# Login form page (GET)
@app.route('/login', methods=['GET'])
def login_form():
    return '''
    <form action="/login" method="post">
        Username: <input name="uname"><br>
        Password: <input name="psw" type="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

# Login processing (POST)
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('uname')
    password = request.form.get('psw')

    if username == 'admin' and password == 'password123':
        return f"Welcome {username}!"
    else:
        return "Login Failed! Try again."

if __name__ == '__main__':
    app.run(debug=True)
