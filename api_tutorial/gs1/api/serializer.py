from rest_framework import serializers
class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)


# class StudentSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = "__all__"
    