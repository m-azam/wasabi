import json

from fastapi import FastAPI, Request
from pydantic import BaseModel, create_model
from services import question_generator, convert_pdf2text, update_user_data, issue_vc, verify_vc
from fastapi.middleware.cors import CORSMiddleware
import logging
from services import signup_login_service
from typing import Optional, Dict, Any
import pandas as pd
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


class Receipt(BaseModel):
    studentId: str


class callback_request(BaseModel):
    code: str
    requestId: Optional[str]
    state: Optional[str]
    subject: Optional[str]
    receipt: Receipt = None


class register_login(BaseModel):
    uname: str
    password: str
    student_id: Optional[str]


class verify_request(BaseModel):
    text: str


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
    if signup_login_service.signup_service(req.uname, req.password, req.student_id) == 1:
        resp = issue_vc.issue_token_api(req.student_id)
        qr_code = resp['qrCode']
        return {"status": "Registration successful", "signup_status_flag": 1, "qr_code": qr_code}
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


@app.get("/verify", status_code=200)
async def verify():
    resp = verify_vc.verify_vc()
    qr_code = resp['qrCode']
    return {"qr_code": qr_code}


@app.post("/callback")
def callback(req: Dict[Any, Any]):
    if req['issuers'] is not None:
        student_id = req['issuers'][0]['claims']['studentId']
        update_user_data.store_student_id(student_id)


@app.get("/get_score", status_code=200)
async def return_score():
    df = pd.read_csv('/Users/sachinvm/Desktop/CS Study/MsftHack/wasabi/qna-app/services/university.csv')
    ids = df.iloc[:, -1]
    list = ids.tolist()
    print(list[-1])
    return list[-1]
