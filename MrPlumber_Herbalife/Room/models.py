from django.db import models

# Create your models here.


class Pisos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("nombre", max_length=50)
    descripcion = models.CharField("descripcion", max_length=50, blank=True)
    class Meta:
        ordering = ('id',)

class Codigos(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    creado = models.DateTimeField(auto_now=True)


class Cuartos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("nombre", max_length=50)
    descripcion = models.CharField("descripcion", max_length=50, blank=True)

    # FK Cuarto a Piso
    piso = models.ForeignKey(
        Pisos,
        on_delete=models.CASCADE,
        verbose_name="Cuarto a Pisos"
    )

    # FK Codigo a Codigos
    codigo = models.ForeignKey(
        Codigos,
        on_delete=models.CASCADE,
        verbose_name="Codigo a Codigos",
        null=True
    )


class Accesorios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("nombre", max_length=50)
    descripcion = models.CharField("descripcion", max_length=50, blank=True)

    # FK
    cuarto = models.ForeignKey(
        Cuartos,
        on_delete=models.CASCADE,
        verbose_name="Accesorios a Cuarto"
    )

    codigo = models.ForeignKey(
        Codigos,
        on_delete=True,
        verbose_name="Accesorios a Codigo",
        null=True
    )


class Actividades(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("nombre", max_length=50)
    descripcion = models.CharField("descripcion", max_length=50, blank=True)


class AccesoriosActividades(models.Model):
    id = models.AutoField(primary_key=True)

    # FK
    accesorio = models.ForeignKey(
        Accesorios,
        on_delete=models.CASCADE,
        verbose_name="AccesoriosACT a Actividades"
    )

    actividades = models.ForeignKey(
        Actividades,
        on_delete=models.CASCADE,
        verbose_name="AccesoriosACT a Actividades"
    )


class Reportes(models.Model):
    id = models.AutoField(primary_key=True)
    creado = models.DateTimeField("creado", auto_now=True)
    observaciones = models.TextField("observaciones", blank=True)
    inicio = models.DateTimeField("inicio")
    fin = models.DateTimeField()

    # Fk
    cuarto = models.ForeignKey(
        Cuartos,
        on_delete=models.CASCADE,

    )


class ActividadesRealizadas(models.Model):
    id = models.AutoField(primary_key=True)
    observaciones = models.TextField("observaciones", blank=True)
    realizado = models.DateTimeField("realizado", auto_now=True)

    # FK
    reporte = models.ForeignKey(
        Reportes,
        on_delete=models.CASCADE,
        verbose_name="Realizadas a Reportes"
    )

    actividades = models.ForeignKey(
        Actividades,
        on_delete=models.CASCADE,
        verbose_name="Realizadas a Reportes"
    )

# Refactor/DB
class FocosDeActividad(models.Model):
    id = models.AutoField(primary_key=True)
    colores = models.CharField("colores", max_length=7)
    descripcion = models.CharField("descripcion", max_length=50, blank=True)


class ActividadAlerta(models.Model):
    id = models.AutoField(primary_key=True)
    actividadRealizada = models.ForeignKey(
        ActividadesRealizadas,
        on_delete=models.CASCADE,
        verbose_name= "Focos a Reporte"
    )
    foco = models.ForeignKey(
        FocosDeActividad,
        on_delete=models.CASCADE,
        verbose_name="Reporte de focos a los focos"
    )


'''
poll = models.ForeignKey(
    Poll,
    on_delete=models.CASCADE,
    verbose_name="the related poll",
)
sites = models.ManyToManyField(Site, verbose_name="list of sites")
place = models.OneToOneField(
    Place,
    on_delete=models.CASCADE,
    verbose_name="related place",
)
'''
