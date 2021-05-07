
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


for user in User.objects.all():
    Token.objects.get_or_create(user=user)