import requests
from post import Post

BLOG_URL = "https://api.npoint.io/6cb2d989d72a8ecd6eb6"


class Posts:
    posts: Post = []

    def __init__(self) -> None:
        res = requests.get(BLOG_URL)
        res.raise_for_status()
        response_data = res.json()

        for post in response_data:
            self.posts.append(
                Post(
                    post['id'],
                    post['title'],
                    post['subtitle'],
                    post['body'],
                    post['author'],
                    post["date"]
                )
            )

    def find(self, index: int) -> Post | None:
        for post in self.posts:
            if post.id == index:
                return post

        return None
