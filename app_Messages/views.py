from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import BaseParser
from .models import Messages
from app_User import models
from rest_framework import status
from django.conf import settings


class PlainTextParser(BaseParser):
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read()
    

@api_view(['POST'])
@parser_classes([PlainTextParser])
@permission_classes([IsAuthenticated])
def messages(request):
    user = request.user
    text = request.data
    text = text.decode('utf-8')
    print(text)
    message = Messages(text=text, user=user)
    message.save()
    return Response({'answer': 'success', 'your_message:': message.text})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_message(request):
    message = Messages.objects.all().values()
    return Response({'messages': message})