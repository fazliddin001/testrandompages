from random import shuffle

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


fake_data = [
    {
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_4N37TIgWC_QLpspNwGddZH8DhzljeYMFnA&s",
        "caption": "YouTube"
    },
    {
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/"
                     "1200px-GitHub_Invertocat_Logo.svg.png",
        "caption": "GitHub"
    },
    {
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWOoWb2-XM9PsxK940NqKjKKFlmN3Q8zDR0A&s",
        "caption": "Nginx"
    }
]

@app.get("/")
async def get_data():
    shuffle(fake_data)
    return fake_data


if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
