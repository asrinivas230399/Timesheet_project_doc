# This module can contain utility functions that are used across the application

def format_date(date_str):
    # Example utility function to format date strings
    from datetime import datetime
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%d-%m-%Y")