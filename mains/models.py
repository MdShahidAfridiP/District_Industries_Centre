from django.db import models

# Create your models here.
class dic_schemes(models.Model):
    title=models.TextField()
    document=models.FileField(upload_to='documents')
    def __str__(self):
        return 'dic schemes: ' + self.title

class rural_schemes(models.Model):
    title = models.TextField()
    document = models.FileField(upload_to='documents')
    def __str__(self):
        return 'rural scheme: ' + self.title

class invester_services(models.Model):
    name = models.TextField()
    url = models.TextField()
    def __str__(self):
        return 'invester services: ' + self.name

class related_dept(models.Model):
    department_name=models.TextField()
    url=models.TextField()
    def __str__(self):
        return 'related dept: ' + self.department_name

class testimonials(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    photo=models.ImageField()
    review=models.TextField()
    def __str__(self):
        return 'Testimonial: ' + self.name

class g_acts(models.Model):
    act_name=models.TextField()
    url=models.TextField()
    def __str__(self):
        return 'Act: ' + self.act_name

class rules(models.Model):
    rule_name=models.TextField()
    url=models.TextField()
    def __str__(self):
        return 'Rule: ' + self.rule_name

class g_orders(models.Model):
    circulars=models.TextField()
    url=models.TextField()
    def __str__(self):
        return 'Orders: ' + self.circulars

class g_policies(models.Model):
    title=models.TextField()
    document=models.FileField(upload_to='documents')
    img=models.ImageField()
    def __str__(self):
        return 'Policies: ' + self.title

class left_notification(models.Model):
    msg=models.TextField()
    url=models.TextField()
    def __str__(self):
        return 'left Notification: ' + self.msg

class right_notification(models.Model):
    msg=models.TextField()
    url=models.TextField()
    def __str__(self):
        return 'right Notification: ' + self.msg