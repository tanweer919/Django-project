from rest_framework import views, status
from account.serializers import AccountSerializer
from rest_framework.response import Response
import sys
class CurrentUserView(views.APIView):

    def post(self, request):
        serializer = AccountSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
