from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager

# Custom User model
class CustomUser(AbstractUser):
    EMPLOYER = 'E'
    JOB_SEEKER = 'J'
    ROLE = [
        (EMPLOYER, 'Employer'),
        (JOB_SEEKER, 'Job Seeker')
    ]

    username = None
    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=2, choices=ROLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Company model
class Company(models.Model):
    company_name = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name


# Job model
class Job(models.Model):
    FULLTIME = 'FT'
    PARTTIME = 'PT'
    CONTRACT = 'CON'
    FREELANCE = 'FR'
    JOB_TYPE = [
        (FULLTIME, "Full-time"),
        (PARTTIME, "Part-time"),
        (CONTRACT, 'Contract'),
        (FREELANCE, 'Freelance'),
    ]

    job_title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100)
    job_type = models.CharField(choices=JOB_TYPE, default=FULLTIME, max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job_title}, {self.location}"
