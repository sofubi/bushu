from bushu.http.client import Client
from bushu import Book

if __name__ == "__main__":
    client = Client()
    chapter = Book(client, 2048, 1)
else:
    print("bushu")
