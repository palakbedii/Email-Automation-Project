from flask import Flask, render_template, redirect, request
from templates_data import email_templates as templates_list

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/email_templates")
def email_templates():

    return render_template(
        "email_templates.html",
        templates=templates_list
    )


@app.route("/compose")
def compose():
    return render_template("compose.html",
        templates=templates_list
    )


@app.route("/scheduled")
def scheduled():
    return render_template("scheduled.html")


@app.route("/sent")
def sent():
    return render_template("sent.html")


@app.route("/failed")
def failed():
    return render_template("failed.html")


@app.route("/calendar")
def calendar():
    return render_template("calendar.html")


@app.route("/smtp_settings", methods=["GET", "POST"])
def smtp_settings():

    if request.method == "POST":

        smtp_host = request.form["smtp_host"]        # Save into database here
        smtp_port = request.form["smtp_port"]
        sender_email = request.form["sender_email"]
        app_password = request.form["app_password"]

    return render_template("smtp_settings.html")

@app.route("/logout")
def logout():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)