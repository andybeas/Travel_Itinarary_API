from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal, engine
from app.models import models
from app.schemas.schemas import Itinerary, ItineraryCreate
from app.crud import crud


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Travel Itinerary Management API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/itineraries/", response_model=Itinerary)
def create_itinerary(itinerary: ItineraryCreate, db: Session = Depends(get_db)):
    return crud.create_itinerary(db=db, itinerary=itinerary)

@app.get("/itineraries/", response_model=List[Itinerary])
def read_itineraries(db: Session = Depends(get_db)):
    return crud.get_itineraries(db=db)

@app.get("/recommendation/", response_model=List[Itinerary])
def recommend_itinerary(nights: int, db: Session = Depends(get_db)):
    itineraries = crud.get_recommendation(db=db, nights=nights)
    if not itineraries:
        raise HTTPException(status_code=404, detail="No itineraries found for given number of nights")
    return itineraries
