from django.db import models


class Contact(models.Model):
    number = models.CharField(max_length=100, verbose_name="Phone Number:", null=True, blank=True)
    mail = models.CharField(max_length=100, verbose_name="Email:", null=True, blank=True)
    location = models.CharField(max_length=100, verbose_name="Location:", null=True, blank=True)
    slogan = models.CharField(max_length=100, verbose_name="Slogan:", null=True, blank=True)


class Project(models.Model):
    title = models.TextField(max_length=1000, verbose_name="Title:", null=True, blank=True)
    title2 = models.TextField(max_length=100, verbose_name="Title 2:", null=True, blank=True)
    title3 = models.TextField(max_length=1000, verbose_name="Title 3:", null=True, blank=True)
    context = models.TextField(verbose_name="Content: ", null=True, blank=True)
    features_1 = models.CharField(max_length=100, verbose_name="Futures 1:", null=True, blank=True)
    features_2 = models.CharField(max_length=100, verbose_name="Futures 2:", null=True, blank=True)
    features_3 = models.CharField(max_length=100, verbose_name="Futures 3:", null=True, blank=True)
    features_4 = models.CharField(max_length=100, verbose_name="Futures 4:", null=True, blank=True)


class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title:", null=True, blank=True)
    title_1 = models.CharField(max_length=100, verbose_name="Title:", null=True, blank=True)
    # 1
    title1 = models.CharField(max_length=100, verbose_name="Title:", null=True, blank=True)
    text1 = models.TextField(max_length=100, verbose_name="Text:", null=True, blank=True)
    photo1 = models.FileField(verbose_name="Photo: ", null=True, blank=True)
    # 2
    title2 = models.CharField(max_length=100, verbose_name="Title:", null=True, blank=True)
    text2 = models.CharField(max_length=100, verbose_name="Text:", null=True, blank=True)
    photo2 = models.FileField(verbose_name="Photo: ", null=True, blank=True)
    # 3
    title3 = models.CharField(max_length=100, verbose_name="Title:", null=True, blank=True)
    text3 = models.CharField(max_length=100, verbose_name="Text:", null=True, blank=True)
    photo3 = models.FileField(verbose_name="Photo: ", null=True, blank=True)
    # 4
    title4 = models.CharField(max_length=100, verbose_name="Title:", null=True, blank=True)
    text4 = models.CharField(max_length=100, verbose_name="Text:", null=True, blank=True)
    photo4 = models.FileField(verbose_name="Photo: ", null=True, blank=True)


class Contact_Us(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title:", null=True, blank=True)
    title1 = models.TextField(max_length=100, verbose_name="Title 2:", null=True, blank=True)
    text = models.CharField(max_length=100, verbose_name="Text:", null=True, blank=True)


class Contact_Us_Punk(models.Model):
    title = models.CharField(max_length=100, verbose_name="Text:", null=True, blank=True)

