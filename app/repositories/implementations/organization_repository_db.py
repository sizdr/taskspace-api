from sqlmodel import Session, select
from typing import Optional
from app.models import Organization

class OrganizationRepositoryDB:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, organization_id: int) -> Optional[Organization]:
        stmt = select(Organization).where(Organization.id == organization_id)
        return self.session.exec(stmt).first()

    def create(self, organization: Organization) -> Organization:
        self.session.add(organization)
        self.session.commit()
        self.session.refresh(organization)
        return organization