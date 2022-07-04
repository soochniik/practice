from sqlalchemy.orm import Session

from schemas.eval import EvaluationCreate, EvaluationUpdate
from db.models.eval import Evaluation


def create_evaluation(evaluation: EvaluationCreate, db: Session, user:int):
    evaluation_object = Evaluation(**evaluation.dict(), user=user)
    db.add(evaluation_object)
    db.commit()
    db.refresh(evaluation_object)
    return evaluation_object


def retreive_evaluation(id:int,db:Session):
    item = db.query(Evaluation).filter(Evaluation.id == id).first()
    return item


def list_evaluations(article:int, db:Session):
    item = list(db.query(Evaluation).filter(Evaluation.article == article))
    return item


def update_eval(id:int, evaluation: EvaluationUpdate,db: Session,user):
    existing = db.query(Evaluation).filter(Evaluation.id == id)
    if not existing.first():
        return 0
    evaluation.__dict__.update(user=user)
    existing.update(evaluation.__dict__)
    db.commit()
    return 1


def delete_eval(id: int,db: Session,user):
    existing = db.query(Evaluation).filter(Evaluation.id == id)
    if not existing.first():
        return 0
    existing.delete(synchronize_session=False)
    db.commit()
    return 1
