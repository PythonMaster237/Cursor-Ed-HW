from datetime import datetime
import hashlib

from app import app, db
from flask import render_template, request, redirect, session, abort
from models import User, Post


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")


@app.route("/save-user", methods=["POST"])
def register():
    data = request.form
    password_hash = hashlib.sha256(data.get("password").encode("utf-8"))
    user = User(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        password=password_hash.hexdigest(),
    )
    db.session.add(user)
    db.session.commit()
    session["user"] = user.serialize
    return redirect("/")


@app.route("/sign-in")
def sign_in():
    return render_template("sign-in.html")


@app.route("/authorize", methods=["POST"])
def authorize():
    data = request.form
    user = User.query.filter(User.email == data.get("email")).first()
    if user:
        if hashlib.sha256(data.get("password").encode("utf-8")).hexdigest() == user.password:
            session["user"] = user.serialize
    return redirect("/users/homepage")


@app.route("/logout")
def logout():
    del session["user"]
    return redirect("/")


@app.route('/posts')
def get_posts():
    posts = Post.query.all()
    return render_template('get_all_posts.html', posts=posts)


@app.route("/posts/new-post", methods=['GET', 'POST'])
def create_post():
    if 'user' not in session or 'id' not in session['user']:
        return abort(401)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user = User.query.get(session['user']['id'])
        new_post = Post(
            title=title,
            content=content,
            author=user,
            edited=datetime.now().strftime("%Y-%m-%d %H:%M")
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect('/users/homepage')
    return render_template('create_post.html')


@app.route("/users/homepage")
def get_my_page():
    if 'user' not in session or 'id' not in session['user']:
        return redirect('/sign-in')
    posts = Post.query.filter(Post.user_id == session['user']['id']).all()
    return render_template('homepage.html', posts=posts)


@app.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author.id != session['user']['id']:
        return f"You don`t have permission!"

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post.title = title
        post.content = content
        post.edited = datetime.now().strftime("%Y-%m-%d %H:%M")
        db.session.commit()

        return redirect('/users/homepage')
    return render_template('edit_post.html', post=post)


@app.route('/posts/<int:post_id>/delete', methods=['GET', 'POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author.id != session['user']['id']:
        return abort(418)

    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        return redirect('/users/homepage')
    return render_template('delete_post.html', post=post)
