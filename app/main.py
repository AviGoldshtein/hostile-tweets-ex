from fastapi import FastAPI
from app.manager import Manager
from bson.json_util import dumps
import uvicorn


app = FastAPI()

manager = Manager()

@app.get("analysis_information")
def analysis_information():
    return dumps(manager.get_results())

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)