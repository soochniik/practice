from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from schemas.eval import EvaluationCreate, EvaluationUpdate
from db.models.eval import Evaluation
from db.models.articles import Article


def create_evaluation(evaluation: EvaluationCreate, db: Session, user:int):     #функция для добавления в бд новой оценки указанной статьи
    evaluation_object = Evaluation(**evaluation.dict(), user=user)
    article1 = evaluation_object.article
    db.add(evaluation_object)
    db.commit()
    db.refresh(evaluation_object)
    avg_eval = str(db.query(Evaluation).with_entities(func.avg(Evaluation.evaluation)).filter(Evaluation.article == article1).first())
    avg_eval=avg_eval.replace('(', '')
    avg_eval=avg_eval.replace(',)', '')
    eval_article = db.query(Article).filter(Article.id == article1).first()
    avg_eval = float(avg_eval)
    eval_article.eval = float("{0:.2f}".format(avg_eval))   #обновление в бд средней оценки статьи
    db.commit()
    return evaluation_object


def retreive_evaluation(id:int,db:Session):     #функция для возвращения конкретной оценки (указав id)
    item = db.query(Evaluation).filter(Evaluation.id == id).first()
    return item


def list_evaluations(article:int, db:Session):      #функция для возвращения всех оценок указанной статьи
    item = list(db.query(Evaluation).filter(Evaluation.article == article))
    return item


def update_eval(id:int, evaluation: EvaluationUpdate,db: Session,user):     #функция для обновления конкретной оценки (указав id)
    existing = db.query(Evaluation).filter(Evaluation.id == id)
    if not existing.first():
        return 0
    evaluation.__dict__.update(user=user)
    existing.update(evaluation.__dict__)
    db.commit()
    return 1


def delete_eval(id: int,db: Session,user):  #функция для удаления конкретной оценки (указав id)
    existing = db.query(Evaluation).filter(Evaluation.id == id)
    if not existing.first():
        return 0
    existing.delete(synchronize_session=False)
    db.commit()
    return 1
