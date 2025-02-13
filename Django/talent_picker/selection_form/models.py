from django.db import models
import os
import uuid

def upload_path(instance, filename,folder_name):
    ext = filename.split('.')[-1] 
    unique_filename = f"{uuid.uuid4()}.{ext}" 
    return os.path.join(folder_name, unique_filename) 


class Employee(models.Model):
    EXPERIENCE_CHOICES = [
        ('fresher', 'Fresher'),
        ('1-3 years', '1-3 Years'),
        ('3-5 years', '3-5 Years'),
        ('5+ years', '5+ Years'),
    ]
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    position = models.CharField(max_length=100)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='fresher')
    resume = models.FileField(upload_to=lambda instance, filename: upload_path(instance, filename, "resumes"), blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.get_experience_display()}"


class Education(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='education')
    highest_degree = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    specialization = models.CharField(max_length=255)
    percentage = models.FloatField()
    education_proof = models.FileField(upload_to=lambda instance, filename: upload_path(instance, filename, "education_proofs"), blank=True, null=True)

    def __str__(self):
        return f"{self.employee.full_name}'s Education"


class BankDetails(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='bank_details')
    account_holder = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee.full_name}'s Bank Details"


class PreviousEmployment(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='previous_employment')
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    employment_duration = models.CharField(max_length=255)
    reason_for_leaving = models.CharField(max_length=255)
    skills_acquired = models.TextField()
    company_reference = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.employee.full_name}'s Previous Employment"
