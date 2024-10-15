from pydantic import BaseModel
from typing import List

# Company schemas
class CompanyBase(BaseModel):
    name: str
    investment_million: float
    country: str
    country_capital_million: float
    theme: str
    theme_capital_million: float
    total_emissions: float
    scope_1_emissions: float
    scope_2_emissions: float
    scope_3_emissions: float

class CompanyCreate(CompanyBase):
    fund_id: str

class Company(CompanyBase):
    id: str

    class Config:
        orm_mode = True


# Fund schemas
class FundBase(BaseModel):
    name: str
    size_million: float
    total_capital_committed_billion: float
    global_south_deals: int
    global_south_countries: int

class FundCreate(FundBase):
    pass

class Fund(FundBase):
    id: str
    companies: List[Company] = []

    class Config:
        orm_mode = True