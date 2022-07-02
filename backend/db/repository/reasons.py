from sqlalchemy.orm import Session

from schemas.reasons import ReasonCreate
from db.models.reasons import Reason


def create_new_reason(reason: ReasonCreate,db: Session,user:int):
    reason_object = Reason(**reason.dict(),user=user)
    db.add(reason_object)
    db.commit()
    db.refresh(reason_object)
    return reason_object


def list_reason(article:int, db:Session):
    item = list(db.query(Reason).filter(Reason.article == article))
    return item
