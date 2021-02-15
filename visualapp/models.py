from django.db import models


class Description(models.Model):
    id = models.AutoField(primary_key=True)
    srp_id = models.TextField(db_column='SRP_ID', blank=True, null=True)
    srr_id = models.TextField(db_column='SRR_ID', blank=True, null=True)
    assay_type = models.TextField(db_column='Assay_Type', blank=True, null=True)
    cultivar = models.TextField(db_column='Cultivar', blank=True, null=True)
    treatment = models.TextField(db_column='Treatment', blank=True, null=True)
    stage = models.TextField(db_column='Stage', blank=True, null=True)
    tissue = models.TextField(db_column='Tissue', blank=True, null=True)
    layout = models.TextField(db_column='Layout', blank=True, null=True)
    treat = models.TextField(db_column='Treat', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description'


class Tpm(models.Model):
    id = models.AutoField(primary_key=True)
    target_id = models.TextField(blank=True, null=True)
    tpm = models.TextField(db_column='Tpm', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpm'
