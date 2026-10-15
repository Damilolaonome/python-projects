from flask import Flask, render_template, request
import smtplib
import requests


# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

API_URL = "https://api.npoint.io/43644ec4f0013682fc0d"

# Replace these with your own details
OWN_EMAIL = "Onome.umukoro2@gmail.com"
OWN_PASSWORD = "godsgeneral4real"


# --------------------------------------------------
# GET BLOG POSTS
# --------------------------------------------------

try:
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    posts = response.json()

except requests.exceptions.RequestException as error:
    print("Could not connect to the blog API.")
    print("Error:", error)
    posts = []


# --------------------------------------------------
# FLASK APP
# --------------------------------------------------

app = Flask(__name__)


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def get_all_posts():
    return render_template(
        "index.html",
        all_posts=posts
    )


# --------------------------------------------------
# INDIVIDUAL BLOG POST
# --------------------------------------------------

@app.route("/post/<int:index>")
def show_post(index):

    requested_post = None

    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
            break

    return render_template(
        "post.html",
        post=requested_post
    )


# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------

@app.route("/about")
def about():
    return render_template("about.html")


# --------------------------------------------------
# CONTACT PAGE
# --------------------------------------------------

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        send_email(
            name,
            email,
            phone,
            message
        )

        return render_template(
            "contact.html",
            msg_sent=True
        )

    return render_template(
        "contact.html",
        msg_sent=False
    )


# --------------------------------------------------
# SEND EMAIL
# --------------------------------------------------

def send_email(name, email, phone, message):

    email_message = f"""Subject: New Message From Your Blog

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
"""

    try:

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:

            connection.starttls()

            connection.login(
                OWN_EMAIL,
                OWN_PASSWORD
            )

            connection.sendmail(
                OWN_EMAIL,
                OWN_EMAIL,
                email_message
            )

        print("Email sent successfully!")

    except Exception as error:

        print("Email could not be sent.")
        print("Error:", error)


# --------------------------------------------------
# RUN FLASK APP
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)