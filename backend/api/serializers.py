from django.contrib.auth.models import User
from .models import Note
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # Debug the validation process
        print(f"Validating data: {data}")
        return data

    def create(self, validated_data):
        print(f"Creating user with: {validated_data}")
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwargs = {"author": {"read_only": True}}

    def create(self, validated_data):
        # Author is set in perform_create, so no need to worry here
        return super().create(validated_data)
