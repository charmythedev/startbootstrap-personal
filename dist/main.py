from datetime import datetime
from flask import Flask, abort, render_template, redirect, url_for, flash, request
import requests


# App initialization
current_year = datetime.now().year
app = Flask(__name__)


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
    pass

@app.route("/resume")
def resume():
    return render_template("resume.html", current_year=current_year)














if __name__ == "__main__":
    app.run(debug=True, port=5002)