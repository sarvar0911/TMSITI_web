from rest_framework import viewsets
from tmsiti_app.models import News, Announcements, CEOs, OrganizationalStructure
from .serializers import NewsSerializer, AnnouncementsSerializer, CEOsSerializer, OrganizationalStructureSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class AnnouncementsViewSet(viewsets.ModelViewSet):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer


class CEOsViewSet(viewsets.ModelViewSet):
    queryset = CEOs.objects.all()
    serializer_class = CEOsSerializer


class OrganizationalStructureViewSet(viewsets.ModelViewSet):
    queryset = OrganizationalStructure.objects.all()
    serializer_class = OrganizationalStructureSerializer
