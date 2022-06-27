from webapps.articles import route_articles
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_articles.router, prefix="", tags=["article-webapp"])