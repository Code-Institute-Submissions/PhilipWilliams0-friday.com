import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_projects")
def get_projects():
    projects = list(mongo.db.projects.find())
    return render_template("projects.html", projects=projects)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    projects = list(mongo.db.projects.find({"$text": {"$search": query}}))
    return render_template("projects.html", projects=projects)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    projects = list(mongo.db.projects.find(
        {"created_by": session["user"]}))
    return render_template("profile.html", username=username, projects=projects)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        project = {
            "category_name": request.form.get("category_name"),
            "status_name": request.form.get("status_name"),
            "project_name": request.form.get("project_name"),
            "project_description": request.form.get("project_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.projects.insert_one(project)
        flash("Project Successfully Added")
        return redirect(url_for("get_projects"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    statuses = mongo.db.status.find().sort("status_name", 1)
    return render_template("add_project.html", categories=categories, statuses=statuses)


@app.route("/edit_project/<project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "status_name": request.form.get("status_name"),
            "project_name": request.form.get("project_name"),
            "project_description": request.form.get("project_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.projects.update({"_id": ObjectId(project_id)}, submit)
        flash("Project Successfully Updated")

    project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    statuses = mongo.db.status.find().sort("status_name", 1)
    return render_template("edit_project.html", project=project, categories=categories, statuses=statuses)


@app.route("/delete_project/<project_id>")
def delete_project(project_id):
    mongo.db.projects.remove({"_id": ObjectId(project_id)})
    flash("Project Successfully Deleted")
    return redirect(url_for("get_projects"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# error handlers
@app.errorhandler(404)
def not_found(e):
    return render_template("error_handlers/404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("error_handlers/500.html"), 500


@app.errorhandler(403)
def forbidden(e):
    return render_template("error_handlers/403.html"), 403


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
