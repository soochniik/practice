from apis.version1 import route_articles
from apis.version1 import route_login
from apis.version1 import route_users
from apis.version1 import route_com
from apis.version1 import route_reasons
from apis.version1 import route_eval
from apis.version1 import route_themes
from apis.version1 import route_search
from apis.version1 import route_admin
from apis.version1 import route_authors

from fastapi import APIRouter


api_router = APIRouter()    #информация о всех маршрутизаторах
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_admin.router, prefix="/admin", tags=["admin"])
api_router.include_router(route_search.router, prefix="/search", tags=["serch"])
api_router.include_router(route_authors.router, prefix="/authors", tags=["authors"])
api_router.include_router(route_articles.router, prefix="/articles", tags=["articles"])
api_router.include_router(route_themes.router, prefix="/themes", tags=["themes"])
api_router.include_router(route_eval.router, prefix="/evaluations", tags=["evaluations"])
api_router.include_router(route_com.router, prefix="/comments", tags=["comments"])
api_router.include_router(route_reasons.router, prefix="/reasons", tags=["reasons"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
