"""
Kakao 인증 컨트롤러
FastAPI 엔드포인트를 정의합니다.
"""
from fastapi import APIRouter, Depends, HTTPException, Query

from kakao_authentication.models import (
    AccessTokenRequest,
    AccessTokenResponse,
    OAuthLinkResponse,
    TokenWithUserInfoResponse,
)
from kakao_authentication.service_interface import KakaoAuthenticationServiceInterface
from kakao_authentication.service_impl import KakaoAuthenticationService

router = APIRouter(prefix="/kakao-authentication", tags=["kakao-authentication"])


def get_service() -> KakaoAuthenticationServiceInterface:
    """
    서비스 인스턴스를 반환합니다 (FastAPI 의존성 주입).
    환경 변수가 로드된 후에만 서비스가 생성됩니다.
    """
    return KakaoAuthenticationService()


@router.get("/request-oauth-link", response_model=OAuthLinkResponse)
async def request_oauth_link(
    service: KakaoAuthenticationServiceInterface = Depends(get_service)
) -> OAuthLinkResponse:
    """
    Kakao OAuth 인증 URL을 생성합니다.
    
    Returns:
        OAuthLinkResponse: 인증 URL이 포함된 응답
    
    Raises:
        HTTPException: 환경 변수 누락 또는 URL 생성 실패 시
    """
    try:
        return service.generate_oauth_url()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"인증 URL 생성 실패: {str(e)}")


@router.get("/request-access-token-after-redirection", response_model=AccessTokenResponse)
async def request_access_token_after_redirection(
    code: str = Query(..., description="Kakao 인증 후 받은 인가 코드"),
    service: KakaoAuthenticationServiceInterface = Depends(get_service)
) -> AccessTokenResponse:
    """
    인가 코드를 받아 Kakao 액세스 토큰을 요청합니다.
    
    Args:
        code: Kakao 인증 후 받은 인가 코드
    
    Returns:
        AccessTokenResponse: 액세스 토큰 정보
    
    Raises:
        HTTPException: 파라미터 누락 또는 토큰 요청 실패 시
    """
    try:
        return service.request_access_token(code)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/request-access-token-with-user-info", response_model=TokenWithUserInfoResponse)
async def request_access_token_with_user_info(
    code: str = Query(..., description="Kakao 인증 후 받은 인가 코드"),
    service: KakaoAuthenticationServiceInterface = Depends(get_service)
) -> TokenWithUserInfoResponse:
    """
    token = get_kakao_token(code), user_info = get_kakao_user_info(token.access_token) 후
    return {"token": token, "user_info": user_info} 형태로 반환합니다.
    """
    try:
        return service.request_access_token_with_user_info(code)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
