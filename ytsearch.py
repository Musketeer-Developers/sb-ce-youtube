from youtubesearchpython import Search
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!!"}


@app.post("/yt_search")
def youtube_search(search):
    allSearch = Search(search, limit = 5)
    titles = []
    links = []
    for X, each in enumerate(allSearch.result()['result']):
        titles.append(allSearch.result()['result'][X]['title'])
        links.append(allSearch.result()['result'][X]['link'])
    return titles,links


# print(youtube_search("data scientist"))