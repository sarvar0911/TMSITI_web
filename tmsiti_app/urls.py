from rest_framework import routers
from .views import NewsViewSet, AnnouncementsViewSet, CEOsViewSet, OrganizationalStructureViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'announcements', AnnouncementsViewSet)
router.register(r'ceos', CEOsViewSet)
router.register(r'organizational-structure', OrganizationalStructureViewSet)

urlpatterns = router.urls
