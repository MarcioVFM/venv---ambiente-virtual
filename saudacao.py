from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/saudacao')
def saudacao():
    """
    Endpoint de saudacao
    """
    return {"Salve":"Cria"}