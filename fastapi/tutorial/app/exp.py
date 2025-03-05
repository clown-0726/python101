from fastapi import APIRouter, Path, Query, Form, File, UploadFile, HTTPException

router_exp = APIRouter()


@router_exp.get("/http_exception")
async def http_exception():
    raise HTTPException(status_code=404, detail="Not Found")
