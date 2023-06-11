from rest_framework import serializers


from .models import ScoreIQ, ScoreEQ, Test





class ScoreIQSerializer(serializers.ModelSerializer):
	class Meta:
		model = ScoreIQ
		fields = '__all__'

class ScoreEQSerializer(serializers.ModelSerializer):
	class Meta:
		model = ScoreEQ
		fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
	ScoreIQ = serializers.SerializerMethodField()
	ScoreEQ = serializers.SerializerMethodField()
	class Meta:
		model = Test
		fields = [
			"ScoreIQ",
			"ScoreEQ"
		]

	def get_ScoreIQ(self,obj):
		if ScoreIQ.objects.filter(login = obj).exists():
			score_iq = ScoreIQSerializer(ScoreIQ.objects.filter(login = obj).first()).data
			return score_iq
		return None
	def get_ScoreEQ(self,obj):
		if ScoreEQ.objects.filter(login = obj).exists():
			score_eq = ScoreEQSerializer(ScoreEQ.objects.filter(login = obj).first()).data
			return score_eq
		return None