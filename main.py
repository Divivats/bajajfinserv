from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI()

# Hardcoded user details
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

class RequestModel(BaseModel):
    data: list

@app.post("/bfhl")
def process_data(request: RequestModel):
    try:
        numbers = [x for x in request.data if re.match(r"^\d+$", str(x))]
        alphabets = [x for x in request.data if isinstance(x, str) and x.isalpha()]
        highest_alphabet = sorted(alphabets, key=lambda x: x.lower(), reverse=True)[:1]

        return {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
    except:
        raise HTTPException(status_code=400, detail="Invalid Input")

@app.get("/bfhl")
def get_operation_code():
    return {"operation_code": 1}
