"""Newsroom: authors write articles, editors review and publish them, readers see the result."""
import os

from flask import Flask, abort, flash, redirect, render_template, request, send_from_directory, session, url_for

import db
import storage
from auth import current_user, require_role

app = Flask(__name__)
app.secret_key = os.environ.get("NEWSROOM_SECRET", "dev")
COVER_REQUIRED = os.environ.get("NEWSROOM_COVER_REQUIRED", "1")


# ---------------------------------------------------------------- readers

@app.route("/")
def home():
    """Front page: the published articles."""
    return render_template("home.html", articles=db.published_articles())


@app.route("/articles/<int:article_id>")
def article(article_id):
    row = db.get_article(article_id)
    if row is None or row["status"] != "published":
        abort(404)
    return render_template("article.html", article=row)


@app.route("/uploads/<path:name>")
def uploaded(name):
    return send_from_directory(storage.UPLOAD_DIR, name)


@app.route("/published.csv")
def published_list():
    return send_from_directory(storage.EXPORT_DIR, "published.csv")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = db.find_user(request.form["email"])
        if user is None:
            flash("Unknown e-mail address")
            return redirect(url_for("login"))
        session["user_id"] = user["id"]
        return redirect(url_for("home"))
    return render_template("login.html")


# ---------------------------------------------------------------- authors

@app.route("/desk")
@require_role("author")
def desk():
    return render_template("desk.html", articles=db.articles_of(current_user()["id"]))


@app.route("/desk/new", methods=["GET", "POST"])
@require_role("author")
def new_article():
    if request.method == "POST":
        cover = request.files.get("cover")
        cover_name = storage.save_upload(cover) if cover else None
        db.create_article(current_user()["id"], request.form["title"], request.form["body"], cover_name)
        flash("Draft saved")
        return redirect(url_for("desk"))
    return render_template("edit.html")


@app.route("/desk/<int:article_id>/submit", methods=["POST"])
@require_role("author")
def submit(article_id):
    row = db.get_article(article_id)
    if row["status"] != "draft":
        flash("Only a draft can be sent for review")
        return redirect(url_for("desk"))
    db.send_for_review(article_id)
    flash("Sent to the editors")
    return redirect(url_for("desk"))


# ---------------------------------------------------------------- editors

@app.route("/review")
@require_role("editor")
def review_queue():
    return render_template("review.html", articles=db.waiting_for_review())


@app.route("/review/<int:article_id>")
@require_role("editor")
def review_detail(article_id):
    return render_template("review_detail.html", article=db.get_article(article_id))


@app.route("/review/<int:article_id>/publish", methods=["POST"])
@require_role("editor")
def publish(article_id):
    row = db.get_article(article_id)
    if row["status"] != "in_review":
        flash("Only an article in review can be published")
        return redirect(url_for("review_queue"))
    if COVER_REQUIRED == "1" and not row["cover"]:
        flash("Add a cover image before publishing")
        return redirect(url_for("review_detail", article_id=article_id))
    db.publish_article(article_id)
    storage.write_published_list(db.published_articles())
    return redirect(url_for("review_queue"))


@app.route("/review/<int:article_id>/return", methods=["POST"])
@require_role("editor")
def send_back(article_id):
    db.return_to_author(article_id, request.form["reason"])
    return redirect(url_for("review_queue"))


# ---------------------------------------------------------------- authors and editors

@app.route("/preview/<int:article_id>")
@require_role("author", "editor")
def preview(article_id):
    return render_template("article.html", article=db.get_article(article_id))


if __name__ == "__main__":
    app.run(port=int(os.environ.get("NEWSROOM_PORT", "5080")))
