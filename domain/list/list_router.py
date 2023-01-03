import uuid

from fastapi import APIRouter

from database import SessionLocal
from models import Todo

router = APIRouter()

@router.get("/list")
def todo_list():
    db = SessionLocal()
    _todo_list = db.query(Todo).order_by(Todo.order.asc()).all()
    db.close()
    return _todo_list