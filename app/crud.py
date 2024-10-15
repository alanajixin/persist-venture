from sqlalchemy.orm import Session
from . import models, schemas
import uuid

# Create a new fund
def create_fund(db: Session, fund: schemas.FundCreate):
    db_fund = models.Fund(
        id=str(uuid.uuid4()),
        name=fund.name,
        size_million=fund.size_million,
        total_capital_committed_billion=fund.total_capital_committed_billion,
        global_south_deals=fund.global_south_deals,
        global_south_countries=fund.global_south_countries
    )
    db.add(db_fund)
    db.commit()
    db.refresh(db_fund)
    return db_fund

# Get all funds
def get_funds(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Fund).offset(skip).limit(limit).all()

# Create a new company
def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(
        id=str(uuid.uuid4()),
        name=company.name,
        investment_million=company.investment_million,
        country=company.country,
        country_capital_million=company.country_capital_million,
        theme=company.theme,
        theme_capital_million=company.theme_capital_million,
        total_emissions=company.total_emissions,
        scope_1_emissions=company.scope_1_emissions,
        scope_2_emissions=company.scope_2_emissions,
        scope_3_emissions=company.scope_3_emissions,
        fund_id=company.fund_id
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

# Get all companies
def get_companies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Company).offset(skip).limit(limit).all()