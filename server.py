from flask import Flask, render_template
from post import Post
from posts import Posts

app = Flask(__name__)

posts: Posts = Posts()


@app.route("/")
def home():
    return render_template('index.html', posts=posts.posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/posts/<int:id>")
def post(id: int):
    current_post = posts.find(id)

    if not current_post:
        return "Page not found"

    return render_template('post.html', post=current_post)


if __name__ == "__main__":
    app.run(debug=True, port=8888)
