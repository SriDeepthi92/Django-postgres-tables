# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GpdbCpTable(models.Model):
    record_field = models.BigIntegerField(db_column='Record #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    entry = models.FloatField(db_column='ENTRY', blank=True, null=True)  # Field name made lowercase.
    check = models.FloatField(db_column='Check', blank=True, null=True)  # Field name made lowercase.
    name1 = models.TextField(db_column='Name1', blank=True, null=True)  # Field name made lowercase.
    pedigree = models.TextField(db_column='Pedigree', blank=True, null=True)  # Field name made lowercase.
    experiment_name = models.TextField(db_column='Experiment Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    year = models.FloatField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    kgha = models.FloatField(db_column='KGHA', blank=True, null=True)  # Field name made lowercase.
    protein = models.FloatField(db_column='Protein', blank=True, null=True)  # Field name made lowercase.
    lw = models.FloatField(db_column='LW', blank=True, null=True)  # Field name made lowercase.
    pm_f = models.FloatField(db_column='PM-F', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    female = models.FloatField(db_column='Female', blank=True, null=True)  # Field name made lowercase.
    male = models.FloatField(db_column='Male', blank=True, null=True)  # Field name made lowercase.
    ripe = models.FloatField(db_column='RIPE', blank=True, null=True)  # Field name made lowercase.
    strl = models.FloatField(db_column='STRL', blank=True, null=True)  # Field name made lowercase.
    head_1 = models.FloatField(db_column='Head_1', blank=True, null=True)  # Field name made lowercase.
    yr = models.FloatField(db_column='YR', blank=True, null=True)  # Field name made lowercase.
    protein_h = models.FloatField(db_column='Protein-H', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lodging = models.FloatField(db_column='LODGING', blank=True, null=True)  # Field name made lowercase.
    falling_number = models.FloatField(db_column='Falling Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gluten_index = models.FloatField(db_column='Gluten Index', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cadmium = models.FloatField(db_column='CADMIUM', blank=True, null=True)  # Field name made lowercase.
    fus_ge = models.FloatField(db_column='FUS_GE', blank=True, null=True)  # Field name made lowercase.
    zeleny = models.FloatField(db_column='ZELENY', blank=True, null=True)  # Field name made lowercase.
    selection = models.FloatField(db_column='Selection', blank=True, null=True)  # Field name made lowercase.
    head = models.FloatField(db_column='Head', blank=True, null=True)  # Field name made lowercase.
    gpdb_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'gpdb_cp_table'
