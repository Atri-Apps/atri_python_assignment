from typing import TypedDict
from datetime import datetime

class UniqueViewsDocument(TypedDict):
    """
    The data in GitHub gets lost after every 14 days, hence, we need to
    record the date on which the data has been fetched.
    """
    date: datetime
    site: str
    unique_views: int
