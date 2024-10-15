from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud
from .database import engine, get_db

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Create a new fund
@app.post("/funds/", response_model=schemas.Fund)
def create_fund(fund: schemas.FundCreate, db: Session = Depends(get_db)):
    return crud.create_fund(db=db, fund=fund)

# Get a list of funds
@app.get("/funds/", response_model=List[schemas.Fund])
def read_funds(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    funds = crud.get_funds(db, skip=skip, limit=limit)
    return funds

# Create a new company
@app.post("/companies/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db=db, company=company)

# Get a list of companies
@app.get("/companies/", response_model=List[schemas.Company])
def read_companies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    companies = crud.get_companies(db, skip=skip, limit=limit)
    return companies
