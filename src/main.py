from fastapi import FastAPI, HTTPException
from src.idatabase import IDatabase
from src.idiff_lib import IDiffLib
from src.ipdf_service import IPdfService
from src.models import DifferenceResponse
from enum import Enum

app = FastAPI()

class AssetParamEnum(str, Enum):
    financellc = "financellc"
    healthinc  = "healthinc"
    retailco   = "retailco"
    techcorp   = "techcorp"

@app.get("/difference/{asset}", response_model=DifferenceResponse)
def get_difference(asset: AssetParamEnum):    
    data_handler = IPdfService(file_path = asset)
    try:
        data_from_pdf = data_handler.get_data()
    except FileNotFoundError:
        raise HTTPException(status_code = 500, detail = f"Error: File {asset} not found")
    
    data_from_db = IDatabase().query_db(data_from_pdf["Company_Name"])
    diff = IDiffLib(data_from_pdf, data_from_db).get_diff()

    return {
        "dataFromPDF": data_from_pdf,
        "dataFromDatabase": data_from_db,
        "delta": diff
    }
