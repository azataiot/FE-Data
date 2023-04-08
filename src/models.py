from pydantic import BaseModel


class ProfileBase(BaseModel):
    city: str | None = None
    zip: str | None = None
    state: str | None = None
    country: str | None = None
    phone: str | None = None
    website: str | None = None
    industry: str | None = None
    sector: str | None = None


class ProfileIn(ProfileBase):
    address1: str | None = None
    longBusinessSummary: str | None = None
    fullTimeEmployees: int | None = None
    auditRisk: int | None = None
    boardRisk: int | None = None
    compensationRisk: int | None = None
    shareHolderRightsRisk: int | None = None
    overallRisk: int | None = None
    governanceEpochDate: int | None = None
    compensationAsOfEpochDate: int | None = None


class Profile(ProfileBase):
    address: str | None = None
    long_business_summary: str | None = None
    full_time_employees: int | None = None
    audit_risk: int | None = None
    board_risk: int | None = None
    compensation_risk: int | None = None
    share_holder_rights_risk: int | None = None
    overall_risk: int | None = None
    governance_epoch_date: int | None = None
    compensation_as_of_epoch_date: int | None = None


class MetaDataRaw(BaseModel):
    symbol: str
    name: str
    market: str


class MetaDataProfile(MetaDataRaw, Profile):
    pass


class MetaData(MetaDataProfile):
    # if we do not have sector, we will use the default value "Other". This is to avoid the error when we try to use the sector as a key in the dictionary.
    sector: str | None = "Other"
    # if we do not have industry, we will use the default value "Other".
    industry: str | None = "Other"
    # if we do not have the country, we will use the default value "Other".
    country: str | None = "Other"
    start_date: str


class MetaDataMin(BaseModel):
    symbol: str
    name: str
    market: str
    sector: str | None = "Other"
    industry: str | None = "Other"
    country: str | None = "Other"
    start_date: str


# define a model for security metadata
class BaseMetaData(BaseModel):
    # All financial Assets must have symbol (ticker), name
    symbol: str
    name: str
    # For assets that dose not have the market type, we will use the default value "N/A"
    market: str | None = "N/A"
    start_date: str | None = None  # written as startDate in the json file


# define a model for CryptoCurrency metadata
class CryptoMetaData(BaseMetaData):
    # All CryptoCurrency must have the market type "Crypto"
    market: str = "Crypto"
    start_date: str | None = None  # written as startDate in the json file
    description: str | None = None
    twitter: str | None = None


# define a model for Stock metadata
class StockMetaData(BaseMetaData):
    # All Stock must have the market type "Stock"
    market: str = "Stock"
    start_date: str | None = None  # written as startDate in the json file
    description: str | None = None


# define a model for Bond metadata
class BondMetaData(BaseMetaData):
    # All Bond must have the market type "Bond"
    market: str = "Bond"


# define a model for ETF metadata
class ETFMetaData(BaseMetaData):
    # All ETF must have the market type "ETF"
    market: str = "ETF"
    start_date: str | None = None  # written as startDate in the json file
    description: str | None = None
    business_summary: str | None = (
        None  # written as longBusinessSummary in the json file
    )


# define a model for MutualFund metadata
class FundMetaData(BaseMetaData):
    # All Fund must have the market type "Fund"
    market: str = "Fund"
    start_date: str | None = None  # written as startDate in the json file
    description: str | None = None
    business_summary: str | None = (
        None  # written as longBusinessSummary in the json file
    )
    phone: str | None = None


# define a model for Index metadata


class IndexMetaData(BaseMetaData):
    # All Index must have the market type "Index"
    market: str = "Index"
    start_date: str | None = None  # written as startDate in the json file
    description: str | None = None
    business_summary: str | None = (
        None  # written as longBusinessSummary in the json file
    )


# define a model for Forex metadata
class ForexMetaData(BaseMetaData):
    # All Forex must have the market type "Forex"
    market: str = "Forex"


# define a model for Commodity metadata
class CommodityMetaData(BaseMetaData):
    # All Commodity must have the market type "Commodity"
    market: str = "Commodity"
