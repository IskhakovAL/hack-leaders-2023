from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Form, File

from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session

from io import BytesIO

from app.dependecies import get_db, RoleChecker

from app.schemas import Token, TokenData, Metro, Industry, Equipments, Accessibilities, Facilities, Platform, \
    Bookings

from app.controllers.security_controller import get_current_user

from app.controllers.platforms_controller import create_metro, get_metro, create_equipment, get_equipments, \
    create_industry, get_industry, create_facility, get_facilities, create_accessibilities, get_accessibilities, \
    create_platform, get_platforms_landlord, verify_platform, get_platforms_search, get_platforms_photo

platforms = APIRouter(
    prefix='/api/platforms',
    tags=['platforms']
)

all_roles = RoleChecker(['tenant', 'landlord', 'admin'])
admin_role = RoleChecker(['admin'])
landlord_role = RoleChecker(['landlord'])
tenant_role = RoleChecker(['tenant'])


@platforms.post('/metro', response_model=Metro, dependencies=[Depends(admin_role)])
def api_create_metro(db: Annotated[Session, Depends(get_db)],
                     current_user: Annotated[TokenData, Depends(get_current_user)],
                     title: Annotated[str, Form()], color: Annotated[str, Form()],
                     branch: Annotated[str, Form()]):
    try:
        return create_metro(db, title, color, branch)
    except HTTPException as e:
        raise e


@platforms.get('/metro', response_model=list[Metro], dependencies=[Depends(all_roles)])
def api_get_metro(db: Annotated[Session, Depends(get_db)],
                  current_user: Annotated[TokenData, Depends(get_current_user)]):
    return get_metro(db)


@platforms.post('/industry', response_model=Industry, dependencies=[Depends(admin_role)])
def api_create_metro(db: Annotated[Session, Depends(get_db)],
                     current_user: Annotated[TokenData, Depends(get_current_user)],
                     title: Annotated[str, Form()]):
    try:
        return create_industry(db, title)
    except HTTPException as e:
        raise e


@platforms.get('/industry', response_model=list[Industry], dependencies=[Depends(all_roles)])
def api_get_metro(db: Annotated[Session, Depends(get_db)],
                  current_user: Annotated[TokenData, Depends(get_current_user)]):
    return get_industry(db)


@platforms.post('/equipments', response_model=Equipments, dependencies=[Depends(admin_role)])
def api_create_metro(db: Annotated[Session, Depends(get_db)],
                     current_user: Annotated[TokenData, Depends(get_current_user)],
                     title: Annotated[str, Form()], price: Annotated[int, Form()]):
    try:
        return create_equipment(db, title, price)
    except HTTPException as e:
        raise e


@platforms.get('/equipments', response_model=list[Equipments], dependencies=[Depends(all_roles)])
def api_get_metro(db: Annotated[Session, Depends(get_db)],
                  current_user: Annotated[TokenData, Depends(get_current_user)]):
    return get_equipments(db)


@platforms.post('/accessibilities', response_model=Accessibilities, dependencies=[Depends(admin_role)])
def api_create_metro(db: Annotated[Session, Depends(get_db)],
                     current_user: Annotated[TokenData, Depends(get_current_user)],
                     title: Annotated[str, Form()]):
    try:
        return create_accessibilities(db, title)
    except HTTPException as e:
        raise e


@platforms.get('/accessibilities', response_model=list[Accessibilities], dependencies=[Depends(all_roles)])
def api_get_metro(db: Annotated[Session, Depends(get_db)],
                  current_user: Annotated[TokenData, Depends(get_current_user)]):
    return get_accessibilities(db)


@platforms.post('/facilities', response_model=Facilities, dependencies=[Depends(admin_role)])
def api_create_metro(db: Annotated[Session, Depends(get_db)],
                     current_user: Annotated[TokenData, Depends(get_current_user)],
                     title: Annotated[str, Form()], price: Annotated[int, Form()]):
    try:
        return create_facility(db, title, price)
    except HTTPException as e:
        raise e


@platforms.get('/facilities', response_model=list[Facilities], dependencies=[Depends(all_roles)])
def api_get_metro(db: Annotated[Session, Depends(get_db)],
                  current_user: Annotated[TokenData, Depends(get_current_user)]):
    return get_facilities(db)


@platforms.post('/', response_model=Platform, dependencies=[Depends(landlord_role)])
def api_create_platform(db: Annotated[Session, Depends(get_db)],
                        current_user: Annotated[TokenData, Depends(get_current_user)],
                        photos: Annotated[list[bytes], File()],
                        title: Annotated[str, Form()],
                        description: Annotated[str, Form()],
                        capacity: Annotated[int, Form()],
                        area: Annotated[int, Form()],
                        phone: Annotated[str, Form()],
                        address: Annotated[str, Form()],
                        price: Annotated[int, Form()],
                        metro_ids: Annotated[list[int], Form()],
                        industry_ids: Annotated[Optional[list[int]], Form()] = None,
                        equipments_ids: Annotated[Optional[list[int]], Form()] = None,
                        accessibilities_ids: Annotated[Optional[list[int]], Form()] = None,
                        facilities_ids: Annotated[Optional[list[int]], Form()] = None):
    try:
        return create_platform(
            db, photos, current_user.user_id, title, description, capacity, area, phone, address, price, metro_ids,
            industry_ids, equipments_ids,
            accessibilities_ids, facilities_ids)
    except HTTPException as e:
        raise e


@platforms.get('/', response_model=list[Platform], dependencies=[Depends(landlord_role)])
def api_create_platform(db: Annotated[Session, Depends(get_db)],
                        current_user: Annotated[TokenData, Depends(get_current_user)]):
    return get_platforms_landlord(db, current_user.user_id)


@platforms.post('/verify', response_model=Platform, dependencies=[Depends(admin_role)])
def api_verify_platform(db: Annotated[Session, Depends(get_db)],
                        current_user: Annotated[TokenData, Depends(get_current_user)],
                        platform_id: Annotated[int, Form()]):
    return verify_platform(db, platform_id)


@platforms.get('/search', response_model=list[Platform], dependencies=[Depends(all_roles)])
def api_search_platforms(db: Annotated[Session, Depends(get_db)],
                         current_user: Annotated[TokenData, Depends(get_current_user)]):
    return get_platforms_search(db)


@platforms.get('/photo/{photo_id}')
def api_photo_platforms(db: Annotated[Session, Depends(get_db)],
                        photo_id: int):
    photo = get_platforms_photo(db, photo_id)
    photo_stream = BytesIO(photo)
    return StreamingResponse(content=photo_stream, media_type='image/jpeg')


# @platforms.post('/bookings', response_model=list[Bookings], dependencies=[Depends(tenant_role)])
# def api_create_platform_booking(db: Annotated[Session, Depends(get_db)],
#                                 current_user: Annotated[TokenData, Depends(get_current_user)],
#                                 platform_id: Annotated[int, Form()],
#                                 from_date: Annotated[str, Form()],
#                                 to_date: Annotated[str, Form()],
#                                 equipments_ids: Annotated[Optional[list[int]], Form()] = None,
#                                 accessibilities_ids: Annotated[Optional[list[int]], Form()] = None,
#                                 facilities_ids: Annotated[Optional[list[int]], Form()] = None):
#     try:
#         return create_platform_booking(
#             db, current_user.user_id, platform_id, from_date, to_date, equipments_ids, accessibilities_ids,
#             facilities_ids
#         )
#     except HTTPException as e:
#         raise e
#
#
# @platforms.get('/bookings/landlord', response_model=list[Bookings], dependencies=[Depends(landlord_role)])
# def api_landlord_bookings(db: Annotated[Session, Depends(get_db)],
#                           current_user: Annotated[TokenData, Depends(get_current_user)]):
#     return get_platform_bookings_landlord(db, current_user.user_id)
