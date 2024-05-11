from typing import Any, Dict, Optional
from fastapi.responses import RedirectResponse
from injector import inject
import requests

from src.core.settings.app_settings import AppSettings


class GithubAuthService:
    app_settings: AppSettings
    
    @inject
    def __init__(self, app_settings: AppSettings) -> None:
        self.app_settings = app_settings

    def login_user(self):
        return RedirectResponse(f'https://github.com/login/oauth/authorize?client_id={self.app_settings.github_client_id}')

    def handle_code(self, code: str) -> Dict[str, Any]:
        params = {
            'client_id'     : self.app_settings.github_client_id,
            'client_secret' : self.app_settings.github_client_secret,
            'code'          : code
        }
        print(params)
        headers = {'Accept': 'application/json'}
        response = requests.post(url='https://github.com/login/oauth/access_token', params=params, headers=headers).json()
        print(response)
        return response

    def get_user_info(self, token: str) -> Optional[Dict[str, Any]]:
        headers = {'Accept': 'application/json'}

        headers.update({'Authorization': f'Bearer {token}'})
        response = requests.get(url='https://api.github.com/user', headers=headers).json()
        if 'error' in response:
            return None
        return response
