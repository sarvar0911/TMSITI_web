from django.urls import path
from rest_framework import routers
from .views import (NewsViewSet, AnnouncementsViewSet, CEOsViewSet,
                    OrganizationalStructureViewSet, ContactViewSet,
                    FundViewSet, BuildingRegulationViewSet,
                    WordList, WordDetail, SubsystemListCreate, SubsystemRetrieveUpdateDestroy, GroupListCreate,
                    GroupRetrieveUpdateDestroy, )

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'announcements', AnnouncementsViewSet)
router.register(r'ceos', CEOsViewSet)
router.register(r'organizational-structure', OrganizationalStructureViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'fund', FundViewSet)
router.register(r'building-regulations', BuildingRegulationViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('words/', WordList.as_view(), name='word-list'),
    path('words/<int:pk>/', WordDetail.as_view(), name='word-detail'),
    path('subsystems/', SubsystemListCreate.as_view(), name='subsystem-list'),
    path('subsystems/<int:pk>/', SubsystemRetrieveUpdateDestroy.as_view(), name='subsystem-detail'),
    path('groups/', GroupListCreate.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupRetrieveUpdateDestroy.as_view(), name='group-detail'),

]
