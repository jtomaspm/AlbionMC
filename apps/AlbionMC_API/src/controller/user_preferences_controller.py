from fastapi import APIRouter, Depends, HTTPException, Request

from src.core.entities.user_preference import UserPreference
from src.repository.user_preferences_repository import UserPreferencesRepository

user_preference_router = APIRouter(prefix="/user_preferences", tags=["User Preferences"])

from src.dependencies import configure_injector
injector = configure_injector()


@user_preference_router.get("/{user_id}")
def get_item_price(user_id: int, user_preference_repo: UserPreferencesRepository = Depends(lambda: injector.get(UserPreferencesRepository))) -> UserPreference:
    user_preference = user_preference_repo.get(user_id=user_id)
    if user_preference:
        return user_preference
    else:
        raise HTTPException(status_code=404, detail="Item price not found")

@user_preference_router.post("/")
def create_item_price(request: Request, user_preference: UserPreference, user_preference_repo: UserPreferencesRepository = Depends(lambda: injector.get(UserPreferencesRepository))):
    user_preference_repo.new(user_preference, request.state.user['login'])
    return {"message": "User preference created successfully"}