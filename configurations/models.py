from django.db import models

class Surface(models.Model):
    surface_id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name="surface")

    def __str__(self):
        return self.nom or f"Surface {self.surface_id}"

    
class Pays(models.Model):
    iso = models.CharField(max_length=3, primary_key=True)
    nom = models.CharField(("nom"), max_length=255)

    def __str__(self):
        return "Pays = f{self.nom}"

class Groupe(models.Model):
    groupe_id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=8, verbose_name="groupe")

    def __str__(self):
        return f"Groupe {self.nom}"

class Poste(models.Model):
    poste_id = models.IntegerField(primary_key=True)
    poste = models.CharField(max_length=4)
    nom = models.CharField(max_length=100, verbose_name="poste")
    groupe_id = models.ForeignKey(Groupe, on_delete=models.CASCADE)

class Club(models.Model):
    club_id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255, verbose_name="nom")
    ville = models.CharField(verbose_name="ville", max_length=255)
    annee_creation = models.IntegerField(verbose_name="annee_creation", null=True, blank=True)
    stade_nom = models.CharField(verbose_name="stade_nom", max_length=255, null=True, blank=True)
    stade_annee_creation = models.IntegerField(verbose_name="stade_annee_creation", null=True, blank=True)
    stade_capacite = models.IntegerField(verbose_name="stade_capacite", default=0, null=True, blank=True)
    surface_id = models.ForeignKey(Surface, on_delete=models.CASCADE)

class Joueur(models.Model):
    joueur_id = models.AutoField(primary_key=True)
    nom = models.CharField(verbose_name="nom", max_length=255)
    prenom = models.CharField(verbose_name="prenom", null=True, blank=True, max_length=255)
    date_naissance = models.DateField(verbose_name="date_naissance", null=True, blank=True)
    poste_id = models.ForeignKey(Poste, on_delete=models.CASCADE)
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    iso = models.ForeignKey(Pays, on_delete=models.CASCADE)

    def __str__(self):
        return f"{nom}_{prenom}"    
    
