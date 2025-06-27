from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

USER_CRENDENTIALS = {
    'username': 'admin',
    'password': '1234'
}

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == USER_CRENDENTIALS['username'] and password == USER_CRENDENTIALS['password']:
            session['user'] = username
            flash('Login successful', "success")
            return redirect(url_for('tasks.view_tasks'))  # ✅ FIXED HERE
        else:
            flash("Invalid username or password", "danger")
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out', 'info')
    return redirect(url_for('auth.login'))
