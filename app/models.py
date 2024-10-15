from django.db import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
# Create your models here.
class Fund(Base):
    __tablename__ = "funds"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    size_million = Column(Float)
    total_capital_committed_billion = Column(Float)
    global_south_deals = Column(Integer)
    global_south_countries = Column(Integer)

    # Relationship: A fund can have multiple companies
    companies = relationship("Company", back_populates="fund")


class Company(Base):
    __tablename__ = "companies"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    investment_million = Column(Float)
    country = Column(String)
    country_capital_million = Column(Float)
    theme = Column(String)
    theme_capital_million = Column(Float)

    # ForeignKey to link to the Fund table
    fund_id = Column(String, ForeignKey("funds.id"))
    fund = relationship("Fund", back_populates="companies")

    # Emissions details
    total_emissions = Column(Float)
    scope_1_emissions = Column(Float)
    scope_2_emissions = Column(Float)
    scope_3_emissions = Column(Float)