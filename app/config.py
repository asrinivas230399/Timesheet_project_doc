from pydantic import BaseSettings

class Settings(BaseSettings):
    TIME_TRACKING_API_URL: str = "https://api.timetracking.com"
    HRM_API_URL: str = "https://api.hrmservice.com"
    # Add more configuration options for different time tracking tools and HRM systems
    ANOTHER_TIME_TRACKING_API_URL: str = "https://api.anothertimetracking.com"
    ANOTHER_HRM_API_URL: str = "https://api.anotherhrmservice.com"

settings = Settings()