from pydantic import BaseModel


class AppSettings(BaseModel):
    github_client_id        : str
    github_client_secret    : str