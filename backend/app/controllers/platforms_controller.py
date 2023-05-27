from sqlalchemy.orm import Session

from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import select

from datetime import datetime

from typing import Optional

import os

from app.models import Platforms, Metro, Industry, Photos, Equipments, Accessibilities, Facilities, \
    PlatformsMetro, PlatformsIndustry, PlatformsFacilities, PlatformsEquipments, PlatformsPhotos, \
    PlatformsAccessibilities, LandlordUsers, TenantUsers, PlatformsBusySlots, Bookings, BookingContracts, \
    Contracts, BookingsFacilities, BookingsAccessibilities, BookingsEquipments

from app.controllers.errors_controller import metro_not_create_exception, metro_exists_exception, \
    industry_exists_exception, industry_not_create_exception, equipment_exists_exception, \
    equipment_not_create_exception, \
    accessibility_exists_exception, accessibility_not_create_exception, \
    facility_exists_exception, facility_not_create_exception, platform_not_create_exception, \
    platform_not_exists_exception, time_slot_exists_exception, booking_not_create_exception


def get_landlord_id(db: Session, user_id: int):
    return db.scalars(select(LandlordUsers).where(LandlordUsers.user_id == user_id)).first().id


def get_tenant_id(db: Session, user_id: int):
    return db.scalars(select(TenantUsers).where(TenantUsers.user_id == user_id)).first().id


def create_metro(db: Session, title: str, color: str, branch: str):
    if db.scalars(select(Metro).where(Metro.title == title)).first():
        raise metro_exists_exception
    try:
        metro_station = Metro(
            title=title,
            color=color,
            branch=branch
        )
        db.add(metro_station)
        db.commit()
        return metro_station
    except SQLAlchemyError as e:
        print(e)
        raise metro_not_create_exception


def get_metro(db: Session):
    metro = db.scalars(select(Metro)).all()
    return metro


def create_industry(db: Session, title: str):
    if db.scalars(select(Industry).where(Industry.title == title)).first():
        raise industry_exists_exception
    try:
        industry = Industry(
            title=title
        )
        db.add(industry)
        db.commit()
        return industry
    except SQLAlchemyError as e:
        print(e)
        raise industry_not_create_exception


def get_industry(db: Session):
    industry = db.scalars(select(Industry)).all()
    return industry


def create_equipment(db: Session, title: str, price: int):
    if db.scalars(select(Equipments).where(Equipments.title == title)).first():
        raise equipment_exists_exception
    try:
        equipment = Equipments(
            title=title,
            price=price
        )
        db.add(equipment)
        db.commit()
        return equipment
    except SQLAlchemyError as e:
        print(e)
        raise equipment_not_create_exception


def get_equipments(db: Session):
    equipments = db.scalars(select(Equipments)).all()
    return equipments


def create_accessibilities(db: Session, title: str):
    if db.scalars(select(Accessibilities).where(Accessibilities.title == title)).first():
        raise accessibility_exists_exception
    try:
        accessibility = Accessibilities(
            title=title
        )
        db.add(accessibility)
        db.commit()
        return accessibility
    except SQLAlchemyError as e:
        print(e)
        raise accessibility_not_create_exception


def get_accessibilities(db: Session):
    accessibilities = db.scalars(select(Accessibilities)).all()
    return accessibilities


def create_facility(db: Session, title: str, price: int):
    if db.scalars(select(Facilities).where(Facilities.title == title)).first():
        raise facility_exists_exception
    try:
        facility = Facilities(
            title=title,
            price=price
        )
        db.add(facility)
        db.commit()
        return facility
    except SQLAlchemyError as e:
        print(e)
        raise facility_not_create_exception


def get_facilities(db: Session):
    facilities = db.scalars(select(Facilities)).all()
    return facilities


def platform_response(platform: Platforms):
    return {
        'platform_id': platform.id,
        'title': platform.title,
        'description': platform.description,
        'capacity': platform.capacity,
        'area': platform.area,
        'address': platform.address,
        'phone': platform.phone,
        'verified': platform.verified,
        'metro': [element.metro for element in platform.platforms_metro],
        'industry': [element.industry for element in platform.platforms_industry],
        'equipments': [element.equipments for element in platform.platforms_equipments],
        'accessibilities': [element.accesibilities for element in platform.platforms_accessibilities],
        'facilities': [element.facilities for element in platform.platforms_facilities],
        'photos': [
            f'/api/platforms/photo/{photo.photos.id}' for photo in platform.platforms_photos
        ]
    }


def booking_response(platform: Platforms,
                     booking: Bookings,
                     busy_slots: Optional[list[PlatformsBusySlots]] = None):
    # return {
    #     'platform_id': platform.id,
    #     'platform': platform_response(platform),
    #     'time_slot': busy_slot,
    #     'equipments': [element.equipments for element in booking.bookings_equipments],
    #     'accessibilities': [element.accesibilities for element in booking.bookings_accessibilities],
    #     'facilities': [element.facilities for element in booking.bookings_facilities],
    # }
    return {
        'booking_id': booking.id,
        'verified': booking.verified,
        'platform': platform_response(platform),
        'time_slots': [busy_slot for busy_slot in busy_slots] if busy_slots else [busy_slot for busy_slot in booking.time_slots],
        'equipments': [element.equipments for element in booking.bookings_equipments],
        'accessibilities': [element.accesibilities for element in booking.bookings_accessibilities],
        'facilities': [element.facilities for element in booking.bookings_facilities],
    }


def create_platform(db: Session,
                    photos: list[bytes],
                    user_id: int,
                    title: str,
                    description: str,
                    capacity: int,
                    area: int,
                    phone: str,
                    address: str,
                    metro_ids: list[int],
                    industry_ids: list[int],
                    equipments_ids: list[int],
                    accessibilities_ids: list[int],
                    facilities_ids: list[int]):
    try:
        landlord_id = get_landlord_id(db, user_id)
        platform = Platforms(
            title=title,
            description=description,
            capacity=capacity,
            area=area,
            address=address,
            phone=phone,
            landlord_id=landlord_id,
            verified=False
        )
        db.add(platform)
        db.commit()

        for metro_id in metro_ids:
            db.add(PlatformsMetro(
                platform_id=platform.id,
                metro_id=metro_id
            ))
        for industry_id in industry_ids:
            db.add(PlatformsIndustry(
                platform_id=platform.id,
                industry_id=industry_id
            ))
        if equipments_ids:
            for equipment_id in equipments_ids:
                db.add(PlatformsEquipments(
                    platform_id=platform.id,
                    equipment_id=equipment_id
                ))
        if accessibilities_ids:
            for accessibility_id in accessibilities_ids:
                db.add(PlatformsAccessibilities(
                    platform_id=platform.id,
                    accessibility_id=accessibility_id
                ))
        if facilities_ids:
            for facility_id in facilities_ids:
                db.add(PlatformsFacilities(
                    platform_id=platform.id,
                    facility_id=facility_id
                ))
        db.commit()
        for n, photo in enumerate(photos, 1):
            photo_path = os.path.join(os.getcwd(), 'data', f'platform_{platform.id}_{n}.jpg')
            new_photo = Photos(src=photo_path)
            db.add(new_photo)
            db.commit()
            db.add(PlatformsPhotos(
                platform_id=platform.id,
                photo_id=new_photo.id
            ))
            with open(photo_path, 'wb') as file:
                file.write(photo)
        db.commit()

        return platform_response(platform)
    except SQLAlchemyError as e:
        print(e)
        db.rollback()
        raise platform_not_create_exception


# Метод просмотра созданных площадок пользователем арендодателем
def get_platforms_landlord(db: Session, user_id: int):
    landlord_id = get_landlord_id(db, user_id)
    platforms = db.scalars(select(Platforms).where(Platforms.landlord_id == landlord_id)).all()
    resp = []
    for platform in platforms:
        resp.append(platform_response(platform))
    return resp


# Метод админа для подтверждения площадки
def verify_platform(db: Session, platform_id: int):
    platform = db.scalars(select(Platforms).where(Platforms.id == platform_id)).one()
    print(type(platform))
    if not platform:
        raise platform_not_exists_exception
    platform.verified = True
    db.commit()
    return platform_response(platform)


# Метод для получения площадок при поиске
def get_platforms_search(db: Session):
    resp = []
    platforms = db.scalars(select(Platforms).\
                           where(Platforms.verified == True)
                           ).all()
    for platform in platforms:
        resp.append(platform_response(platform))
    return resp


def get_platforms_photo(db: Session, photo_id: int):
    photo = db.scalars(select(Photos).where(Photos.id == photo_id)).first()
    with open(photo.src, 'rb') as file:
        return file.read()


# def create_platform_time_slot(db: Session, platform_id: int, from_date: s)


# Метод оформления брони на площадку
def create_platform_booking(db: Session,
                            user_id: int,
                            platform_id: int,
                            from_date: str,
                            to_date: str,
                            equipments_ids: list[int],
                            accessibilities_ids: list[int],
                            facilities_ids: list[int]):
    tenant_id = get_tenant_id(db, user_id)
    platform = db.scalars(select(Platforms).where(Platforms.id == platform_id)).first()
    if not platform:
        raise platform_not_exists_exception
    landlord_id = platform.landlord_id
    date_format = '%d.%m.%Y'
    from_date_datetime = datetime.strptime(from_date, date_format)
    to_date_datetime = datetime.strptime(to_date, date_format)
    try:
        if db.scalars(
                select(PlatformsBusySlots). \
                        where(PlatformsBusySlots.platform_id == platform_id). \
                        where(PlatformsBusySlots.from_time == from_date_datetime). \
                        where(PlatformsBusySlots.to_time == to_date_datetime)
        ).first():
            raise time_slot_exists_exception
        busy_slot = PlatformsBusySlots(
            platform_id=platform_id,
            from_time=from_date_datetime,
            to_time=to_date_datetime
        )
        db.add(busy_slot)
        db.commit()

        booking = Bookings(
            paid=False,
            tenant_id=tenant_id,
            landlord_id=landlord_id,
            platform_id=platform_id,
            time_slot_id=busy_slot.id
        )
        db.add(booking)
        db.commit()

        if equipments_ids:
            for equipment_id in equipments_ids:
                db.add(BookingsEquipments(
                    booking_id=booking.id,
                    equipment_id=equipment_id
                ))
        if accessibilities_ids:
            for accessibility_id in accessibilities_ids:
                db.add(BookingsAccessibilities(
                    booking_id=booking.id,
                    accessibility_id=accessibility_id
                ))
        if facilities_ids:
            for facility_id in facilities_ids:
                db.add(BookingsFacilities(
                    booking_id=booking.id,
                    facility_id=facility_id
                ))
        db.commit()

        return booking_response(platform, busy_slot, booking)

    except SQLAlchemyError as e:
        print(e)
        raise booking_not_create_exception


def get_platform_bookings_landlord(db: Session, user_id: int):
    landlord_id = get_landlord_id(db, user_id)
    bookings = db.scalars(select(Bookings).where(Bookings.landlord_id == landlord_id)).all()
    resp = []
    for booking in bookings:
        resp.append(booking_response(booking.platforms, booking))
    return resp


# Метод для получения площадок, которые арендовал арендатор
def get_platforms_tenant(db: Session, user_id: int):
    tenant_id = get_tenant_id(db, user_id)
    # TODO доделать когда будут готовы брони
    pass
