from typing import Protocol, Optional
from app.models import Organization

class OrganizationRepository(Protocol):
    def get_by_id(self, organization_id: int) -> Optional[Organization]:
        ...

    def create(self, organization: Organization) -> Organization:
        ...