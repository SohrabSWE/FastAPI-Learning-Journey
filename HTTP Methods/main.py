from fastapi import FastAPI,Path, HTTPException
import json

app = FastAPI()

def load_data():
    with open('studdent.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def home():
    return "Student Management System API."

@app.get("/about")
def about():
    return "A fully functional API to manage our students records."

@app.get("/view")
def view_students():
    data = load_data()
    return data

@app.get("/view/{student_id}")
def view_studnets_by_id(student_id: str = Path(..., description="Student id of the Students", example="S001")):
    data = load_data()

    if student_id in data:
        return data[student_id]
    else:
        raise HTTPException( status_code= 404 ,detail="Student not found.")
    