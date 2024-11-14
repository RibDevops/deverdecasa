from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime
from login.models import User 

# **Model Escola**
class Escola(models.Model):
    nome_escola = models.CharField(max_length=100, verbose_name="Nome da escola")

    def __str__(self):
        return self.nome_escola

# **Model Turma - Alteração: Correção no __str__ para retornar o nome da turma**
class Turma(models.Model):
    fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="turma_escola", verbose_name="Nome da escola")
    turma = models.CharField(max_length=100, verbose_name="Nome da turma")

    def __str__(self):
        # **Alteração:** Antes retornava `self.nome_escola`, que não existe nesta model.
        # **Motivo:** Para evitar erro de atributo não definido.
        return self.turma

# **Model Materia**
class Materia(models.Model):
    nome_materia = models.CharField(max_length=100, verbose_name="Nome da matéria")

    def __str__(self):
        return self.nome_materia

# **Model Professor**
class Professor(models.Model):
    fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="professores_escola", verbose_name="Nome da escola")
    fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="professor_materias", verbose_name="Matéria")
    nome_professor = models.CharField(max_length=100, verbose_name="Nome do Professor")

    def __str__(self):
        return self.nome_professor

# **Model Livro**
class Livro(models.Model):
    fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="livro_materia", verbose_name="Matéria")
    nome_livro = models.CharField(max_length=100, verbose_name="Nome do livro")

    def __str__(self):
        return self.nome_livro

# **Model Aluno**
class Alunos(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aluno_user', verbose_name="Responsável")
    fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="aluno_escola", verbose_name="Escola")
    fk_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="aluno_turma", verbose_name="Turma")
    nome_aluno = models.CharField(max_length=100, verbose_name="Nome do aluno")

    def __str__(self):
        return self.nome_aluno

# **Model DeverDeCasa - Alterações: Melhorias nos métodos**
class DeverDeCasa(models.Model):
    fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="dever_escola", verbose_name="Escola")
    fk_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="dever_professor", verbose_name="Professor")  # **Alteração:** Nome do related_name para evitar confusão.
    fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="dever_materia", verbose_name="Matéria")  # **Alteração:** Adicionado related_name para evitar erros de relacionamento.
    fk_livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, blank=True, related_name="dever_livro", verbose_name="Livro")  # **Alteração:** Adicionado related_name para evitar erros de relacionamento.
    dever = models.TextField(verbose_name="Dever de casa")
    data_entrega = models.DateField(verbose_name="Data da entrega")
    data_postagem = models.DateTimeField(auto_now_add=True)

    # **Método horas_restantes - Alteração: Simplificação**
    def horas_restantes(self):
        # **Motivo:** Simplificar o cálculo de horas restantes.
        agora = datetime.now()
        delta = self.data_entrega - date.today()
        return delta.total_seconds() / 3600  # **Alteração:** Usar total_seconds() para considerar todos os segundos.

    # **Método dias_para_entrega - Sem Alterações**
    def dias_para_entrega(self):
        return (self.data_entrega - date.today()).days

    # **Método data_formatada - Alteração: Simplificação**
    def data_formatada(self):
        # **Motivo:** Simplificar a formatação da data.
        return self.data_entrega.strftime("%d %a")  # **Alteração:** Usar %a para o dia da semana abreviado.

    def __str__(self):
        # **Alteração:** Melhorar a formatação da string de retorno.
        return f"Dever de {self.fk_materia.nome_materia} - {self.dever[:20]}... - {self.data_formatada()}"

# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from datetime import date, datetime

# # Definição da classe Escola
# class Escola(models.Model):
#     nome_escola = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_escola

# # Definição da classe Turma
# class Turma(models.Model):
#     fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="turma_escola")
#     turma = models.CharField(max_length=100)

#     def __str__(self):
#         # Correção do retorno para o nome da turma
#         return self.turma  # Alteração: `self.nome_escola` foi substituído por `self.turma` para retornar o nome da turma corretamente.

# # Definição da classe Materia
# class Materia(models.Model):
#     nome_materia = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_materia

# # Definição da classe Professor
# class Professor(models.Model):
#     fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="professores_escola")
#     fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="materias_professor")
#     nome_professor = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_professor

# # Definição da classe Livro
# class Livro(models.Model):
#     fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="materias_livro")
#     nome_livro = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_livro

# # Definição da classe Aluno
# class Aluno(models.Model):
#     fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="alunos")
#     fk_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="turma_aluno")
#     nome_aluno = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_aluno

# # Definição da classe DeverDeCasa
# class DeverDeCasa(models.Model):
#     fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="deveres")
#     fk_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="deveres")
#     fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
#     fk_livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, blank=True)
#     dever = models.TextField()
#     data_entrega = models.DateField()
#     data_postagem = models.DateTimeField(auto_now_add=True)

#     def horas_restantes(self):
#         agora = datetime.now()
#         # Converte `self.data_entrega` para `datetime` com a mesma hora de `agora`
#         data_entrega_datetime = datetime.combine(self.data_entrega, agora.time())
#         delta = data_entrega_datetime - agora
#         return delta.total_seconds() // 3600  # Retorna as horas restantes

#     def dias_para_entrega(self):
#         # Retorna o número de dias até o prazo de entrega
#         return (self.data_entrega - date.today()).days

#     def data_formatada(self):
#         # Listas de dias da semana em inglês e português
#         dias_da_semana_ingles = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#         dias_da_semana_portugues = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

#         # Formata o dia da semana em português
#         dia_semana_ingles = self.data_entrega.strftime("%a")
#         dia_semana_portugues = dias_da_semana_portugues[dias_da_semana_ingles.index(dia_semana_ingles)]

#         # Retorna no formato desejado: "08 seg"
#         return self.data_entrega.strftime(f"%d {dia_semana_portugues}")

#     def __str__(self):
#         # Corrige o uso de `self.data_formatada()` ao invés de `self.dever.data_formatada()`
#         return f"Dever de {self.fk_materia.nome_materia} - {self.dever} - {self.data_formatada()}"
#         # Motivo: `self.data_formatada()` é o método da instância, o uso anterior `self.dever.data_formatada()` causaria erro.
















# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.db import models
# from datetime import date
# from datetime import datetime
# from datetime import datetime, date

# class Escola(models.Model):
#     nome_escola = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_escola

# class Turma(models.Model):
#     fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="turma_escola")
#     turma = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_escola
    
# class Materia(models.Model):
#     nome_materia = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_materia

# class Professor(models.Model):
#     fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="professores_escola")
#     fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="materias_professor")
#     nome_professor = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_professor


# class Livro(models.Model):
#     fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="materias_livro")
#     nome_livro = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_livro

# class Aluno(models.Model):
#     fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="alunos")
#     fk_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="turma_aluno")
#     nome_aluno = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome_aluno

# class DeverDeCasa(models.Model):
#     fk_escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="deveres")
#     fk_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="deveres")
#     fk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
#     fk_livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, blank=True)
#     dever = models.TextField()
#     data_entrega = models.DateField() 
#     data_postagem = models.DateTimeField(auto_now_add=True)

#     def horas_restantes(self):
#         agora = datetime.now()
#         # Converte `self.data_entrega` para um objeto `datetime` no mesmo horário de `agora`
#         data_entrega_datetime = datetime.combine(self.data_entrega, agora.time())
#         delta = data_entrega_datetime - agora
#         return delta.total_seconds() // 3600  # Retorna as horas restantes

    
#     def dias_para_entrega(self):
#         # Retorna a quantidade de dias para o prazo de entrega
#         return (self.data_entrega - date.today()).days
    
#     def data_formatada(self):
#         # Lista de dias da semana em inglês
#         dias_da_semana_ingles = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#         # Lista de dias da semana em português
#         dias_da_semana_portugues = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
        
#         # Formatar a data para o dia e o dia da semana em inglês
#         dia_semana_ingles = self.data_entrega.strftime("%a")  # Exemplo: 'Mon', 'Tue', etc.
#         dia_semana_portugues = dias_da_semana_portugues[dias_da_semana_ingles.index(dia_semana_ingles)]
        
#         # Retornar a data no formato desejado: "08 seg"
#         return self.data_entrega.strftime(f"%d {dia_semana_portugues}")


#     def __str__(self):
#         return f"Dever de {self.fk_materia.nome_materia} - {self.dever} - {self.dever.data_formatada()}"


