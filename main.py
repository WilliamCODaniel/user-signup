from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('user-form.html', title="usersignup")

@app.route('/user', methods=['POST', 'GET'])
def display_user_form():
    username = request.form['user']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']

    user_error = ""
    pass_error = ""
    pass_error2 = ""
    email_error = ""
    special = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if not username:
        user_error = "No Username entered"
        username = ""
    elif len(username) < 3:
        user_error = """Username length must be more than 3 and less than
        20 characters"""
        username = username
    elif len(username) >20:
        user_error = """Username length must be more than 3 and less than
        20 characters"""
        username = username
    elif ' ' in username:
        user_error = "Username cannot contain spaces"
        username = username
    if not password:
        pass_error = "No Password entered"
        password = ""
    elif len(password) < 3:
        pass_error = """Password length must be more than 3 and less than
        20 characters"""
        password = ""
    elif len(password) > 20:
        pass_error = """Password length must be more than 3 and less than
        20 characters"""
        password = ""
    elif ' ' in password:
        pass_error = "Password cannot contain spaces"
        password = ""
    elif special.search(password)== None:
        pass_error = "Password must contain at least 1 Special character"
        password = ""
    else:
        dot = 0
        at = 0
        hasnumber = False
        for char in password:
            if char.isdigit():
                hasnumber = True
        if not hasnumber:
                pass_error = "Password must contain at least 1 number"
        for char in email:
            if char == '.':
                dot += 1
            if char == '@':
                at += 1
                if dot or at > 1:
                    email_error = "Must contain only one '.' and one '@'."
                    email = email
    if password != password2:
        pass_error2 = "Passwords do not match"
        password2 = ""
    if not email:
        email_error = ""
    elif len(email) < 3:
        email_error = """Email length must be more than 3 and less than
        20 characters"""
        email = email
    elif len(email) > 20:
        email_error = """Email length must be more than 3 and less than
        20 characters"""
        email = email
    elif ' ' in email:
        email_error = "Email cannot contain spaces"
        email = email
    elif ('.' or '@') not in email:
        email_error = "Not a valid email address"
        email = email

        


    
    if user_error or pass_error or pass_error2 or email_error:
        print (password, password2)
        return render_template ('user-form.html', title="usersignup", user_error=user_error,
        pass_error=pass_error, pass_error2=pass_error2, email_error=email_error,
        user=username, password=password, password2=password2, email=email)

    return render_template('thanks.html', title="Welcome", user=username)


app.run()
