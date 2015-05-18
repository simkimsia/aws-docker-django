from django.db import models

# Create your models here.
class ReportTemplate(models.Model):
    title = models.CharField(max_length=50)
    markup = models.TextField(default = 'markup here...')
    styles = models.TextField(default = 'styles here...')

    # __unicode__ on Python 2
    # __str__ on Python 3
    def __unicode__(self):
        return self.title

class Report(models.Model):
    """docstring for Report"""
    title = models.CharField(max_length=50)
    commodity = models.CharField(max_length=10)
    date = models.DateTimeField('date traded')
    trade_period = models.CharField(max_length=10, default='open')
    quantity_cutoff = models.IntegerField(default=0)
    printed = models.BooleanField(default=0)
    datetime_email_sent = models.DateTimeField('date email sent', blank=True, null=True)
    data = models.TextField(default = 'data here...')
    template = models.ForeignKey(ReportTemplate)
    # __unicode__ on Python 2
    # __str__ on Python 3
    def __unicode__(self):
        return self.title