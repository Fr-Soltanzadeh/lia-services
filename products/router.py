from fastapi import APIRouter, status, HTTPException


router = APIRouter(prefix="/products", tags=["Products"])
