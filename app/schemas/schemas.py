from pydantic import BaseModel
from typing import List, Optional

# Activity
class ActivityBase(BaseModel):
    name: str
    description: Optional[str] = None
    location: Optional[str] = None

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int

    class Config:
        from_attributes = True

# Transfer
class TransferBase(BaseModel):
    description: str
    origin: Optional[str] = None
    destination: Optional[str] = None

class TransferCreate(TransferBase):
    pass

class Transfer(TransferBase):
    id: int

    class Config:
        from_attributes = True

# Hotel Accommodation
class HotelAccommodationBase(BaseModel):
    hotel_name: str
    address: Optional[str] = None

class HotelAccommodationCreate(HotelAccommodationBase):
    pass

class HotelAccommodation(HotelAccommodationBase):
    id: int

    class Config:
        from_attributes = True

# Day
class DayBase(BaseModel):
    day_number: int

class DayCreate(DayBase):
    hotel: HotelAccommodationCreate
    activities: List[ActivityCreate]
    transfers: List[TransferCreate]

class Day(DayBase):
    id: int
    hotel: Optional[HotelAccommodation] = None
    activities: List[Activity] = []
    transfers: List[Transfer] = []

    class Config:
        from_attributes = True

# Itinerary
class ItineraryBase(BaseModel):
    name: str
    description: Optional[str] = None
    duration_nights: int

class ItineraryCreate(ItineraryBase):
    days: List[DayCreate]

class Itinerary(ItineraryBase):
    id: int
    days: List[Day] = []

    class Config:
        from_attributes = True
