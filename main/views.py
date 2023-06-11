from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from .models import ScoreIQ, ScoreEQ, Test
from .serializers import ScoreIQSerializer, ScoreEQSerializer, TestSerializer
# Create your views here.

allowed_chars = 'abcdefghijklmnopqrstuvwxyz'

@api_view()
def create_test(request):
	login = get_random_string(10, allowed_chars = allowed_chars)
	test = Test(login = login)
	test.save()
	return Response({"login": login})



class ScoreIQView(viewsets.ModelViewSet):
	queryset = ScoreIQ.objects.all()
	serializer_class = ScoreIQSerializer



class ScoreEQView(viewsets.ModelViewSet):
	queryset = ScoreEQ.objects.all()
	serializer_class = ScoreEQSerializer



class ResultsView(viewsets.ModelViewSet):
	queryset = Test.objects.all()
	serializer_class = TestSerializer
	lookup_field = 'login'