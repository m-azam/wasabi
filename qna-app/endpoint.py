from fastapi import FastAPI
from pydantic import BaseModel, Field
from services import question_generator, convert_pdf2text, update_user_data
from fastapi.middleware.cors import CORSMiddleware
import logging
from services import signup_login_service
from typing import Optional

app = FastAPI()

origins = [
    "http://localhost:8060",
    "http://localhost:8080",
    "http://localhost:8090",
    "http://localhost:8000",
    "http://localhost:8000/login.html?",
    "http://18.188.61.131/ui/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class text_qna_request(BaseModel):
    text: str


class pdf_qna_request(BaseModel):
    base64encoded: str


class callback_request(BaseModel):
    text: str


class register_login(BaseModel):
    uname: str
    password: str


class update_user_score(BaseModel):
    uname: str
    score: Optional[str]
    date: Optional[str]
    school_id: Optional[str]


@app.post("/qna/getqna/text")
async def getTextQnA(req: text_qna_request):
    logging.info("text qna endpoint called")
    paragraph = req.text
    questions = question_generator.get_qna(paragraph)
    logging.info("qna text call complete")
    return questions


@app.post("/getqna/pdf")
async def getPdfQnA(req: pdf_qna_request):
    logging.info(req.base64encoded)
    paragraphs = convert_pdf2text.get_paras(req.base64encoded)
    qna_list = []
    for paragraph in paragraphs:
        question_generator.get_multi_para_qna(paragraph, qna_list)
    return qna_list


@app.post("/authentication/register", status_code=200)
async def register(req: register_login):
    if signup_login_service.signup_service(req.uname, req.password) == 1:
        return {"status": "Registration successful", "signup_status_flag": 1}
    else:
        return {"status": "Registration unsuccessful! Username may already exist", "signup_status_flag": 0}


@app.post("/authentication/login", status_code=200)
async def login(req: register_login):
    print(req.uname)
    print(req.password)
    if signup_login_service.login_service(req.uname, req.password) == 1:
        return {"status": "Login successful", "login_status_flag": 1}
    else:
        return {"status": "Please check username and password!", "login_status_flag": 0}


@app.post("/update/score", status_code=200)
async def update_score(req: update_user_score):
    if update_user_data.update_score(req.uname, req.score) == 1:
        return {"status": "update successful"}
    else:
        return {"status": "username does not exist"}


@app.post("/update/date", status_code=200)
async def update_score(req: update_user_score):
    if update_user_data.update_date(req.uname, req.date) == 1:
        return {"status": "update successful"}
    else:
        return {"status": "username does not exist"}


@app.post("/update/schoolid", status_code=200)
async def update_score(req: update_user_score):
    if update_user_data.update_schoolid(req.uname, req.school_id) == 1:
        return {"status": "update successful"}
    else:
        return {"status": "username does not exist"}


@app.post("/callback")
async def callback(req: callback_request):
    print(req.text)
