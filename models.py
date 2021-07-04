from django.db import models

class Admins(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)


class Manger(models.Model):
    idmanger = models.AutoField(primary_key=True)
    hospital = models.CharField(max_length=45, blank=True, null=True)
    admin_id = models.ForeignKey(Admins, on_delete=models.CASCADE, related_name='Admins_admin_id')

class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    idmanger = models.ForeignKey(Manger, on_delete=models.CASCADE, related_name='Manger_idmanger')
    # admin_id = models.ForeignKey(Admins, on_delete=models.CASCADE, db_column='Admins_admin_id')

#
class Department(models.Model):
    iddepartment = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    departmentcol = models.CharField(max_length=45, blank=True, null=True)
    hospital_hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='Hospital_hospital_id')

class Doctor(models.Model):
    iddoctor = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    pressent = models.TextField(blank=True, null=True)
    department_iddepartment = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_iddepartment')


class DoctorHasHospital(models.Model):
    doctor_iddoctorD = models.OneToOneField(Doctor, on_delete=models.CASCADE, related_name='doctor_iddoctorD', primary_key=True)
    hospital_hospital_idD = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='hospital_hospital_idD')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hospital_manger_idmangerD = models.ForeignKey(Manger, on_delete=models.CASCADE, related_name='hospital_manger_idmangerD')  # Field name made lowercase.
    hospital_admin_admin_idD = models.ForeignKey(Admins, on_delete=models.CASCADE, related_name='hospital_admin_admin_idD')  # Field name made lowercase. Field renamed to remove unsuitable characters.



class Nurse(models.Model):
    idnurse = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    pressent = models.CharField(max_length=45, blank=True, null=True)
    department_iddepartmentN = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_iddepartmentN')
    manger_idmangerN = models.ForeignKey(Manger, on_delete=models.CASCADE, related_name='manger_idmangerN')


class Receptinist(models.Model):
    idreceptinist = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    manger_idmanger = models.ForeignKey(Manger, on_delete=models.CASCADE, related_name='manger_idmanger')
    hospital_hospital_idP = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='Hospital_hospital_idp')




class Pathient(models.Model):
    idpathient = models.AutoField(db_column='idPathient', primary_key=True)
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)
    phone_field = models.IntegerField(db_column='phone #', blank=True, null=True)
    gender = models.CharField(db_column='Gender', max_length=45, blank=True, null=True)
    national_id = models.IntegerField(db_column='National id', blank=True, null=True)  #
    emergency_contact_field = models.IntegerField(db_column='emergency contact #', blank=True, null=True)
    doctor_iddoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_iddoctor')
    nurse_idnurseP = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='nurse_idnurse')
    receptinist_idreceptinistP = models.ForeignKey(Receptinist, on_delete=models.CASCADE, related_name='receptinist_idreceptinistP')



class PathientHasHospital(models.Model):
    pathient_idpathient = models.OneToOneField(Pathient, on_delete=models.CASCADE, db_column='Pathient_idPathient', primary_key=True)  # Field name made lowercase.
    hospital_hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE, db_column='Hospital_ hospital ID')



class Rooms(models.Model):
    idrooms = models.AutoField(primary_key=True)
    filled = models.CharField(max_length=45, blank=True, null=True)
    capacity = models.CharField(max_length=45, blank=True, null=True)
    degree = models.CharField(max_length=45, blank=True, null=True)
    department_iddepartment = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='department_iddepartment')

class Bed(models.Model):
    idbed = models.AutoField(db_column='idBed', primary_key=True)  # Field name made lowercase.
    filled = models.CharField(max_length=45, blank=True, null=True)
    rooms_idrooms = models.ForeignKey('Rooms',on_delete=models.CASCADE ,  related_name='rooms_idrooms')


class Report(models.Model):
    idreport = models.AutoField(primary_key=True)
    full_report = models.CharField(db_column='full report', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dignose = models.CharField(max_length=45, blank=True, null=True)
    date = models.CharField(max_length=45, blank=True, null=True)
    treatment = models.CharField(max_length=45, blank=True, null=True)
    required_tests = models.CharField(db_column='required tests', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pathient_idpathient = models.ForeignKey(Pathient, on_delete=models.CASCADE, related_name='Pathient_idPathient')  # Field name made lowercase.
    pathient_doctor_iddoctor = models.ForeignKey(Pathient, on_delete=models.CASCADE, related_name='Pathient_doctor_iddoctor')  # Field name made lowercase.

