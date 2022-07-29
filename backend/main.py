from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.base import api_router
from db.session import engine
from db.base import Base 


def include_router(app):   #включение маршрутизаторов
	app.include_router(api_router)


def create_tables():	#создание таблиц
	print("create_tables")
	Base.metadata.create_all(bind=engine)

	
def start_application():	#запуск самого проекта
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	create_tables()
	return app

app = start_application()
