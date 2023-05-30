import logging
from .models import UserSpec
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serializers import UserSpecSerializer

logger = logging.getLogger(__name__)


class UserListCreate(generics.ListCreateAPIView):
    queryset = UserSpec.objects.all()
    serializer_class = UserSpecSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            logger.exception(f'ValidationError when creating a user: {e}')
            return Response({"error": "Invalid data provided."}, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieve(generics.RetrieveAPIView):
    queryset = UserSpec.objects.all()
    serializer_class = UserSpecSerializer
