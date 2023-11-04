from django.db import models

# Create your models here.
class Kategoriler(models.Model):
    isim=models.CharField(max_length=80)
    aciklama=models.TextField()

    def __str__(self):
        return self.isim

    class Meta:
        verbose_name="Kategori"
        verbose_name_plural="Kategoriler"

class Haberler(models.Model):
    isim=models.CharField(max_length=150)
    aciklama=models.TextField()
    eklenme_tarihi=models.DateField()
    video=models.TextField()
    kategori=models.ManyToManyField(Kategoriler)
    eklenme_tarih=models.DateTimeField(auto_now_add=True)
    kapak=models.CharField(max_length=200)
    kaynak=models.CharField(max_length=200)
    ulke=models.CharField(max_length=150)

    def __str__(self):
        return self.isim
    class Meta:
        verbose_name="Haberler"
        verbose_name_plural="Haberler"

class Ekonomi(models.Model):
    isim=models.CharField(max_length=200)
    aciklama=models.TextField()
    kapak=models.ImageField(upload_to="images",default="Ekonomi.png")
    def __str__(self):
        return self.isim

    class Meta:
        verbose_name="Ekonomi"
        verbose_name_plural="Ekonomi"

class Sondakika(models.Model):
    isim=models.CharField(max_length=120)
    sira=models.IntegerField()
    tarih=models.DateField()
    Ekonomi=models.ForeignKey(Ekonomi,on_delete=models.CASCADE)
    def __str__(self):
        return self.isim
    class Meta:
        verbose_name="Sondakika"
        verbose_name_plural="Son Dakika"

class Gündem(models.Model):
    isim=models.CharField(max_length=200)
    sira=models.IntegerField()
    tarih=models.DateField()
    eklenme_tarihi=models.DateTimeField(auto_now_add=True)
    video=models.TextField()
    video2=models.TextField(default="")
    aciklama=models.TextField()

    def __str__(self):
        return self.isim

    class Meta:
        verbose_name="Gündem"
        verbose_name_plural="Gündem"
