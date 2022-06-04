from app import app
from flask import render_template

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template('admin/sign_up.html')

@app.route("/admin/profile")
def admin_profile():
    return "Admin profile"