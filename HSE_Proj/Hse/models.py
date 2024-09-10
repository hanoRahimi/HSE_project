from django.db import models
from django.contrib.auth.models import User

# مدل برای ذخیره اطلاعات ایمنی و سلامت محیط کار
class Incident(models.Model):
    INCIDENT_TYPES = [
        ('accident', 'Accident'),
        ('near_miss', 'Near Miss'),
        ('hazard', 'Hazard'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES)
    date_reported = models.DateField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)  # ارجاع به کاربری که حادثه را گزارش داده
    location = models.CharField(max_length=255)
    risk_level = models.IntegerField()  # سطح ریسک حادثه (مثلاً از 1 تا 10)
    corrective_action = models.TextField(blank=True, null=True)  # اقدام اصلاحی برای رفع مشکل

    def __str__(self):
        return f"{self.title} ({self.get_incident_type_display()})"

# مدل برای ریسک‌ها و ارزیابی‌ها
class RiskAssessment(models.Model):
    risk_title = models.CharField(max_length=255)
    description = models.TextField()
    assessed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_assessed = models.DateField()
    risk_level_before = models.IntegerField()  # سطح ریسک قبل از اقدامات
    risk_level_after = models.IntegerField()   # سطح ریسک بعد از اقدامات
    mitigation_plan = models.TextField()  # برنامه کاهش ریسک

    def __str__(self):
        return f"{self.risk_title} (Risk Level Before: {self.risk_level_before}, After: {self.risk_level_after})"

# مدل برای گزارشات ایمنی و سلامت
class HSEReport(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    report_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null=True, blank=True)  # ارجاع به حادثه‌ای که ممکن است مرتبط باشد
    risk_assessment = models.ForeignKey(RiskAssessment, on_delete=models.SET_NULL, null=True, blank=True)  # ارجاع به ارزیابی ریسکی که ممکن است مرتبط باشد

    def __str__(self):
        return self.title

# مدل برای کاربران و نقش‌ها در سیستم HSE
class HSEUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    supervisor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='supervisees')  # ارجاع به مدیر مستقیم

    def __str__(self):
        return f"{self.user.username} ({self.job_title})"
