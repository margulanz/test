from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, MinLengthValidator

# Create your models here.
allowd_chars = RegexValidator(r'^[абвгд]*$', 'Только set(а,б,в,г,д) допустимы')

class Test(models.Model):
	login = models.CharField(max_length = 10, unique = True, validators = [MinLengthValidator(10)]) #
	def __str__(self):
		return self.login


class ScoreIQ(models.Model):
	took_at = models.DateTimeField()
	score   = models.IntegerField(default = 0,validators=[MinValueValidator(0), MaxValueValidator(50)])
	login   = models.ForeignKey(Test, on_delete=models.CASCADE, unique  =True)
	def __repr__(self):
		return f'iq score for {self.login}'

	def __str__(self):
		return f'iq score for {self.login}'


class ScoreEQ(models.Model):
	took_at = models.DateTimeField()
	sequence = models.CharField(max_length = 5,validators=[allowd_chars])
	login   = models.ForeignKey(Test, on_delete=models.CASCADE, unique = True)
	def __repr__(self):
		return f'eq score for {self.login}'
	def __str__(self):
		return f'eq score for {self.login}'