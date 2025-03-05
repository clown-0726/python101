import time
import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException, RequestValidationError
from starlette.responses import JSONResponse

from app import router_params, router_header, router_di, router_resp, router_exp

app = FastAPI(
    title="Tutorial",
    description="A tutorial app",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


# 重写异常类的放回格式
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse({"message": exc.detail}, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse({"message": str(exc)}, status_code=400)


# 使用中间件
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)  # 添加自定义的以“X-”开头的响应头
    return response


app.include_router(router_params, prefix="/params", tags=["Params test"])
app.include_router(router_resp, prefix="/resp", tags=["Resp test"])
app.include_router(router_header, prefix="/header", tags=["Header data test"])
app.include_router(router_di, prefix="/di", tags=["Dependence injection"])
app.include_router(router_exp, prefix="/exp", tags=["Exception handling"])


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=1)
