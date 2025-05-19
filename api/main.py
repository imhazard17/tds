from fastapi import FastAPI, Query, HTTPException
from typing import List
import json

app = FastAPI()

# Load data from the JSON file once at startup
def load_data(filename: str = "q-vercel-python.json") -> dict:
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail=f"Data file '{filename}' not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail=f"Error decoding JSON from '{filename}'.")

# Initialize data
DATA = marks_dict = {student['name']: student['marks'] for student in load_data()}

@app.get("/api")
def get_marks(name: List[str]) -> dict:
    marks = []
    # if len(name) == 0:
    #     return {"marks": marks}
    for n in name:
        if n in list(DATA.keys()):
            marks.append(DATA[n])
        else:
            marks.append(None)
    return {"marks|": marks}
