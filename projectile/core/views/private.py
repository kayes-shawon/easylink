from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..serializers import PersonSerializer


class MeDetail(generics.RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
