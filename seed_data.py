from app.database import SessionLocal
from app.models import models

def seed_database():
    db = SessionLocal()

    # -------- Phuket 3 Nights Itinerary --------
    phuket_trip = models.Itinerary(
        name="Phuket 3 Nights Getaway",
        description="Explore the stunning beaches of Phuket in 3 nights.",
        duration_nights=3
    )
    db.add(phuket_trip)
    db.commit()
    db.refresh(phuket_trip)

    day1 = models.Day(day_number=1, itinerary_id=phuket_trip.id)
    db.add(day1)
    db.commit()
    db.refresh(day1)

    db.add(models.HotelAccommodation(
        hotel_name="Holiday Inn Resort Phuket",
        address="Patong Beach, Phuket",
        day_id=day1.id
    ))

    db.add(models.Activity(
        name="Arrival and Relaxation",
        description="Check-in and relax at the beach.",
        day_id=day1.id
    ))
    
    db.add(models.Transfer(
        description="Airport pickup and transfer to hotel",
        origin="Phuket Airport",
        destination="Holiday Inn Resort",
        day_id=day1.id
    ))

    day2 = models.Day(day_number=2, itinerary_id=phuket_trip.id)
    db.add(day2)
    db.commit()
    db.refresh(day2)

    db.add(models.Activity(
        name="Phi Phi Island Tour",
        description="Full-day speedboat tour to Phi Phi Islands with snorkeling.",
        day_id=day2.id
    ))

    day3 = models.Day(day_number=3, itinerary_id=phuket_trip.id)
    db.add(day3)
    db.commit()
    db.refresh(day3)

    db.add(models.Activity(
        name="Old Phuket Town Exploration",
        description="Explore heritage sites and local markets in Phuket town.",
        day_id=day3.id
    ))

    db.add(models.Transfer(
        description="Hotel checkout and airport transfer",
        origin="Holiday Inn Resort",
        destination="Phuket Airport",
        day_id=day3.id
    ))

    # -------- Krabi 5 Nights Itinerary --------
    krabi_trip = models.Itinerary(
        name="Krabi 5 Nights Adventure",
        description="Adventure-packed 5 nights trip across Krabi's stunning nature spots.",
        duration_nights=5
    )
    db.add(krabi_trip)
    db.commit()
    db.refresh(krabi_trip)

    for i in range(1, 6):
        day = models.Day(day_number=i, itinerary_id=krabi_trip.id)
        db.add(day)
        db.commit()
        db.refresh(day)

        db.add(models.HotelAccommodation(
            hotel_name="Rayavadee Resort",
            address="Railay Beach, Krabi",
            day_id=day.id
        ))

        db.add(models.Activity(
            name=f"Day {i} Activity",
            description=f"Exciting adventure on day {i} in Krabi!",
            day_id=day.id
        ))

    # -------- Short Phuket 2 Nights Itinerary --------
    short_phuket_trip = models.Itinerary(
        name="Short Phuket 2 Nights",
        description="Quick trip to Phuket for 2 nights.",
        duration_nights=2
    )
    db.add(short_phuket_trip)
    db.commit()
    db.refresh(short_phuket_trip)

    for i in range(1, 3):
        day = models.Day(day_number=i, itinerary_id=short_phuket_trip.id)
        db.add(day)
        db.commit()
        db.refresh(day)

        db.add(models.HotelAccommodation(
            hotel_name="The Charm Resort Phuket",
            address="Patong, Phuket",
            day_id=day.id
        ))

        db.add(models.Activity(
            name=f"Relaxation Day {i}",
            description=f"Enjoy relaxing activities on day {i}.",
            day_id=day.id
        ))

    # -------- Krabi 8 Nights Itinerary --------
    krabi_long_trip = models.Itinerary(
        name="Krabi 8 Nights Long Stay",
        description="Leisurely stay to enjoy everything Krabi offers.",
        duration_nights=8
    )
    db.add(krabi_long_trip)
    db.commit()
    db.refresh(krabi_long_trip)

    for i in range(1, 9):
        day = models.Day(day_number=i, itinerary_id=krabi_long_trip.id)
        db.add(day)
        db.commit()
        db.refresh(day)

        db.add(models.HotelAccommodation(
            hotel_name="Centara Grand Beach Resort & Villas Krabi",
            address="Ao Nang Beach, Krabi",
            day_id=day.id
        ))

        db.add(models.Activity(
            name=f"Relax/Adventure Day {i}",
            description=f"Mixture of beach relaxation and tours on day {i}.",
            day_id=day.id
        ))

    # Finish and commit
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_database()
    print("Database seeded successfully!")
