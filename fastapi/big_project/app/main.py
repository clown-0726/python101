import uvicorn
from fastapi import FastAPI
from api.v1 import user as user_v1

app = FastAPI()

app.include_router(user_v1.router, prefix="/v1/users", tags=["Users", "v1"])

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=1)
