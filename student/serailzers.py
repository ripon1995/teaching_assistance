from rest_framework import serializers

from course.models import Course
from student.error_messages.error_messages import NAME_ERROR_MESSAGE, CONTACT_ERROR_MESSAGE
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=30, min_length=5, error_messages=NAME_ERROR_MESSAGE)
    father_name = serializers.CharField(required=True, max_length=30, min_length=5, error_messages=NAME_ERROR_MESSAGE)
    mother_name = serializers.CharField(required=True, max_length=30, min_length=5, error_messages=NAME_ERROR_MESSAGE)
    institution = serializers.CharField(required=True, max_length=30, min_length=5, error_messages=NAME_ERROR_MESSAGE)
    contact_number = serializers.CharField(required=True, max_length=11, min_length=11,
                                           error_messages=CONTACT_ERROR_MESSAGE)
    father_contact_number = serializers.CharField(required=True, max_length=11, min_length=11,
                                                  error_messages=CONTACT_ERROR_MESSAGE)
    start_date = serializers.DateField(format='%Y-%m-%d', read_only=True)

    def validate(self, attrs):
        contact_number = attrs.get('contact_number')
        father_contact_number = attrs.get('father_contact_number')
        if Student.objects.filter(contact_number=contact_number).exists():
            raise serializers.ValidationError(CONTACT_ERROR_MESSAGE['unique'])

        if Student.objects.filter(father_contact_number=father_contact_number).exists():
            raise serializers.ValidationError(CONTACT_ERROR_MESSAGE['unique'])

        return attrs

    class Meta:
        model = Student
        fields = '__all__'


class StudentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, max_length=30, min_length=5, error_messages=NAME_ERROR_MESSAGE)
    father_name = serializers.CharField(required=False, max_length=30, min_length=5, error_messages=NAME_ERROR_MESSAGE)
    mother_name = serializers.CharField(required=False, max_length=30, min_length=5, error_messages=NAME_ERROR_MESSAGE)
    contact_number = serializers.CharField(required=False, max_length=11, min_length=11,
                                           error_messages=CONTACT_ERROR_MESSAGE)
    father_contact_number = serializers.CharField(required=False, max_length=11, min_length=11,
                                                  error_messages=CONTACT_ERROR_MESSAGE)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    def validate(self, attrs):
        contact_number = attrs.get('contact_number')
        if contact_number and Student.objects.exclude(pk=self.instance.pk).filter(
                contact_number=contact_number).exists():
            raise serializers.ValidationError(CONTACT_ERROR_MESSAGE['unique'])

        father_contact_number = attrs.get('father_contact_number')
        if father_contact_number and Student.objects.exclude(pk=self.instance.pk).filter(
                father_contact_number=father_contact_number).exists():
            raise serializers.ValidationError(CONTACT_ERROR_MESSAGE['unique'])

        return attrs

    class Meta:
        model = Student
        fields = '__all__'