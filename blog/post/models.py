from django.db import models

# Create your models here.

# ------- 8
# Declaramos nuestro modelo para las publicaciones de nuestro blog



class Posts(models.Model):
    titulo = models.CharField(max_length=45)
    categoria = models.CharField(max_length=45)
    fecha = models.DateField(auto_now_add=True)
    banner = models.ImageField(upload_to='blog/banners')
    descripcion = models.TextField()
    body = models.TextField()
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural='Posts'
