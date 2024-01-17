from django.shortcuts import render
from datetime import date

list_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Max",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "I had the best week ever with my family. We went for a week on the mountains.",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos.
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "woods.jpg",
        "author": "Max",
        "date": date(2021, 7, 21),
        "title": "Woods",
        "excerpt": "I had the best week ever with my family. We went for a week on the mountains.",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos.
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "coding.jpg",
        "author": "Max",
        "date": date(2021, 7, 21),
        "title": "Programming",
        "excerpt": "I had the best week ever with my family. We went for a week on the mountains.",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos.

        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nobis
        aperiam est praesentium, quos.
        """
    },
]

def get_date(post):
    return post['date']
def index(request):
    sorted_posts = sorted(list_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})

def posts(request):
    return render(request, "blog/posts.html", {"all_posts": list_posts})

def post_detail(request, slug):
    identified_post = next(post for post in list_posts if post['slug'] == slug)
    return render(request, "blog/post_detail.html", {"post": identified_post})