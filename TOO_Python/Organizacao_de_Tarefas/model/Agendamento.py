from datetime import date, time, datetime, timedelta


class Agendamento:
    def __init__(
        self, data_inicio=None, data_fim=None, atividade=None, nome=None, local=None
    ):
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.atividade = atividade
        self.nome = nome
        self.local = local

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_ini):
        if data_ini is None:
            self.__data_inicio = None
            return
        try:
            # Tenta converter a data no formato com hífens
            temporario = datetime.strptime(data_ini, "%d-%m-%Y")
            self.__data_inicio = temporario.date()
        except ValueError:
            # Se falhar, AVISA o erro e LEVANTA uma nova exceção para parar o processo.
            # Isso força o 'except' do seu programa principal a ser acionado.
            # o try excpt captura erros que acontecem sozinhos já o raize ele cria um erro intencional
            raise ValueError(
                f"ERRO: Data '{data_ini}' em formato inválido. Use DD-MM-YYYY."
            )

    @property
    def data_fim(self):
        return self.__data_fim

    @data_fim.setter
    def data_fim(self, data_f):
        if data_f is None:
            self.__data_fim = None
            return
        try:
            temporario = datetime.strptime(data_f, "%d-%m-%Y")
            self.__data_fim = temporario.date()
        except ValueError:
            # mesma logica utilizada no de cima
            raise ValueError(
                f"ERRO: Data '{data_f}' em formato inválido. Use DD-MM-YYYY."
            )

    @property
    def atividade(self):
        return self.__atividade

    @atividade.setter
    def atividade(self, ativ):
        self.__atividade = ativ

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome_atv):
        self.__nome = nome_atv

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, loc_atv):
        self.__local = loc_atv

    def __str__(self):
        infos_taref = f"\nAGENDAMENTO: \nNome: {self.nome}\nAtividade: {self.atividade} \nLocal: {self.local} \nData início: {self.data_inicio} \nData final: {self.data_fim}"
        return infos_taref
    
    def exibir_dados(self):
        infos = "\nAGENDAMENTO"
        if self.nome != None:
            infos += f"\nNome: {self.nome}"

        if self.atividade != None:
            infos += f"\nAtividade: {self.atividade}"

        if self.local != None:
            infos += f"\nLocal: {self.local}"

        if self.data_inicio != None:
            infos += f"\nData início: {self.data_inicio}"

        if self.data_fim != None:
            infos += f"\nData final: {self.data_fim}"

        return infos