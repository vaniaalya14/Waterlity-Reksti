import json
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from pydantic import BaseModel
import psycopg2 as psycopg
import time
app = FastAPI()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost:1234",
    "http://localhost:1234/",
    "http://localhost:1234"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
@app.post('/read', tags = ['Add reading'])
def write_from_sensor (pH : float, temp:float, turbid : float, dissoxy : float, orp : float, cond  :float):
    # change this line to connect code to database
    query= db.cursor()
    # add query to database according to the parameters from function
    db.commit()
    query.close()
    db.close()
    return
@app.get('/Averages', tags=['Counting Aggregate'])
def count_averages():
    # change this line to connect code to database
    query = db.cursor()
    #query to take avg
    reading = query.fetchone()
    avgph=reading[0]
    avgturb = reading[1]
    avgdissoxy = reading[2]
    avgtemp = reading[3]
    avgorp = reading[4]
    avgcond = reading[5]
    # print ()
    return {"avgph":avgph, "avgturbidity":avgturb, "avgdissox":avgdissoxy, "avgtemp":avgtemp, "avgoxired":avgorp, "avgconductivity":avgcond}
@app.get('/Minimum', tags=["Counting Aggregate"])
def count_minimum():
    # change this line to connect code to database
    query = db.cursor()
    #query to take min number for each column
    reading = query.fetchone()
    minph = reading[0]
    minturb = reading[1]
    mindissoxy=reading[2]
    mintemp = reading[3]
    minorp = reading[4]
    mincond = reading[5]
    return {"minph":minph, "minturbidity":minturb,"mindissox":mindissoxy, "mintemp":mintemp, "minoxired":minorp, "minconductivity":mincond}

@app.get('/Maximum', tags=["Counting Aggregate"])
def count_maximum():
    # change this line to connect code to database
    query = db.cursor()
    #query to take max number for each column
    reading = query.fetchone()
    minph = reading[0]
    minturb = reading[1]
    mindissoxy=reading[2]
    mintemp = reading[3]
    minorp = reading[4]
    mincond = reading[5]
    return {"maxph":minph, "maxturbidity":minturb,"maxdissox":mindissoxy, "maxtemp":mintemp, "maxoxired":minorp, "maxconductivity":mincond}
    
@app.get('/Kelayakan-minum-secara-smart', tags=["Kelayakan minum secara smart"])
def Kelayakan_last_reading():
    # change this line to connect code to database
    query = db.cursor()
    #query to take avg
    avg= query.fetchone()
    avgph=avg[0]
    avgturb = avg[1]
    avgdissoxy = avg[2]
    avgtemp = avg[3]
    #query to take datas
    lastreading = query.fetchone()
    lastph = lastreading[0]
    lastturb = lastreading[1]
    lastdissoxy = lastreading[2]
    lasttemp = lastreading[3]
    ksrph = 1-(abs(lastph-avgph)/avgph)
    ksrturb = 1-(abs(lastturb-avgturb)/avgturb)
    ksrdissoxy = 1-(abs(lastdissoxy-avgdissoxy)/avgdissoxy)
    ksrtemp = 1-(abs(lasttemp-avgtemp)/avgtemp)
    appropriateness = ksrph * ksrdissoxy * ksrtemp * ksrturb
    return {"Kelayakan minum" : appropriateness}

@app.get('/Kelayakan-minum', tags=["Kelayakan minum secara normal"])
def Kelayakan_minum():
    # change this line to connect code to database
    query = db.cursor()
    #query to take datas
    lastreading = query.fetchone()
    lastph = lastreading[0]
    lastturb = lastreading[1]
    lastdissoxy = lastreading[2]
    lasttemp = lastreading[3]
    if lastdissoxy > 4 :
        if lastturb < 0.5 :
            if lasttemp>=24 and lasttemp <=30 :
                if lastph >= 6.5 and lastph <=8.5:
                    return {"Kelayakan" : "layak"}
    return {"Kelayakan" : "Tidak layak"}

@app.get('/Kelayakan-sanitasi', tags=["Kelayakan sanitasi"])
def Kelayakan_sanitasi():
    # change this line to connect code to database
    query = db.cursor()
    #query to take datas
    lastreading = query.fetchone()
    lastph = lastreading[0]
    lastturb = lastreading[1]
    lastdissoxy = lastreading[2]
    lasttemp = lastreading[3]
    if lastturb < 0.5 :
        if lasttemp>=16 and lasttemp <=30 :
            if lastph >= 6.5 and lastph <=8.5:
                return {"Kelayakan" : "layak"}
    return {"Kelayakan" : "Tidak layak"}
@app.get('/Kelayakan-mandi', tags=["Kelayakan mandi"])
def Kelayakan_mandi():
    # change this line to connect code to database
    query = db.cursor()
    #query to take datas
    lastreading = query.fetchone()
    lastph = lastreading[0]
    lastturb = lastreading[1]
    lastdissoxy = lastreading[2]
    lasttemp = lastreading[3]
    if lastdissoxy >= 4:
        if lastturb < 0.5 :
            if lasttemp>=16 and lasttemp <=30 :
                if lastph >= 6.5 and lastph <=8.5:
                    return {"Kelayakan" : "layak"}
    return {"Kelayakan" : "Tidak layak"}

@app.get('/Kelayakan-tani', tags=["Kelayakan tani"])
def Kelayakan_sanitasi():
    # change this line to connect code to database
    query = db.cursor()
    #query to take datas
    lastreading = query.fetchone()
    lastph = lastreading[0]
    lastturb = lastreading[1]
    lastdissoxy = lastreading[2]
    lasttemp = lastreading[3]
    lastorp = lastreading[4]
    lastcond = lastreading[5]
    if lastdissoxy >= 0:
        if lastturb < 30 and lastturb > 0.2 :
            if lasttemp>=29 and lasttemp <=33 :
                if lastph >= 5 and lastph <=9:
                    if lastcond < 250 :
                        if lastorp >=300 and lastorp<=500 :
                            return {"Kelayakan" : "layak"}
    return {"Kelayakan" : "Tidak layak"}

@app.get('/Kelayakan-perikanan', tags=["Kelayakan perikanan"])
def Kelayakan_sanitasi():
    # change this line to connect code to database
    query = db.cursor()
    #query to take datas
    lastreading = query.fetchone()
    lastph = lastreading[0]
    lastturb = lastreading[1]
    lastdissoxy = lastreading[2]
    lasttemp = lastreading[3]
    lastorp = lastreading[4]
    lastcond = lastreading[5]
    if lastdissoxy > 4:
        if lastturb < 30 and lastturb > 0.2 :
            if lasttemp>=28 and lasttemp <=32 :
                if lastph >= 6 and lastph <=9:
                    if lastcond < 250 :
                        if lastorp >=300 and lastorp<=500 :
                            return {"Kelayakan" : "layak"}
    return {"Kelayakan" : "Tidak layak"}

@app.get('/last-read', tags=["Pembacaan nilai terakhir"])
def last_read():
    # change this line to connect code to database
    query = db.cursor()
    #query to take datas
    lastreading = query.fetchone()
    lastph = lastreading[0]
    lastturb = lastreading[1]
    lastdissoxy = lastreading[2]
    lasttemp = lastreading[3]
    lastorp = lastreading[4]
    lastcond = lastreading[5]
    return {"lastph" : lastph, "lastturb" : lastturb, "lastdissoxy" : lastdissoxy, "lasttemp" : lasttemp, "lastorp":lastorp, "lastcond":lastcond}