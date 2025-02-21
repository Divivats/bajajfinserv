from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=False,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Hardcoded user details
USER_ID = "Divyansh_Vats_22BAI71419"
EMAIL = "divyansh@xyz.com"
ROLL_NUMBER = "22AML4A"

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
