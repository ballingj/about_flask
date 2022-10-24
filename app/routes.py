from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'


@app.route('/html')
def _html():
    user = {'username': 'Jeff'}
    return '''
<html>
    <head>
        <title>Home - Microapp</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''</h1>
    </body>
</html>'''

# localhost:5000/user/Jeff
# output: Hello Jeff
''' Filters for Jinja
    safe
    capitalize
    lower
    upper
    title
    trim
    striptags
'''
@app.route('/user/<name>')
def user(name):
    # return f'<h1>Hello {name}</h1>'
    return render_template('01-user.html', name=name)

@app.route('/template')
def _template():
    user = {'username': 'Jeff'}
    return render_template('01-template.html', title='Home', user=user)


@app.route('/conditional')
def _conditional():
    user = {'username': 'Jeff'}
    return render_template('02-conditional.html', title='Microapp', user=user)


@app.route('/forloop')
def _forloop():
    user = {'username': 'Jeff'}
    posts = [
        {
            'author': {'username': 'Jeff'},
            'body': 'Beautiful day in Omaha!'
        },
        {
            'author': {'username': 'Cris'},
            'body': 'Work sucks!'
        }
    ]
    return render_template('03-forloop.html', title='Microapp', user=user, posts=posts)

# Start of template inheritance
@app.route('/temp_inherit')
def temp_inherit():
    user = {'username': 'Jeff'}
    posts = [
        {
            'author': {'username': 'Jeff'},
            'body': 'Beautiful day in Omaha!'
        },
        {
            'author': {'username': 'Cris'},
            'body': 'Work sucks!'
        }
    ]
    return render_template('04-tmpl_inheritance.html', title='Microapp', user=user, posts=posts)

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('05-login.html', title='Sign-In', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # flash('Login requested for user {}: {}, remember_me={}'.format(
        #     form.username.data, form.usermode.data, form.remember_me.data))
        # the flash() function is useful way to display a message;
        # must be used with get_flashed_messages() function
        flash(f'Login requested for user {form.username.data} - usermode {form.usermode.data}, \
                remember_me={form.remember_me.data}')
        # the redirect() function is used to redirect to a new page
        return redirect(url_for('temp_inherit'))
    return render_template('05-login.html', title='Sign-In', form=form)


# Create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Server Error
@app.errorhandler(500)
def something_wrong(e):
    return render_template('500.html'), 500
