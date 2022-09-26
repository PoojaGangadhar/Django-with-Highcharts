from django.db import models

# Create your models here.
class Passenger(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )

    CHERBOURG = 'C'
    QUEENSTOWN = 'Q'
    SOUTHAMPTON = 'S'
    PORT_CHOICES = (
        (CHERBOURG, 'Cherbourg'),
        (QUEENSTOWN, 'Queenstown'),
        (SOUTHAMPTON, 'Southampton'),
    )

    survived = models.IntegerField(db_column='Survived', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    sex = models.TextField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    ticket = models.TextField(db_column='Ticket', blank=True, null=True)  # Field name made lowercase.
    embarked = models.TextField(db_column='Embarked', blank=True, null=True, choices=PORT_CHOICES)  # Field name made lowercase.

    class Meta:
        db_table = 'passenger'


