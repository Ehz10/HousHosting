from django.db import models


class Biblio(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True, null=True)
    genderid = models.ForeignKey('Genderbook', models.DO_NOTHING, db_column='genderid')
    aquisition = models.DateField(blank=True, null=True)
    editor = models.CharField(blank=True, null=True)
    num_page = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Biblio'


class Genderbook(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    class Meta:
        managed = False
        db_table = 'Genderbook'