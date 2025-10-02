class Disciplina:
    def __init__ (self, nome = None, curso = None, carga_horaria = None, professor = None):
        self.nome = nome
        self.curso = curso
        self.carga_horaria = carga_horaria
        self.professor = professor

        # eu deixo os __ caso eu não quero mais alterar,
        # botei um curso e não vou mais alterar não posso mais alterar
        # tendo um setter eu posso mudar ela e retiro o __

    @property  # sempre tem um retorno
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome_disciplina):
        self.__nome = nome_disciplina.strip().title()

    @property
    def curso (self):
        return self.__curso
    
    @curso.setter
    def curso (self, nome_curso):
        self.__curso = nome_curso

    @property
    def carga_horaria (self):
        return self.__carga_horaria
    
    @carga_horaria.setter
    def carga_horaria (self, total_horas_curso):
        if total_horas_curso > 0 :
            self.__carga_horaria = total_horas_curso
            return
        else:
            raise ValueError("A carga horaria deve ser maior que ZERO !!!")
        
    @property
    def professor (self):
        return self.__professor
    
    @professor.setter
    def professor (self, nome_professor):
        self.__professor = nome_professor

    def __str__(self):
        return f"{self.nome} ({self.curso})"
    
    def exibir_dados(self):
        Vou_exibir = "Diciplina:\n"

        if self.nome != None:
            Vou_exibir += self.nome

        if self.curso != None:
            Vou_exibir += f" ({self.curso})\n"

        if self.carga_horaria != None:
            Vou_exibir += f"Carga horaria: {self.carga_horaria}\n"

        if self.professor != None:
            Vou_exibir += f"Prof: {self.__professor}\n"

        return Vou_exibir