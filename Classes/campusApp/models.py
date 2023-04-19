from django.db import models

# creating the UniversityCampus model, with the needed data fields
# adding Meta class so that model names display properly

class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=50, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField( default="", blank=True, null=False)

    # creates model manager
    object = models.Manager()

    # displays the object output values as a string
    def __str__(self):
        # Returns the input value of the campus name and
        # field as a tuple to display instead of the default titles
        display_campus = '{0.campus_name}: {0.state}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campus"
