"""
Kakao 인증 서비스 인터페이스
Controller는 이 인터페이스에만 의존합니다.
"""
from abc import ABC, abstractmethod

from kakao_authentication.models import (
    AccessTokenResponse,
    KakaoUserInfo,
    OAuthLinkResponse,
    TokenWithUserInfoResponse,
)


class KakaoAuthenticationServiceInterface(ABC):
    """Kakao 인증 서비스 인터페이스"""
    
    @abstractmethod
    def generate_oauth_url(self) -> OAuthLinkResponse:
        """
        Kakao OAuth 인증 URL을 생성합니다.
        
        Returns:
            OAuthLinkResponse: 인증 URL이 포함된 응답
        
        Raises:
            ValueError: 필수 환경 변수가 설정되지 않은 경우
        """
        pass
    
    @abstractmethod
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
        pass
    
    @abstractmethod
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
        pass
    
    @abstractmethod
    def request_access_token_with_user_info(self, code: str) -> TokenWithUserInfoResponse:
        """
        인가 코드로 토큰 발급 후, 해당 토큰으로 유저 정보를 가져와 { token, user_info } 로 반환합니다.
        """
        pass
