from rest_framework import viewsets, filters, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tmsiti_app.models import (News, Announcements,
                               CEOs, OrganizationalStructure,
                               Contact, Fund,
                               BuildingRegulations, Word, Subsystem, Group, Rating)
from .filters import FundPagination
from .serializers import (NewsSerializer, AnnouncementsSerializer,
                          CEOsSerializer, OrganizationalStructureSerializer,
                          ContactSerializer, FundSerializer,
                          BuildingRegulationSerializer, WordSerializer,
                          SubsystemSerializer, GroupSerializer, RatingSerializer, )
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


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_pk = self.kwargs.get('product_pk')
        if product_pk is not None:
            return Rating.objects.filter(product_id=product_pk)
        else:
            return Rating.objects.none()

    def get_serializer_context(self):
        user_id = self.request.user.id
        product_id = self.kwargs.get("product_pk")
        return {"user_id": user_id, "product_id": product_id}

    def perform_create(self, serializer):
        user_id = self.request.user.id
        product_id = self.kwargs.get("product_pk")

        # Delete any existing rating for this user and product
        Rating.objects.filter(user_id=user_id, product_id=product_id).delete()

        # Save the new rating
        serializer.save(user_id=user_id, product_id=product_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
