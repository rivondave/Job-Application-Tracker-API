from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from typing import Optional
from sqlalchemy import asc, desc
from fastapi import Query

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.dependencies import (get_current_user)

from app.models.application import Application
from app.models.user import User

from app.schemas.application import (ApplicationCreate, ApplicationResponse, ApplicationUpdate)

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

@router.post(
    "",
    response_model=ApplicationResponse
)
def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    new_application = Application(
        company_name=application.company_name,
        job_title=application.job_title,
        status=application.status,
        notes=application.notes,
        date_applied=application.date_applied,
        user_id=current_user.id
    )

    db.add(new_application)

    db.commit()

    db.refresh(new_application)

    return new_application

@router.get(
    "",
    response_model=list[ApplicationResponse]
)
def get_applications(
    status: Optional[str] = None,
    search: Optional[str] = None,
    sort_by: Optional[str] = "date_applied",
    order: Optional[str] = "desc",
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    query = (
        db.query(Application)
        .filter(
            Application.user_id == current_user.id
        )
    )

    if status:
        query = query.filter(
            Application.status == status
        )

    if search:
        query = query.filter(
            Application.company_name.ilike(
                f"%{search}%"
            )
        )

    allowed_sort_fields = {
        "company_name": Application.company_name,
        "job_title": Application.job_title,
        "status": Application.status,
        "date_applied": Application.date_applied,
        "created_at": Application.created_at
    }

    sort_column = allowed_sort_fields.get(
        sort_by,
        Application.date_applied
    )

    if order.lower() == "asc":
        query = query.order_by(
            asc(sort_column)
        )
    else:
        query = query.order_by(
            desc(sort_column)
        )

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )

@router.get(
    "/{application_id}",
    response_model=ApplicationResponse
)
def get_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    application = (
        db.query(Application)
        .filter(
            Application.id == application_id,
            Application.user_id == current_user.id
        )
        .first()
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application

@router.put(
    "/{application_id}",
    response_model=ApplicationResponse
)
def update_application(
    application_id: int,
    data: ApplicationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    application = (
        db.query(Application)
        .filter(
            Application.id == application_id,
            Application.user_id == current_user.id
        )
        .first()
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    application.company_name = data.company_name
    application.job_title = data.job_title
    application.status = data.status
    application.notes = data.notes
    application.date_applied = data.date_applied

    db.commit()
    db.refresh(application)

    return application


@router.delete(
    "/{application_id}"
)
def delete_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    application = (
        db.query(Application)
        .filter(
            Application.id == application_id,
            Application.user_id == current_user.id
        )
        .first()
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    db.delete(application)
    db.commit()

    return {
        "message": "Application deleted"
    }