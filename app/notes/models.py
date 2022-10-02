from django.db import models

class User_note(models.Model):
	external_id = models.PositiveIntegerField(verbose_name = "Telegram user ID")
	name = models.TextField(verbose_name = "Имя пользователя" )
	external_id = models.PositiveIntegerField(verbose_name = "Telegram user ID")
	def __str__(self):
		return f'{self.external_id} {self.name}'
class Message(models.Model):
	profile = models.ForeignKey(
		to='notes.User_note',
		on_delete=models.PROTECT,
	)
	text = models.TextField(
		verbose_name = "Текст",
	)
	created_time = models.DateTimeField(
		verbose_name='Время получения', 	
		auto_now_add=True,
	)
	def __str__(self):
		return f'Сообщение {self.text} от {self.profile}'