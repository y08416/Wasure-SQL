from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv  # 追加

# .envファイルを読み込む
load_dotenv()  # 追加

# データベースURLの設定（デフォルト値付き）
# envから取って
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./test.db')

# データベースエンジンの作成
engine = create_engine(DATABASE_URL)

# セッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラスの作成
Base = declarative_base()

# データベースセッションを取得する関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()