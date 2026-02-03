"""
Kakao 인증 관련 데이터 모델
"""
from typing import Optional

from pydantic import BaseModel, Field


class OAuthLinkResponse(BaseModel):
    """OAuth 인증 URL 응답 모델"""
    oauth_url: str = Field(..., description="Kakao OAuth 인증 URL")


class AccessTokenRequest(BaseModel):
    """액세스 토큰 요청 모델"""
    code: str = Field(..., description="Kakao 인증 후 받은 인가 코드")


class AccessTokenResponse(BaseModel):
    """액세스 토큰 응답 모델"""
    access_token: str = Field(..., description="액세스 토큰")
    token_type: str = Field(..., description="토큰 타입 (보통 'bearer')")
    refresh_token: Optional[str] = Field(None, description="리프레시 토큰")
    expires_in: int = Field(..., description="토큰 만료 시간 (초)")
    scope: Optional[str] = Field(None, description="토큰 스코프")
    refresh_token_expires_in: Optional[int] = Field(None, description="리프레시 토큰 만료 시간 (초)")


class KakaoUserInfo(BaseModel):
    """Kakao 사용자 정보 모델"""
    id: int = Field(..., description="Kakao 사용자 ID")
    nickname: Optional[str] = Field(None, description="닉네임")
    email: Optional[str] = Field(None, description="이메일")
    profile_image: Optional[str] = Field(None, description="프로필 이미지 URL")


class AccessTokenWithUserInfoResponse(BaseModel):
    """액세스 토큰과 사용자 정보를 포함한 응답 모델"""
    access_token: str = Field(..., description="액세스 토큰")
    token_type: str = Field(..., description="토큰 타입")
    refresh_token: Optional[str] = Field(None, description="리프레시 토큰")
    expires_in: int = Field(..., description="토큰 만료 시간 (초)")
    user_info: KakaoUserInfo = Field(..., description="Kakao 사용자 정보")


class TokenWithUserInfoResponse(BaseModel):
    """token + user_info 합쳐서 반환하는 응답 모델"""
    token: AccessTokenResponse = Field(..., description="get_kakao_token 결과")
    user_info: KakaoUserInfo = Field(..., description="get_kakao_user_info 결과")
