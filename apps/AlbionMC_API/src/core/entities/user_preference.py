from pydantic import BaseModel


class UserPreference(BaseModel):
    user_id: int
    theme: str