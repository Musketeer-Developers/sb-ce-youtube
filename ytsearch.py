from youtubesearchpython import Search
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["https://stickball-main-admin.vercel.app/", "https://stickball-main-admin.vercel.app", "stickball-main-admin.vercel.app", "http://localhost:3000",
        "https://stickball-main-admin-staging.vercel.app/", "https://stickball-main-admin-staging.vercel.app", "stickball-main-admin-staging.vercel.app",
        "https://stickball-admin-staging.vercel.app/", "https://stickball-admin-staging.vercel.app", "stickball-admin-staging.vercel.app", "http://manage-development.stickball.biz", "https://manage-development.stickball.biz", "manage-development.stickball.biz",
         "https://manage-staging.stickball.biz", "manage-staging.stickball.biz","http://manage-staging.stickball.biz", "https://manage.stickball.biz", "manage.stickball.biz", "https://stickball-admin.vercel.app", "stickball-admin.vercel.app", "http://stickball-admin.vercel.app/", "http://localhost:3001"
        ],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

@app.get("/")
def root():
    return {"message": "YouTube Api!!"}


@app.post("/yt_search")
def youtube_search(search):
    all_links = list()
    try:
        allSearch = Search(search, limit = 15)
        
        for X, each in enumerate(allSearch.result()['result']):
            diction=dict()
            diction["title"] = allSearch.result()['result'][X]['title']
            diction["link"] = allSearch.result()['result'][X]['link']
            all_links.append(diction)
    except:
        pass
    return all_links


@app.post("/keyword_search_youtube")
def keyword_search(search):
    all_links = list()
    try:
        allSearch = Search(search, limit = 15)
        
        for X, each in enumerate(allSearch.result()['result']):
            diction=dict()
            diction["title"] = allSearch.result()['result'][X]['title']
            diction["link"] = allSearch.result()['result'][X]['link']
            all_links.append(diction)
    except:
        pass
    return all_links


# print(youtube_search("data scientist"))
