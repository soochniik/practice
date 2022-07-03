from sqlalchemy.orm import Session

from schemas.eval import EvaluationCreate
from db.models.eval import Evaluation


def leave_evaluation(evaluation: EvaluationCreate,db: Session,user):
    evaluation_object = Evaluation(**evaluation.dict(),user=user)
    db.add(evaluation_object)
    db.commit()
    db.refresh(evaluation_object)
    return evaluation_object


def list_evaluations(article:int, db:Session):
    item = list(db.query(Evaluation).filter(Evaluation.article == article))
    return item
