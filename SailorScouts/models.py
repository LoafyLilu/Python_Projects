from django.db import models

# Creates the Scout Model
class Scout(models.Model):
    sailor_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    japanese_name = models.CharField(max_length=50)
    sailor_power = models.CharField(max_length=50)
    # Defines the model Manager for Scout
    Scouts = models.Manager()






    # Allows references to a specific entry be returned as the sailor name not the primary key
    def __str__(self):
        return self.sailor_name + '' + self.english_name