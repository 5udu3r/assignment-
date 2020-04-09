from django.db import models
from django.contrib.auth.models import AbstractUser


class Agencies(models.Model):
    name = models.CharField(max_length=255, default='noname')
    parent = models.CharField(max_length=255, default='noname')
    credibility_rate = models.CharField(max_length=255, default='noname')


class News(models.Model):
    NEWS_API = 'N'
    RED = 'R'  # reddit
    SOURCES = (
        (NEWS_API, 'NEWS API'),
        (RED, 'REDDIT'),
     )
    headline = models.CharField(max_length=255, default='noname')
    link = models.CharField(max_length=255, default='noname')
    source = models.CharField(max_length=1, choices=SOURCES, default=NEWS_API, blank=True, null=True)
    agency = models.ForeignKey(Agencies, on_delete=models.CASCADE)
    country = models.CharField(max_length=2, default='noname')
    author = models.CharField(max_length=128, default='noname')
    urlToImage = models.CharField(max_length=512, default='noname')
    publishedAt = models.DateTimeField(max_length=64, default='noname')


class SearchResults(models.Model):
    """
        ... to Save The Search Results
    """
    keyword = models.CharField(max_length=255, default='noname')
    date_time = models.DateTimeField()


class User(AbstractUser):
    DIPLOMA = 'DI'
    BACH = 'BA'
    MASTER = 'MA'
    DOC = 'DO'
    POSTDOC = 'PD'
    FREE = 'FR'
    LAST_DEGREE = (
        (DIPLOMA, 'Diploma'),
        (BACH, 'Bachelor'),
        (MASTER, 'Master'),
        (DOC, 'Doctorate'),
        (POSTDOC, 'Post Doctorate'),
        (FREE, 'Free'),
    )
    ENGLISH = 'EN'
    PERSIAN = 'FA'
    LANGUAGE = (
        (ENGLISH, 'English'),
        (PERSIAN, 'Persian'),
    )
    VALIDATE = 'Y'
    UNVALIDATE = 'N'
    STATUS = (
        (VALIDATE, 'Validate'),
        (UNVALIDATE, 'Unvalidate'),
    )
    PAID = 'P'
    UNPAID = 'U'
    WAITING = 'W'
    PAY_STATUS = (
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
        (WAITING, 'Waiting')
     )
    DABIR = 'DB'
    DAVAR = 'DV'
    USER = 'US'
    WORKSHOP = 'WS'
    NAZER= 'NZ'
    ADMIN= 'AD'
    WRITER= 'WR'
    SCI_COM= 'SCI'
    EXE_COM= 'EXE'
    SUPERADMIN= 'SU'
    TYPE = (
        (USER, 'User'),
        (WORKSHOP, 'Workshop'),
        (SCI_COM, 'Scientific Committee '),
        (EXE_COM, 'Executive Committee'),
        (DABIR, 'Dabir'),
        (DAVAR, 'Davar'),
        (WRITER, 'Writer'),
        (NAZER, 'Nazer'),
        (ADMIN, 'Admin'),
        (SUPERADMIN, 'SuperAdministrator'),


    )
    ACTIVE = '1'
    DISABLE = '0'
    MAIL = (
        (ACTIVE, 'Active'),
        (DISABLE, 'Disabled'),
    )

    SEND_ARTICLE = 'SA'
    JUST_VISIT = 'JV'
    POINT = (
        (SEND_ARTICLE, 'Send Article'),
        (JUST_VISIT, 'Just Visit'),
     )
    ONLINE = '1'
    OFFLINE = '0'
    ACTIVITY = (
        (ONLINE, 'Online'),
        (OFFLINE, 'Offline'),
     )

    name = models.CharField(max_length=255,default='noname')
    family = models.CharField(max_length=255, blank=True, null=True)
    last_degree = models.CharField(max_length=255, choices=LAST_DEGREE, default=FREE,  blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    activity = models.CharField(max_length=255,choices=ACTIVITY, default=OFFLINE, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    institute = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    expertise = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    mail = models.CharField(max_length=255,blank=True, null=True)
    mail_verify = models.CharField(max_length=255, choices=MAIL, default=DISABLE, blank=True, null=True)
    tracking_code = models.CharField(max_length=255, blank=True, null=True)
    agent = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    registration_date = models.CharField(max_length=255, blank=True, null=True)
    pic = models.CharField(max_length=255, blank=True, null=True)
    point = models.CharField(max_length=255, choices=POINT, default=SEND_ARTICLE, blank=True, null=True)
    pay_sts = models.CharField(max_length=255, choices=PAY_STATUS, default=WAITING, blank=True, null=True)
    scan_id = models.CharField(max_length=255, blank=True, null=True)
    scan_bc = models.CharField(max_length=255, blank=True, null=True)
    document_validation_sts = models.CharField(max_length=1, choices=STATUS, default=UNVALIDATE, blank=True, null=True)
    acl = models.CharField(max_length=255, choices=TYPE, default=USER, blank=True, null=True)



