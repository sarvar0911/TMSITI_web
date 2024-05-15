from rest_framework import viewsets, filters, generics
from tmsiti_app.models import (News, Announcements,
                               CEOs, OrganizationalStructure,
                               Contact, Fund,
                               BuildingRegulations, Word, Subsystem, Group)
from .filters import FundPagination
from .serializers import (NewsSerializer, AnnouncementsSerializer,
                          CEOsSerializer, OrganizationalStructureSerializer,
                          ContactSerializer, FundSerializer,
                          BuildingRegulationSerializer, WordSerializer,
                          SubsystemSerializer, GroupSerializer,)
from django.core.mail import send_mail
from django.conf import settings


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


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Send email notification
        subject = 'New Contact Form Submission'
        message = (f"A new contact form has been submitted:\n\nFull Name: {instance.full_name}\n"
                   f"Email: {instance.email}\nPhone: {instance.phone}\nMessage: {instance.message}\n"
                   f"Appeal Type: {instance.appeal_type}")
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.CONTACT_FORM_EMAIL]

        send_mail(subject, message, from_email, recipient_list)


class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer
    pagination_class = FundPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'code', 'year', 'description']


class BuildingRegulationViewSet(viewsets.ModelViewSet):
    queryset = BuildingRegulations.objects.all()
    serializer_class = BuildingRegulationSerializer


class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['word', 'language']


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class SubsystemListCreate(generics.ListCreateAPIView):
    queryset = Subsystem.objects.all()
    serializer_class = SubsystemSerializer


class SubsystemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subsystem.objects.all()
    serializer_class = SubsystemSerializer


class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
