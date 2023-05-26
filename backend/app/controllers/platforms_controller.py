from sqlalchemy.orm import Session

from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import select

import os

from app.models import Platforms, Metro, Industry, Photos, Equipments, Accessibilities, Facilities, \
    PlatformsMetro, PlatformsIndustry, PlatformsFacilities, PlatformsEquipments, PlatformsPhotos, \
    PlatformsAccessibilities, LandlordUsers

from app.controllers.errors_controller import metro_not_create_exception, metro_exists_exception, \
    industry_exists_exception, industry_not_create_exception, equipment_exists_exception, equipment_not_create_exception, \
    accessibility_exists_exception, accessibility_not_create_exception, \
    facility_exists_exception, facility_not_create_exception, platform_not_create_exception


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
        landlord_id = db.scalars(select(LandlordUsers).where(LandlordUsers.user_id == user_id)).first().id
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
        for equipment_id in equipments_ids:
            db.add(PlatformsEquipments(
                platform_id=platform.id,
                equipment_id=equipment_id
            ))
        for accessibility_id in accessibilities_ids:
            db.add(PlatformsAccessibilities(
                platform_id=platform.id,
                accessibility_id=accessibility_id
            ))
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

        return {
            'platform_id': platform.id,
            'title': platform.title,
            'description': platform.description,
            'capacity': platform.capacity,
            'area': platform.area,
            'address': platform.address,
            'phone': platform.phone,
            'metro': [element.metro for element in platform.platforms_metro],
            'industry': [element.industry for element in platform.platforms_industry],
            'equipments': [element.equipments for element in platform.platforms_equipments],
            'accessibilitie': [element.accesibilities for element in platform.platforms_accessibilities],
            'facilities': [element.facilities for element in platform.platforms_facilities]
        }
    except SQLAlchemyError as e:
        print(e)
        db.rollback()
        raise platform_not_create_exception


def get_platforms_landlord(db: Session, user_id: int):
    landlord_id = db.scalars(select(LandlordUsers).where(LandlordUsers.user_id == user_id)).first().id
    platforms = db.scalars(select(Platforms).where(Platforms.landlord_id == landlord_id)).all()
    resp = []
    for platform in platforms:
        resp.append({
            'platform_id': platform.id,
            'title': platform.title,
            'description': platform.description,
            'capacity': platform.capacity,
            'area': platform.area,
            'address': platform.address,
            'phone': platform.phone,
            'metro': [element.metro for element in platform.platforms_metro],
            'industry': [element.industry for element in platform.platforms_industry],
            'equipments': [element.equipments for element in platform.platforms_equipments],
            'accessibilitie': [element.accesibilities for element in platform.platforms_accessibilities],
            'facilities': [element.facilities for element in platform.platforms_facilities]
        })
    return resp
