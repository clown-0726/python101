from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CityInfo(BaseModel):
    province: str
    continent: str
    is_affected: Optional[bool] = None


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


# 下面 city 参数是路径参数，query_string 是查询参数
@app.get("/city/{city}")
def city(city: str, q_str: Optional[str] = None):
    return {'city': city, 'query_string': q_str}


@app.put('/city/{city}')
def result(city: str, city_info: CityInfo):
    return {
        'city': city,
        'province': city_info.province,
        'continent': city_info.continent,
        'is_affected': city_info.is_affected
    }


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, workers=1)
