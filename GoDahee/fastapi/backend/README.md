# Kakao Authentication FastAPI Backend

Kakao OAuth 인증을 위한 FastAPI 백엔드 애플리케이션입니다.

## 기능

- **PM-EDDI-1**: 환경 변수 로딩을 위한 config/env 초기화
- **PM-EDDI-2**: Kakao 인증 URL 생성
- **PM-EDDI-3**: 인가 코드로 액세스 토큰 요청
- **PM-EDDI-4**: 액세스 토큰으로 사용자 정보 조회

## 설치 및 실행

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env.example` 파일을 참고하여 `.env` 파일을 생성하고 필요한 값들을 설정하세요:

```bash
cp .env.example .env
```

`.env` 파일에 다음 값들을 설정해야 합니다:
- `KAKAO_CLIENT_ID`: Kakao 개발자 콘솔에서 발급받은 Client ID
- `KAKAO_REDIRECT_URI`: Kakao 인증 후 리다이렉트될 URI

### 3. 애플리케이션 실행

```bash
uvicorn main:app --reload
```

애플리케이션은 기본적으로 `http://localhost:8000`에서 실행됩니다.

## API 엔드포인트

### 1. Kakao OAuth 인증 URL 생성

```
GET /kakao-authentication/request-oauth-link
```

**응답:**
```json
{
  "oauth_url": "https://kauth.kakao.com/oauth/authorize?..."
}
```

### 2. 액세스 토큰 요청

```
GET /kakao-authentication/request-access-token-after-redirection?code={인가코드}
```

**응답:**
```json
{
  "access_token": "...",
  "token_type": "bearer",
  "refresh_token": "...",
  "expires_in": 21599,
  "scope": "...",
  "refresh_token_expires_in": 5183999
}
```

### 3. 액세스 토큰 및 사용자 정보 요청 (통합)

```
GET /kakao-authentication/request-access-token-with-user-info?code={인가코드}
```

**응답:**
```json
{
  "access_token": "...",
  "token_type": "bearer",
  "refresh_token": "...",
  "expires_in": 21599,
  "user_info": {
    "id": 123456789,
    "nickname": "사용자닉네임",
    "email": "user@example.com",
    "profile_image": "https://..."
  }
}
```

## 아키텍처

이 프로젝트는 Layered Architecture를 따릅니다:

- **Controller**: API 엔드포인트 정의 및 요청/응답 처리
- **Service Interface**: 서비스 계약 정의 (추상 클래스)
- **Service Implementation**: 서비스 로직 구현
- **Models**: 데이터 모델 정의 (Pydantic)

Controller는 Service Interface에만 의존하며, 구현체에 직접 의존하지 않습니다.

## 프로젝트 구조

```
backend/
├── config/
│   ├── __init__.py
│   └── env.py              # 환경 변수 로딩
├── kakao_authentication/
│   ├── __init__.py
│   ├── controller.py        # API 엔드포인트
│   ├── service_interface.py # 서비스 인터페이스
│   ├── service_impl.py      # 서비스 구현체
│   └── models.py            # 데이터 모델
├── strategy/
│   ├── config/
│   │   └── PM-EDDI-1.yaml
│   └── kakao_authentication/
│       ├── PM-EDDI-2.yaml
│       ├── PM-EDDI-3.yaml
│       └── PM-EDDI-4.yaml
├── main.py                  # 애플리케이션 엔트리포인트
├── requirements.txt
├── .env.example
└── README.md
```
