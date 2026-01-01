from datetime import datetime
from flask import Flask, abort, render_template, redirect, url_for, flash, request
import requests
import json
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv


import os

# DELETE THIS LINE AFTER TESTING
load_dotenv()
GOOGLE_PASSWORD = os.getenv("GOOGLE_PASSWORD")


# App initialization
current_year = datetime.now().year
app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET")



# Example project data
response = requests.get("https://api.npoint.io/2d62bbc55683f8cfc99e")
response.raise_for_status()
projects = response.json()




# ROUTES
@app.route("/")
def index():
    github_url = "https://github.com/charmythedev"
    return render_template("index.html", current_year=current_year, github_url=github_url)

@app.route("/projects")
def show_projects():
    return render_template("projects.html", current_year=current_year, projects =projects)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        full_message = f"""
        New contact form submission:

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        msg = MIMEText(full_message)
        msg["Subject"] = "New Contact Form Submission"
        msg["From"] = email
        msg["To"] = "charmythedev@gmail.com"

        # Gmail SMTP
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("charmythedev@gmail.com", GOOGLE_PASSWORD)
            server.send_message(msg)

        return render_template("contact_success.html")

    return render_template("contact.html")

@app.route("/resume")
def resume():
    with open("dist/static/assets/resume.json", "r") as f:
        resume_json = json.load(f)
    return render_template("resume.html", current_year=current_year, resume_json=resume_json)














if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=False, port=5000)