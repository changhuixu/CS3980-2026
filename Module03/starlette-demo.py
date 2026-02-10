from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse


async def homepage(request):
    return JSONResponse({"hello": "world"})


async def hi(request):
    return JSONResponse({"hi": "world"})


app = Starlette(routes=[Route("/", homepage), Route("/hi", hi)])
