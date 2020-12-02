from bushu.http.client import Client
from bushu import Chapter

if __name__ == "__main__":
    client = Client('sofubi', 'TmLCY5VdRCqisj')
    chapter = Chapter(client, 2048, 1)
    chapter.get_chapter_data()
    chapter.download_pages()
else:
    print("Try again")
