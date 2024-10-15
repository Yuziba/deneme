from django.db import models

class AaModel(models.Model):
    nick = models.CharField(max_length=50)
    mesaj = models.CharField(max_length=150)
    def __str__(self):
        return f"isim : {self.nick} mesaj {self.mesaj}"