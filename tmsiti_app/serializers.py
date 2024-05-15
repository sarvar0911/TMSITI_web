from rest_framework.serializers import ModelSerializer

from tmsiti_app.models import News, Announcements, CEOs, OrganizationalStructure, Contact, Fund, BuildingRegulations, \
    Word, Group, Subsystem


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


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'message', 'appeal_type', 'file_upload']


class FundSerializer(ModelSerializer):
    class Meta:
        model = Fund
        fields = ['name', 'code', 'year', 'description']


class BuildingRegulationSerializer(ModelSerializer):
    class Meta:
        model = BuildingRegulations
        fields = ['id', 'code', 'name', 'document']


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'language']


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'code', 'name']


class SubsystemSerializer(ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Subsystem
        fields = ['id', 'code', 'name', 'groups']
