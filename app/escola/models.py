from django.db import models
from django.core.validators import MinLengthValidator


class Estudante(models.Model):
    """
    Dados necessários:
                        Id
                        Nome
                        E-mail
                            Não pode estar em branco
                        CPF
                            Máximo de 11 caracteres
                        Data de Nascimento
                        Número de Celular
                            Máximo de 14 caracteres
    
    """
    nome = models.CharField(max_length=80)
    email = models.EmailField(blank=False, max_length=40)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome
    
    

class Curso(models.Model):
    '''
    Dados necessários:
            Id
            Código
                Máximo de 10 caracteres
            Descrição
                Não pode estar em Branco
            Nível (Básico, Intermediário e Avançado)
                Não pode estar em Branco
                Não pode ser Nulo
                Por padrão deve ser Básico
    '''
    
    NIVEL = (
        ('B','Basico'),
        ('I','Intermediario'),
        ('A','Avançado'),
    )
    codigo = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(3)] )
    descricao = models.CharField(blank=False)
    nivel = models.CharField(max_length=1,choices=NIVEL, blank=False, null=False, default='B')
    
    
    def __str__(self):
        return self.codigo
    
    
class Matricula(models.Model):
    PERIODO = (
        ('M','Manha'),
        ('T','Tarde'),
        ('N','Noite'),
        )
    
    estudante = models.ForeignKey(Estudante, on_delete= models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete= models.CASCADE)
    periodo = models.CharField(max_length=1,choices= PERIODO, blank=False, null=False, default='M')
    
  
