from typing import List, Optional
from pydantic import BaseModel

class DataFromPDF(BaseModel):
    Company_Name: Optional[str] = None
    Industry: Optional[str] = None
    Market_Capitalization: Optional[str] = None
    Revenue_in_millions: Optional[str] = None
    EBITDA_in_millions: Optional[str] = None
    Net_Income_in_millions: Optional[str] = None
    Debt_in_millions: Optional[str] = None
    Equity_in_millions: Optional[str] = None
    Enterprise_Value_in_millions: Optional[str] = None
    P_E_Ratio: Optional[str] = None
    Revenue_Growth_Rate: Optional[str] = None
    EBITDA_Margin: Optional[str] = None
    ROE_Return_on_Equity: Optional[str] = None
    ROA_Return_on_Assets: Optional[str] = None
    Current_Ratio: Optional[str] = None
    Debt_to_Equity_Ratio: Optional[str] = None
    Location: Optional[str] = None
    CEO: Optional[str] = None
    Number_of_Employees: Optional[str] = None

class DataFromDatabase(BaseModel):
    Company_Name: Optional[str] = None
    Industry: Optional[str] = None
    Market_Capitalization: Optional[str] = None
    Revenue_in_millions: Optional[str] = None
    EBITDA_in_millions: Optional[str] = None
    Net_Income_in_millions: Optional[str] = None
    Debt_in_millions: Optional[str] = None
    Equity_in_millions: Optional[str] = None
    Enterprise_Value_in_millions: Optional[str] = None
    P_E_Ratio: Optional[str] = None
    Revenue_Growth_Rate: Optional[str] = None
    EBITDA_Margin: Optional[str] = None
    Net_Income_Margin: Optional[str] = None
    ROE_Return_on_Equity: Optional[str] = None
    ROA_Return_on_Assets: Optional[str] = None
    Current_Ratio: Optional[str] = None
    Debt_to_Equity_Ratio: Optional[str] = None
    Location: Optional[str] = None

class DifferenceResponse(BaseModel):
    dataFromPDF: Optional[DataFromPDF] = None
    dataFromDatabase: Optional[DataFromDatabase] = None
    delta: Optional[List[str]] = None
