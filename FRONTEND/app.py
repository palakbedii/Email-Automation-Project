from flask import Flask, render_template, redirect, request, flash, url_for
import requests

from templates_data import email_templates as templates_list

app = Flask(__name__)
app.secret_key = "email_automation_project"


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/email_templates")
def email_templates():

    return render_template(
        "email_templates.html",
        templates=templates_list
    )


@app.route("/compose", methods=["GET", "POST"])
def compose():

    if request.method == "POST":

        print("===== COMPOSE FORM SUBMITTED =====")
        print(request.form)

        data = {
            "recipient": request.form["recipient"],
            "subject": request.form["subject"],
            "message": request.form["message"],
            "date": request.form["date"],
            "time": request.form["time"]
        }

        response = requests.post(
            "http://127.0.0.1:8000/emails",
            json=data
        )

        print(response.status_code)
        print(response.text)

        if response.status_code == 200:

            flash(
                "Email Scheduled Successfully!",
                "success"
            )

        else:

            flash(
                "Unable to schedule email.",
                "danger"
            )

        return redirect(url_for("compose"))

    return render_template(
        "compose.html",
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

        smtp_host = request.form["smtp_host"]
        smtp_port = int(request.form["smtp_port"])
        sender_email = request.form["sender_email"]
        app_password = request.form["app_password"]

        data = {
            "smtp_host": smtp_host,
            "smtp_port": smtp_port,
            "sender_email": sender_email,
            "app_password": app_password
        }

        response = requests.post(
            "http://127.0.0.1:8000/smtp_settings",
            json=data
        )

        if response.status_code == 200:
            flash("SMTP Settings Saved Successfully", "success")
        else:
            flash("Unable to save SMTP Settings.", "danger")

        return redirect(url_for("smtp_settings"))

    response = requests.get(
        "http://127.0.0.1:8000/smtp_settings"
    )

    if response.status_code == 200:
        settings = response.json()
    else:
        settings = None

    return render_template(
        "smtp_settings.html",
        settings=settings
    )


@app.route("/logout")
def logout():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)