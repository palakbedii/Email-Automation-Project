from flask import Flask, render_template, redirect, request, flash, url_for
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
import requests

app = Flask(__name__)
app.secret_key = "email_automation_project"


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/email_templates")
def email_templates():

    keyword = request.args.get("keyword")

    if keyword:

        response = requests.get(
            "http://127.0.0.1:8000/templates/search",
            params={"keyword": keyword}
        )

    else:

        response = requests.get(
            "http://127.0.0.1:8000/templates"
        )

    templates = response.json()

    return render_template(
        "email_templates.html",
        templates=templates,
        keyword=keyword
    )

@app.route("/new_template", methods=["GET", "POST"])
def new_template():

    if request.method == "POST":

        print("FORM SUBMITTED")
        print(request.form)

        data = {
        "name": request.form["name"],
        "subject": request.form["subject"],
        "body": request.form["body"],
        "last_edited": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        print(data)
        
        response = requests.post(
            "http://127.0.0.1:8000/templates",
            json=data
        )
        
        print("Status Code:", response.status_code)
        print("Response:", response.text)

        if response.status_code == 200:

            flash(
                "Template created successfully!",
                "success"
            )

            return redirect(url_for("email_templates"))

        flash(
            "Unable to save template.",
            "danger"
        )

        return redirect(url_for("new_template"))

    return render_template("new_template.html")


@app.route("/edit_template/<int:id>", methods=["GET", "POST"])
def edit_template(id):

    if request.method == "POST":

        data = {
            "name": request.form["name"],
            "subject": request.form["subject"],
            "body": request.form["body"],
            "last_edited": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        response = requests.put(
            f"http://127.0.0.1:8000/templates/{id}",
            json=data
        )

        if response.status_code == 200:

            flash(
                "Template updated successfully!",
                "success"
            )

            return redirect(url_for("email_templates"))

        flash(
            "Unable to update template.",
            "danger"
        )

        return redirect(url_for("edit_template", id=id))

    response = requests.get(
        f"http://127.0.0.1:8000/templates/{id}"
    )

    template = response.json()

    return render_template(
        "edit_template.html",
        template=template
    )


@app.route("/delete_template/<int:id>")
def delete_template(id):

    response = requests.delete(
        f"http://127.0.0.1:8000/templates/{id}"
    )

    if response.status_code == 200:

        flash(
            "Template deleted successfully!",
            "success"
        )

    else:

        flash(
            "Unable to delete template.",
            "danger"
        )

    return redirect(url_for("email_templates"))


@app.route("/send_now", methods=["POST"])
def send_now():

    recipient = request.form["recipient"].strip()
    subject = request.form["subject"].strip()
    message = request.form["message"].strip()

    # 1. Check recipient empty
    if not recipient:
        flash(
            "Recipient email is required.",
            "danger"
        )
        return redirect(url_for("compose"))

    # 2. Check email format
    try:
        validate_email(recipient)

    except EmailNotValidError:
        flash(
            "Please enter a valid email address.",
            "danger"
        )
        return redirect(url_for("compose"))

    # 3. Check subject
    if not subject:
        flash(
            "Subject cannot be empty.",
            "danger"
        )
        return redirect(url_for("compose"))

    # 4. Check message
    if not message:
        flash(
            "Message cannot be empty.",
            "danger"
        )
        return redirect(url_for("compose"))

    # Only after validation:
    data = {
        "recipient": recipient,
        "subject": subject,
        "message": message,
    }

    response = requests.post(
        "http://127.0.0.1:8000/emails/send_now",
        json=data
    )

    result = response.json()

    if response.status_code == 200:

        flash(
            result.get("message", "Email Sent Successfully!"),
            "success"
        )

    else:

        flash(
            result.get("detail", "Unable to send email."),
            "danger"
        )

    return redirect(url_for("compose"))

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

    template_id = request.args.get("template_id")
    selected_template = None

    if template_id:

        response = requests.get(
            f"http://127.0.0.1:8000/templates/{template_id}"
        )

        selected_template = response.json()

    response = requests.get("http://127.0.0.1:8000/templates")
    templates = response.json()

    return render_template(
        "compose.html",
        templates=templates,
        selected_template=selected_template
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