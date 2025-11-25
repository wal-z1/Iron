from fastapi import FastAPI, HTTPException
from app.schema import POSTinfo
app = FastAPI()

post_text = {
    1: {"title": "first post", "content": "Just got started with this blog! Excited to share thoughts."},
    2: {"title": "morning thoughts", "content": "Woke up early today and the coffee tasted amazing."},
    3: {"title": "tech musings", "content": "FastAPI is surprisingly fast for building APIs."},
    4: {"title": "random notes", "content": "Sometimes you just need to take a walk and breathe."},
    5: {"title": "coding life", "content": "Debugging code at 2 AM feels like a mini adventure."},
    6: {"title": "travel dreams", "content": "One day, I will visit the mountains and watch the sunrise."},
    7: {"title": "book review", "content": "Just finished a novel—characters were deep and relatable."},
    8: {"title": "fun fact", "content": "Did you know octopuses have three hearts? Fascinating creatures."},
    9: {"title": "daily grind", "content": "Work emails piling up, but progress feels good."},
    10: {"title": "random thought", "content": "If cats could talk, would they tell us secrets or just judge?"}
}

@app.get("/posts")
def getallposts(limit: int = 0):
    if limit:
        return list(post_text.values())[0:limit]
    return post_text

@app.get("/posts/{id}")
def fetchpost(id: int):
    if id not in post_text:
        raise HTTPException(status_code=404, detail="Post not found")
    return post_text[id]

@app.post("/posts")
def createPost(post : POSTinfo):
    newpost=  {"title": post.title,"content":post.content}
    post_text[max(post_text.keys()) +1] = newpost
    return newpost

@app.delete("/posts/{id}")
def deletepost(id):
    if id not in post_text.keys():
       raise HTTPException(status_code=404,detail="the post wasnt found in the database")
    del post_text[id]
    return {"message": "Post deleted successfully"}
