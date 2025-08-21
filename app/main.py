from fastapi import FastAPI
from app.manager import Manager
from app.helper import convert_bson_types


app = FastAPI()

manager = Manager()

@app.get("/analysis_information")
def analysis_information():
    return convert_bson_types(manager.get_results())