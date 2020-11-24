from time import time

from fastapi import APIRouter, HTTPException

router = APIRouter()

startup = time()
delay = 15.0

@router.get("/api/healthz")
async def is_online():
  if time() - delay < startup:
    raise HTTPException(status_code=503, detail="App not ready")
  
  return "OK"
