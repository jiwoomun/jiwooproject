from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from board.models import PostVO
from board.serializer import PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from icecream import ic

class Boards(APIView):
    def post(self,request):
        data = request.data['body']
        ic(data)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result':f'Welcome, {serializer.data.get("name")}'}, status=201)
            ic(serializer.errors)
        return Response(serializer.errors, status=400)

