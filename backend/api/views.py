from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer,NoteSerializer
import logging
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from .models import Note
logger = logging.getLogger(__name__)
# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        try:
            if serializer.is_valid():
                serializer.save(author=self.request.user)
                logger.info(f'Note created successfully for user: {self.request.user.username}')
            else:
                logger.error(f'Error creating note: {serializer.errors}')
                logger.debug(f'Failed data: {serializer.initial_data}')
        except Exception as e:
            logger.error(f"Exception occurred during note creation: {str(e)}")
            raise

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            logger.info(f"Data is valid for user {request.user.username}. Creating note...")
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Validation errors for user {request.user.username}: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            logger.info(f'Note created successfully for user: {self.request.user.username}')
        else:
            logger.error(f'Error creating note: {serializer.errors}')
            logger.debug(f'Full data: {serializer.initial_data}')

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Ensure the note can be accessed by the authenticated user
        user = self.request.user
        return Note.objects.filter(author=user)

    def delete(self, request, *args, **kwargs):
        try:
            # Attempt to delete the note
            instance = self.get_object()
            self.perform_destroy(instance)
            logger.info(f'Note deleted successfully for user: {request.user.username}')
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            # Log the error details
            logger.error(f'Error deleting note: {str(e)}')
            return Response({"detail": "An error occurred while deleting the note."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_destroy(self, instance):
        # Override this method if you need to add custom logic before deletion
        instance.delete()



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print("Data is valid.")
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Log the validation errors
            print(f"Validation errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




