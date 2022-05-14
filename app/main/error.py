from flask import render_template, request
from . import main
from .. import db
from ..models import Subscribers
from ..email import welcome_message, notification_message

@main.app_errorhandler(404)
def notfound(error):
    """
    Function to render the 404 error page
    """
    if request.method == "POST":
        new_sub = Subscribers(email = request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
        welcome_message("Thank you for subscribing to lynne blog", 
                        "email/welcome", new_sub.email)
    return render_template("error.html"),404