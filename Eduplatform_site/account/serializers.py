from rest_framework import serializers

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from .models import (User, Teacher, Student, Group)


__all__ = {
    "UserSerializer", "TeacherSerializer", 
    "StudentSerializer", "GroupSerializer", 
    "GroupTeacherSerializer", "RegisterSerializer",
    "LoginSerializer"
    }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value: str) -> str:
        return make_password(value)
    

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'group_name', 'course', 'teacher', 'student')


class GroupTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher

    def to_representation(self, obj):
        match isinstance(obj, Teacher):
            case True:
                serializer = TeacherSerializer(obj)
            case False:
                serializer = GroupSerializer(obj)
            case _:
                raise Exception("Nothing to serialize.")
        return serializer.data


class RegisterSerializer(serializers.ModelSerializer):
    "token = ..."

    class Meta:
        model = User
        field = ("email", "password", "first_name", "last_name")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    "token = ..."

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(username=email, password=password)

        if not all(email or password or user):
            raise serializers.ValidationError("Check email or/and password. Data is incorrect!")

        if not user.is_active:
            raise serializers.ValidationError("This user is not active yet :(")

        return {"email": user.email}
