from datetime import timedelta
from typing import Any, Dict, Optional
from fastapi.responses import RedirectResponse
from injector import inject
import requests

from src.service.cache_service import CacheService
from src.core.settings.app_settings import AppSettings


class GithubAuthService:
    app_settings: AppSettings
    cache_service: CacheService
    
    @inject
    def __init__(self, app_settings: AppSettings, cache_service: CacheService) -> None:
        self.app_settings = app_settings
        self.cache_service = cache_service

    def login_user(self):
        return RedirectResponse(f'https://github.com/login/oauth/authorize?client_id={self.app_settings.github_client_id}')

    def handle_code(self, code: str) -> Dict[str, Any]:
        params = {
            'client_id'     : self.app_settings.github_client_id,
            'client_secret' : self.app_settings.github_client_secret,
            'code'          : code
        }
        headers = {'Accept': 'application/json'}
        response = requests.post(url='https://github.com/login/oauth/access_token', params=params, headers=headers).json()
        return response

    def get_user_info(self, token: str) -> Optional[Dict[str, Any]]:
        info = self.cache_service.get(token)
        if info:
            return info
        headers = {
            'Accept'        : 'application/json',
            'Authorization' : f'Bearer {token}'
            }
        response = requests.get(url='https://api.github.com/user', headers=headers)
        print(response.status_code)
        if response.status_code > 299:
            return None
        res_json = response.json()
        self.cache_service.put(token, res_json)
        return res_json
