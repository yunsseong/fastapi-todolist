from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#데이터베이스 접속 주소
SQLALCHEMY_DATA_BASE_URL = "sqlite:///./todolist.db"

#커넥션 풀 생성
engine = create_engine(
    SQLALCHEMY_DATA_BASE_URL, connect_args={"check_same_thread": False}
)

#세션 객체 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#데이터베이스 모델 구성에 사용
Base = declarative_base()