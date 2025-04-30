from sqlalchemy.orm import Session
from app.models import models
from app.schemas.schemas import Itinerary, ItineraryCreate


def create_itinerary(db: Session, itinerary: ItineraryCreate):
    db_itinerary = models.Itinerary(
        name=itinerary.name,
        description=itinerary.description,
        duration_nights=itinerary.duration_nights
    )
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)

    for day_data in itinerary.days:
        day = models.Day(
            day_number=day_data.day_number,
            itinerary_id=db_itinerary.id
        )
        db.add(day)
        db.commit()
        db.refresh(day)

        hotel = models.HotelAccommodation(
            hotel_name=day_data.hotel.hotel_name,
            address=day_data.hotel.address,
            day_id=day.id
        )
        db.add(hotel)

        for activity_data in day_data.activities:
            activity = models.Activity(
                name=activity_data.name,
                description=activity_data.description,
                location=activity_data.location,
                day_id=day.id
            )
            db.add(activity)

        for transfer_data in day_data.transfers:
            transfer = models.Transfer(
                description=transfer_data.description,
                origin=transfer_data.origin,
                destination=transfer_data.destination,
                day_id=day.id
            )
            db.add(transfer)

        db.commit()

    return db_itinerary

def get_itineraries(db: Session):
    return db.query(models.Itinerary).all()

def get_recommendation(db: Session, nights: int):
    return db.query(models.Itinerary).filter(models.Itinerary.duration_nights == nights).all()
