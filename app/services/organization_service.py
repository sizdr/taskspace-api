from app.repositories.interfaces.organization_repository import OrganizationRepository
from app.services.user_service import UserService
from app.schemas import OrganizationCreateForm
from app.models import Organization, RoleEnum
from fastapi import HTTPException

class OrganizationService: 
    def __init__(self, org_repo: OrganizationRepository, user_service: UserService):
        self.org_repo = org_repo
        self.user_service = user_service

    def create_organization(self, organization_form: OrganizationCreateForm):
        org_dict = organization_form.organization.model_dump()
        org_model = Organization(**org_dict)
        organization = self.org_repo.create(org_model)
        if not organization:
            return HTTPException(status_code=500, detail="Organization creation failed")
        user = self.user_service.create_user(organization_form.user, organization.id, RoleEnum.OWNER)
        if not user:
            return HTTPException(status_code=500, detail="User creation failed")
        return organization


        