import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Optional, good practice for dev purposes. Allow all middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/search?query=bayesian-neural-networks
@app.get("/search")
def search(query: str):  # "bayesian neural networks" / "adam optimizers" / ...
    """
    Calls search function from logic/search.py and returns the top 5 results in list of str format.
    """
    import research_pulse.logic.search as ls
    data=ls.load_data()
    vector, matrix = ls.vectorizer(data)
    top20=ls.search(query.lower(), data, vector, matrix)
    return {'#1': top20[0], '#2': top20[1], '#3': top20[2], '#4': top20[3], '#5': top20[4],
            '#6': top20[5], '#7': top20[6], '#8': top20[7], '#9': top20[8], '#10': top20[9],
            '#11': top20[10], '#12': top20[11], '#13': top20[12], '#14': top20[13], '#15': top20[14],
            '#16': top20[15], '#17': top20[16], '#18': top20[17], '#19': top20[18], '#20': top20[19]}

@app.get("/")
def root():
    return {'greeting':'Hello'}
