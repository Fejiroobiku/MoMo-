from datetime import datetime
import xml.etree.ElementTree as ET
from datetime import datetime


def convert_to_date(date_str: str) -> datetime:
    """Converts a string in eg: '10 May 2024 4:30:58 PM' format to a datetime object."""
    return datetime.strptime(date_str, "%d %b %Y %I:%M:%S %p")
