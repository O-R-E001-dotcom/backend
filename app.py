from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv

import uvicorn
import os   

load_dotenv()
app = FastAPI(title="Ore's API", version="1.0.0") 

data = [{"name": "Victory", "age": 20, "track": "AI Dev"},
        {"name": "Peter", "age": 21, "track": "AI Engineer"},
        {"name": "Samantha", "age": 22, "track": "AI Dev"}] 

class Item(BaseModel):
    name:str = Field(..., example= "Florence")
    age: int = Field(..., example= 23)
    track: str = Field(..., example= "AI Dev")

@app.get("/", description="This endpoint returns a welcome message")
def root():
    return {"message": "Welcome to my FastAPI App"}

@app.get("/get-data")
def get_data():
    return data

@app.post("/create-data")
def create_data(req: Item):
    data.append(req.dict())
    print(data)
    return {"Message": "Data received", "Data": data}

@app.put("/update-data/{id}")
def update_data(id: int, req: Item):
    data[id] = req.dict()
    print(data)

@app.patch("/update-data/{id}")
def partial_update(id: int, req: Item):
    for key, value in req.dict().items():
        if value:  # only update non-empty values
            data[id][key] = value
    return {"message": "Data partially updated", "data": data}
   

@app.delete("/delete-data{id}")
def delete_data(id: int):
    deleted = data.pop(id)
    print(data)
    return {"message": "Data deleted successfully", "deleted": deleted, "data": data}
    
    
if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))    
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))
    # try:
    #     uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")), reload=True)
    # except OSError:
    #     # If port 8000 is already in use, switch to 8001
    #     print(f" Port {port} already in use — switching to {port + 1}")
    #     uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")) + 1, reload=True)   


