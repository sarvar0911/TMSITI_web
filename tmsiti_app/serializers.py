from rest_framework.serializers import ModelSerializer

from tmsiti_app.models import News, Announcements, CEOs, OrganizationalStructure


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class AnnouncementsSerializer(ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'


class CEOsSerializer(ModelSerializer):
    class Meta:
        model = CEOs
        fields = '__all__'


class OrganizationalStructureSerializer(ModelSerializer):
    class Meta:
        model = OrganizationalStructure
        fields = '__all__'
