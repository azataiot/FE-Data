class SymbolOHLVCExistsException(Exception):
    """Symbol OHLCV file already exists."""
    pass


class EmptyResponseException(Exception):
    """Empty response(df) from the API"""
    pass
