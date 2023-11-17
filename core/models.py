from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produk(models.Model):
    nama_barang = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to="item_images", null=True, blank=False)
    deskripsi = models.TextField(blank=True,null=True)
    harga = models.PositiveIntegerField()
    jumlah = models.PositiveIntegerField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_barang