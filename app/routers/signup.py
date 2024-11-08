from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db 
from app.models import User
from app.utils import get_password_hash


router = APIRouter()

@router.post("/signup")
async def signup(user_id: str, email: str, password: str, username: str, occupation: str, fcm_token: str, db: Session = Depends(get_db)):
    # Emailが既に登録されているかチェック
    db_user = db.query(User).filter(User.email == email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # パスワードをハッシュ化して保存
    hashed_password = get_password_hash(password)
    new_user = User(
        user_id=user_id,
        email=email,
        username=username,
        hashed_password=hashed_password,
        occupation=occupation,
        fcm_token=fcm_token
    )

    # データベースに新規ユーザーを追加
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}
