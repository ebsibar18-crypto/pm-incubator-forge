"""
환경 변수 로딩 모듈
애플리케이션 시작 시 .env 파일을 로드합니다.
"""
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


def load_env(env_file: Optional[str] = None) -> None:
    """
    환경 변수를 로드합니다.
    .env 파일이 없어도 애플리케이션은 시작되며, 경고만 출력합니다.
    
    Args:
        env_file: 로드할 .env 파일 경로. None인 경우 프로젝트 루트의 .env 파일을 찾습니다.
    """
    if env_file is None:
        # 프로젝트 루트 디렉토리 찾기 (backend 폴더)
        current_dir = Path(__file__).parent.parent
        env_file = current_dir / ".env"
    
    env_path = Path(env_file)
    
    if not env_path.exists():
        # .env 파일이 없어도 조용히 진행 (시스템 환경 변수 사용 가능)
        # 개발 환경에서는 .env 파일을 생성하는 것을 권장하지만, 필수는 아님
        return
    
    load_dotenv(env_path, override=False)


def get_env(key: str, default: Optional[str] = None) -> str:
    """
    환경 변수 값을 가져옵니다.
    
    Args:
        key: 환경 변수 키
        default: 기본값 (환경 변수가 없을 경우)
    
    Returns:
        환경 변수 값
    
    Raises:
        ValueError: 환경 변수가 없고 기본값도 없는 경우
    """
    value = os.getenv(key, default)
    
    if value is None:
        raise ValueError(f"환경 변수 '{key}'가 설정되지 않았습니다.")
    
    return value
