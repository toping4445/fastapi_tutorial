from datetime import datetime

from fastapi import APIRouter
from starlette.responses import Response
from starlette.requests import Request
from inspect import currentframe as frame

from app.database.schema import Users
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.conn import db

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session),):
    """
    ELB 상태 체크용 API
    :return:
    """

    users = Users(status="active",name="helloworld")
    session.add(users)
    session.commit()

    Users().create(session,auto_commit=True,name="코알라")

    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")




@router.get("/test")
async def test(request: Request):
    """
    ELB 상태 체크용 API
    :return:
    """
    print("state.user", request.state.user)
    try:
        a = 1/0
    except Exception as e:
        request.state.inspect = frame()
        raise e
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
