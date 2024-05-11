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

    def get_user_info(self, code):
        params = {
            'client_id'     : self.app_settings.github_client_id,
            'client_secret' : self.app_settings.github_client_secret,
            'code'          : code
        }
        headers = {'Accept': 'application/json'}
        response = requests.post(url='https://github.com/login/oauth/access_token', params=params, headers=headers).json()

        if 'access_token' in response:
            access_token = response['access_token']
            headers.update({'Authorization': f'Bearer {access_token}'})
            response = requests.get(url='https://api.github.com/user', headers=headers).json()
        
        return response
