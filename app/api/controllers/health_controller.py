from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/api/healthz")
async def is_online():
  # TODO: implement healthcheck
  raise HTTPException(status_code=501)
