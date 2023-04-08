from pydantic import BaseModel


# create a class for the get_stock_profile_data() method as StockProfile

class Profile(BaseModel):
    address1: str | None = None
    city: str | None = None
    zip: str | None = None
    state: str | None = None
    country: str | None = None
    phone: str | None = None
    website: str | None = None
    industry: str | None = None
    sector: str | None = None
    longBusinessSummary: str | None = None
    fullTimeEmployees: int | None = None
    auditRisk: int | None = None
    boardRisk: int | None = None
    compensationRisk: int | None = None
    shareHolderRightsRisk: int | None = None
    overallRisk: int | None = None
    governanceEpochDate: int | None = None
    compensationAsOfEpochDate: int | None = None
