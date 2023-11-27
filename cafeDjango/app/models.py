from django.db import models

class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
    def __str__(self):
        return f'{self.nome_cidade} {self.uf}'
    
class Cargo(models.Model):
    nomeCargo = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
    def __str__(self):
        return self.nomeCargo
    
class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    class Meta:
            verbose_name = "Usuario"
            verbose_name_plural = "Usuarios"
    def __str__(self):
        return f'{self.nome_usuario} {self.cpf} {self.cargo} {self.cidade}'


class Fazenda(models.Model):
    nomeFazenda = models.CharField(max_length=50)
    altitude = models.IntegerField()
    areaTotal = models.IntegerField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    nomeRodoviaKm = models.CharField(max_length=70)
    class Meta:
        verbose_name = "Fazenda"
        verbose_name_plural = "Fazendas"
    def __str__(self):
        return f'{self.nomeFazenda} {self.altitude} {self.areaTotal} {self.cidade} {self.nomeRodoviaKm}'

class AreaPlantio(models.Model):
    nomeFazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE) 
    area_plantio = models.IntegerField()
    class Meta:
        verbose_name = "Area Plantio"
        verbose_name_plural = "Areas Plantio"
    def __str__(self):
        return f'{self.nomeFazenda} {self.area_plantio}'

class Talhoes(models.Model):
    nomeFazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE) 
    area_talhoes = models.IntegerField()
    class Meta:
        verbose_name = "Talhao"
        verbose_name_plural = "Talhoes"
    def __str__(self):
        return f'{self.nomeFazenda} {self.area_talhoes}'

class TexturaSolo(models.Model):
    tipoSolo = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Textura Solo"
        verbose_name_plural = "Texturas Solo"
    def __str__(self):
        return self.tipoSolo

class AnaliseSolo(models.Model):
    ph = models.FloatField()
    textura = models.ForeignKey(TexturaSolo, on_delete=models.CASCADE)
    materia_organica_porcentagem = models.IntegerField()
    qtde_Calcio = models.FloatField()
    qtde_Magnesio = models.FloatField()
    qtde_Potassio = models.FloatField()
    class Meta:
        verbose_name = "Analise Solo"
        verbose_name_plural = "Analise Solos"
    def __str__(self):
        return f'{self.ph} {self.textura} {self.materia_organica_porcentagem} {self.qtde_Calcio} {self.qtde_Magnesio} {self.qtde_Potassio}'

class Exportadora(models.Model):
    nome_exportadora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Exportadora"
        verbose_name_plural = "Exportadoras"
    def __str__(self):
        return f'{self.nome_exportadora} {self.cnpj} {self.endereco} {self.cidade}'
