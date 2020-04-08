import datetime
from django.contrib.auth.models import User
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.http import JsonResponse
import ghasedak
import random
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
@permission_classes((AllowAny, IsAuthenticated))
def test(request):
    """
    kghvkghvkh
    """
    content = {'message': 'Hello, World! from yapaitek api'}
    return JsonResponse(content)


@api_view(['POST'])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
# @permission_classes((AllowAny,IsAuthenticated))
def send_code(request):
    """
        Send Code To Mobile / removed
    """
    sms = ghasedak.Ghasedak("x")
    content = {
        'status_code': '200',
        'data_code': '2120',
        'data': sms,
    }
    return JsonResponse(content, status=200)

@api_view(['POST'])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
# @permission_classes((AllowAny,IsAuthenticated))
def verify_code(request):
    """
     Verify Code From Mobile / removed
    """
    if request.method == "POST":
        time = datetime.datetime.now()
        code = request.data['code']
        check_existence = User.objects.filter(tracking_code=code)
        if check_existence.count() == 0:

            content = {'message': ' موجود نیست'}
            return JsonResponse(content, status=200)
        elif check_existence.count() > 0:

            u = check_existence.first()
            if code == u.tracking_code:
                u.tracking_code = None
                u.is_active = True
                u.save()

            refresh = RefreshToken.for_user(u)

            content = {'access': str(refresh.access_token), 'refresh': str(refresh), 'data': u'فعال شد'}

            return JsonResponse(content, status=200)
    else:
        content = {'access': '403'}
        return JsonResponse(content, status=200)
