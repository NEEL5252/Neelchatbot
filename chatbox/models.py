from django.db import models

# Create your models here.
class new_user(models.Model):
    responseId = models.CharField(max_length = 50, blank = True, null = True)

    def __str__(self):
        return str(self.id) + " " + str(self.responseId)  

class new_order(models.Model):
    user = models.ForeignKey(new_user, on_delete = models.CASCADE, default = '')
    item_name = models.CharField(max_length = 50, blank = True, null = True)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id) + " " + str(self.item_name) + " " + str(self.quantity) + " " + str(self.user.id)