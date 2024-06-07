from rest_framework import serializers

from attendance.models import Attendance
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name']


class StudentAttendanceListSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'


class BulkStudentAttendanceListUpdateSerializer(serializers.ListSerializer):
    def update(self, queryset, validated_data):
        instance_mapping = {instance.id: instance for instance in queryset}
        data_mapping = {item['id']: item for item in validated_data}

        updated_instances = []
        for instance_id, data in data_mapping.items():
            instance = instance_mapping.get(instance_id, None)
            if instance is not None:
                for attr, value in data.items():
                    setattr(instance, attr, value)
                instance.save()
                updated_instances.append(instance)

        return updated_instances


class AttendancesUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Attendance
        fields = ['id', 'status']
        list_serializer_class = BulkStudentAttendanceListUpdateSerializer


class AttendanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'status']
