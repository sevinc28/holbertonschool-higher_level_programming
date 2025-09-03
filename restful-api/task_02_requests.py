import requests 
import csv

API_Url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        structured_data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

    with open("posts.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, filenames=["id", "ittle", "body"])
        writer.writeheader()
        writer.writerows(structured_data)