from django.db import models

# Create your models here.
class AgentName(models.Model):
    name_id = models.AutoField(primary_key=True, null=False)
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255,null=True)
    phone = models.CharField(max_length=13, null = False)
    pollingunit_uniqueid = models.IntegerField(null=False)

    class Meta:
        db_table ='agentname'

class Announced_Lga_Results(models.Model):
    result_id = models.AutoField(primary_key=True, null= False)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table ='announced_lga_results'

class Announced_Pu_Results(models.Model):
    result_id = models.AutoField(primary_key=True, null= False)
    polling_unit_uniqueid_id = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table ='announced_pu_results'

class Announced_State_Results(models.Model):
    result_id = models.AutoField(primary_key=True, null= False)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table ='announced_state_results'

class Announced_Ward_Results(models.Model):
    result_id = models.AutoField(primary_key=True, null= False)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table ='announced_ward_results'

class Lga(models.Model):
    uniqueid =  models.AutoField(primary_key=True, null=False)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table ='lga'

class Party(models.Model):
    id = models.AutoField(primary_key=True)
    partyid = models.CharField(max_length = 11)
    partyname = models.CharField(max_length=11)

    class Meta:
        db_table ='party'

class Polling_Unit(models.Model):
    uniqueid = models.AutoField(primary_key=True, null=False)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id_id = models.IntegerField()
    uniquewardid = models.IntegerField(null=True)
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.TextField()
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    entered_by_user = models.CharField(max_length=50, null=True)
    date_entered = models.DateTimeField(auto_now_add=True, null=True)
    user_ip_address = models.CharField(max_length=50, null=True)

    class Meta:
        db_table ='polling_unit'

class States(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name =  models.CharField(max_length=50)

    class Meta:
        db_table ='states'

class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table ='ward'
