import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Prompt(BaseModel):
    title: str
    tag: str
    mainCharacterName: str
    plot: str


    def to_prompt_format(self):
        instruction_format = """
### 소설 제목은 다음과 같아
{title}

### 소설의 줄거리는 다음과 같아
{plot}

### 소설의 장르는 다음과 같아
{tag}

### 주인공 이름은 다음과 같아
{name}

### 소설의 내용은 다음과 같아
"""

        return instruction_format.format(title=self.title, plot=self.plot, tag=self.tag, name=self.mainCharacterName)

    def __str__(self):
        return self.to_prompt_format()

app = FastAPI()
model_id = "kichan05/Novel-Kaguya"
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_model():
    global model_id
    return None

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/generate")
async def generate(prompt: Prompt):
    print(prompt)
    time.sleep(2)
    return {
        "novel" : "개쩌는 인공지능이 만든 소설",
        "prompt": prompt.to_prompt_format()
    }