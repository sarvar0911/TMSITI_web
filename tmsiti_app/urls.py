from rest_framework import routers
from .views import (NewsViewSet, AnnouncementsViewSet, CEOsViewSet,
                    OrganizationalStructureViewSet, ContactViewSet,
                    FundViewSet, BuildingRegulationViewSet)

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'announcements', AnnouncementsViewSet)
router.register(r'ceos', CEOsViewSet)
router.register(r'organizational-structure', OrganizationalStructureViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'fund', FundViewSet)
router.register(r'building-regulations', BuildingRegulationViewSet)

urlpatterns = router.urls
