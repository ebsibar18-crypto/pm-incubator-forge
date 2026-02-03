"""
Kakao 인증 서비스 구현체
"""
import os
from typing import Dict, Any
from urllib.parse import urlencode

import httpx

from config.env import get_env
from kakao_authentication.models import (
    AccessTokenResponse,
    KakaoUserInfo,
    OAuthLinkResponse,
    TokenWithUserInfoResponse,
)
from kakao_authentication.service_interface import KakaoAuthenticationServiceInterface


class KakaoAuthenticationService(KakaoAuthenticationServiceInterface):
    """Kakao 인증 서비스 구현체"""
    
    # Kakao OAuth 설정
    KAKAO_OAUTH_BASE_URL = "https://kauth.kakao.com"
    KAKAO_API_BASE_URL = "https://kapi.kakao.com"
    
    def __init__(self):
        """서비스 초기화 - 환경 변수에서 설정값 로드"""
        self.client_id = get_env("KAKAO_CLIENT_ID")
        self.redirect_uri = get_env("KAKAO_REDIRECT_URI")
        self.response_type = "code"  # OAuth 2.0 표준
    
    def generate_oauth_url(self) -> OAuthLinkResponse:
        """
        Kakao OAuth 인증 URL을 생성합니다.
        
        Returns:
            OAuthLinkResponse: 인증 URL이 포함된 응답
        
        Raises:
            ValueError: 필수 환경 변수가 설정되지 않은 경우
        """
        if not self.client_id:
            raise ValueError("KAKAO_CLIENT_ID 환경 변수가 설정되지 않았습니다.")
        
        if not self.redirect_uri:
            raise ValueError("KAKAO_REDIRECT_URI 환경 변수가 설정되지 않았습니다.")
        
        # Kakao OAuth 인증 URL 생성
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": self.response_type,
        }
        
        oauth_url = f"{self.KAKAO_OAUTH_BASE_URL}/oauth/authorize?{urlencode(params)}"
        
        return OAuthLinkResponse(oauth_url=oauth_url)
    
    def request_access_token(self, code: str) -> AccessTokenResponse:
        """
        인가 코드를 사용하여 액세스 토큰을 요청합니다.
        
        Args:
            code: Kakao 인증 후 받은 인가 코드
        
        Returns:
            AccessTokenResponse: 액세스 토큰 정보
        
        Raises:
            ValueError: 필수 파라미터가 누락된 경우
            Exception: Kakao API 요청 실패 시
        """
        if not code:
            raise ValueError("인가 코드(code)가 필요합니다.")
        
        if not self.client_id:
            raise ValueError("KAKAO_CLIENT_ID 환경 변수가 설정되지 않았습니다.")
        
        if not self.redirect_uri:
            raise ValueError("KAKAO_REDIRECT_URI 환경 변수가 설정되지 않았습니다.")
        
        # Kakao 토큰 요청
        token_url = f"{self.KAKAO_OAUTH_BASE_URL}/oauth/token"
        
        data = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "code": code,
        }
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        
        try:
            with httpx.Client() as client:
                response = client.post(token_url, data=data, headers=headers)
                response.raise_for_status()
                
                token_data: Dict[str, Any] = response.json()
                
                return AccessTokenResponse(
                    access_token=token_data["access_token"],
                    token_type=token_data.get("token_type", "bearer"),
                    refresh_token=token_data.get("refresh_token"),
                    expires_in=token_data.get("expires_in", 0),
                    scope=token_data.get("scope"),
                    refresh_token_expires_in=token_data.get("refresh_token_expires_in"),
                )
        except httpx.HTTPStatusError as e:
            error_detail = "알 수 없는 오류"
            try:
                error_data = e.response.json()
                error_detail = error_data.get("error_description", str(e))
            except:
                error_detail = str(e)
            
            raise Exception(f"액세스 토큰 요청 실패: {error_detail}")
        except httpx.RequestError as e:
            raise Exception(f"Kakao API 요청 중 오류 발생: {str(e)}")
    
    def get_user_info(self, access_token: str) -> KakaoUserInfo:
        """
        액세스 토큰을 사용하여 사용자 정보를 조회합니다.
        
        Args:
            access_token: Kakao 액세스 토큰
        
        Returns:
            KakaoUserInfo: 사용자 정보
        
        Raises:
            ValueError: 토큰이 유효하지 않은 경우
            Exception: Kakao API 요청 실패 시
        """
        if not access_token:
            raise ValueError("액세스 토큰이 필요합니다.")
        
        # Kakao 사용자 정보 조회 API
        user_info_url = f"{self.KAKAO_API_BASE_URL}/v2/user/me"
        
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        
        try:
            with httpx.Client() as client:
                response = client.get(user_info_url, headers=headers)
                response.raise_for_status()
                
                user_data: Dict[str, Any] = response.json()
                
                # Kakao API 응답 구조에 맞게 파싱
                kakao_account = user_data.get("kakao_account", {})
                properties = user_data.get("properties", {})
                
                return KakaoUserInfo(
                    id=user_data["id"],
                    nickname=properties.get("nickname"),
                    email=kakao_account.get("email"),
                    profile_image=properties.get("profile_image"),
                )
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise ValueError("액세스 토큰이 유효하지 않거나 만료되었습니다.")
            
            error_detail = "알 수 없는 오류"
            try:
                error_data = e.response.json()
                error_detail = error_data.get("msg", str(e))
            except:
                error_detail = str(e)
            
            raise Exception(f"사용자 정보 조회 실패: {error_detail}")
        except httpx.RequestError as e:
            raise Exception(f"Kakao API 요청 중 오류 발생: {str(e)}")
    
    def get_kakao_token(self, code: str) -> AccessTokenResponse:
        """인가 코드로 Kakao 액세스 토큰을 발급받습니다."""
        return self.request_access_token(code)

    def get_kakao_user_info(self, access_token: str) -> KakaoUserInfo:
        """액세스 토큰으로 Kakao 사용자 정보(닉네임, 이메일 등)를 가져옵니다."""
        return self.get_user_info(access_token)

    def request_access_token_with_user_info(self, code: str) -> TokenWithUserInfoResponse:
        """
        token = get_kakao_token(code) → user_info = get_kakao_user_info(token.access_token) → { token, user_info } 반환
        """
        token = self.get_kakao_token(code)
        user_info = self.get_kakao_user_info(token.access_token)
        return TokenWithUserInfoResponse(token=token, user_info=user_info)
