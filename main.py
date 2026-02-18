from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
class Tea(BaseModel):
    id : int
    name : str
    origin : str
teas : List[Tea] = []

@app.get("/")
def read_root():
    return{"message ":"welcome to the tea house"}


@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_teas(tea:Tea):
    return teas.append(tea)

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int , updated_tea : Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            tea[index] = update_tea
            return update_tea
    return {"error":{"tea no found !"}}


@app.delete("/teas/{tea_id}")
def delete_tea(tea_id:int):
    for index, tea in enumerate(teas):
        if tea.id== tea_id:
            deleted = teas.pop(index)
            return deleted
    return {"error" : "tea not found !"}