"""
FastAPI 애플리케이션 엔트리포인트
"""
import uvicorn
from fastapi import FastAPI

from config.env import load_env
from kakao_authentication.controller import router as kakao_auth_router

# 환경 변수 로드 (애플리케이션 시작 시 1회 실행)
load_env()

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="Kakao Authentication API",
    description="Kakao OAuth 인증 API",
    version="1.0.0",
)

# 라우터 등록
app.include_router(kakao_auth_router)


@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {"message": "Kakao Authentication API"}


@app.get("/health")
async def health_check():
    """헬스 체크 엔드포인트"""
    return {"status": "healthy"}


if __name__ == "__main__":
    # 직접 실행 시 서버 시작
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
