from flask import Flask, request, render_template

app = Flask(__name__)


# http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    return "<h1>Hello World</h1>"


# http://127.0.0.1:5000/name
@app.route("/name")
def print_name():
    return "<h1>Dhimant Godhani</h1>"


# http://127.0.0.1:5000/sum
@app.route("/sum")
def add_number():
    a = request.args.get('a')
    b = request.args.get('b')
    c = int(a) + int(b)
    return "Sum : " + str(c)

# http://127.0.0.1:5000/welcome
@app.route('/welcome')
def welcome():
    return render_template('hello.html')  # Using render function from flask


# Using Jinja2 template for PATH parameter
# http://127.0.0.1:5000/welcome/Pritesh
@app.route('/welcome/<name>')
def welcome_name(name):
    return render_template('welcome.html', myname=name)  # Passing Parameter to template


@app.route('/user-data', methods=['POST'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        result = '''
                <h1>First Name : {}<h1>
                <h1>Last Name : {}<h1>
                '''
    return result.format(first_name, last_name)


@app.route('/user')
def user_form():
    return '''
    <form method="POST" action="http://127.0.0.1:5000/user-data">
        <div><label>First Name: <input type="text" name="first_name"></label></div>
        <div><label>Last Name: <input type="text" name="last_name"></label></div>
        <input type="submit" value="Submit">
    </form>
    '''


if __name__ == '__main__':
    app.run()
