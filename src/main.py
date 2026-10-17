from datetime import datetime, date
import sys
import unicodedata


def padron(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    pad = nfkd.encode('ASCII', 'ignore').decode('ASCII')
    pad = pad.strip()
    pad = pad.lower()
    return pad

lista_tarefas = []

class Cadastro:
    def __init__(self):
        self.nome = None
        self.dif = None
        self.data = None
        self.restante = None
        self.desc = None
        self.status = "Pendente"
        self.prioridade = None

    def nom(self):
        while True:
            nome = input("Digite o nome da tarefa: ").strip()
            existe = False
            for tarefa in lista_tarefas:
                if padron(tarefa["Nome"]) == padron(nome):
                    existe = True
                    break
            if nome == "":
                print("A tarefa deve ter obrigatoriamente um nome")
            elif existe:
                print("Ja tem uma tarefa com esse nome")
            else:
                desc = input("Digite a descrição: ")
                if desc == "":
                    desc = "Sem descrição"
                self.desc = desc
                self.nome = nome
                return self.nome, self.desc

    def difi(self):
        dif = ''
        while dif == '':
            dif = input("Digite a dificuldade da tarefa (facil, media ou dificil): ")
            dif = padron(dif)
            if dif in ['facil', 'media', 'dificil']:
                if dif == 'facil':
                    self.dif = 'Fácil'
                elif dif == 'media':
                    self.dif = 'Média'
                else:
                    self.dif = 'Difícil'
                return self.dif
            else:
                print("Essa não é uma dificuldade reconhecida, tente novamente")
                dif = ''

    def odata(self):
        hoje = date.today()
        while True:
            try:
                dia, mes, ano = int(input("Dia: ")), int(input("Mês: ")), int(input("Ano: "))
                try:
                    data = date(ano, mes, dia)
                    self.data = data
                    return self.data
                except ValueError:
                    if dia == 0 or mes == 0 or ano == 0:
                        print("Os valores não podem ser nulos")
                    elif dia == 29 and mes == 2:
                        print("O ano não é bisexto")
                    elif dia not in range(1, 31) or mes not in range(1, 13):
                        print("O valor digitado não pertence a uma data real")
                    elif ano not in range(1, 9999):
                        print("O ano está fora do alcance")
            except ValueError:
                print("Valor incorreto adicionado")

    def rest(self):
        a = self.data
        hoje = date.today()
        r = a - hoje
        self.restante = r
        return self.restante

    def calc_prio(self):
        dias = self.restante.days
        if self.dif == 'Difícil':
            peso_dif = 3
        elif self.dif == 'Média':
            peso_dif = 2
        else:
            peso_dif = 1
        
        if dias < 0:
            score = 0
        else:
            score = peso_dif * 100 - dias
        
        self.prioridade = score
        return self.prioridade

    def lista(self):
        a = self.data
        b = datetime.strftime(a, "%d/%m/%Y")
        r = self.restante
        res = r.days
        self.calc_prio()
        
        tarefa_dict = {
            "Nome": self.nome,
            "Descrição": self.desc,
            "Dificuldade": self.dif,
            "Data": b,
            "Prioridade_Score": self.prioridade,
            "Tempo_restante": f"{res} dias",
            "Status": self.status,
            "Data_obj": self.data
        }
        lista_tarefas.append(tarefa_dict)


n = ''
while n == '':
    print(120 * "=")
    print("1. Cadastrar nova tarefa \n2. Visualizar tarefas cadastradas \n3. Marcar tarefa como concluída \n4. Sair da aplicação")
    try:
        n = int(input("Digite a opção que desejar: "))
    except ValueError:
        n = ''
        print("Opção invalida, por favor tente novamente")
    print(120 * "=")
    
    if n not in range(1, 5):
        print("Opção invalida, por favor tente novamente")
        n = ''
    elif n == 1:
        c = Cadastro()
        c.nom()
        c.difi()
        c.odata()
        c.rest()
        c.lista()
        n = ''
    elif n == 2:
        if not lista_tarefas:
            print("A lista de tarefas está vazia")
        else:
            hoje = date.today()
            print("Tarefas pendentes e no prazo")
            pendentes = [t for t in lista_tarefas if t["Status"] == "Pendente" and t["Data_obj"] >= hoje]
            pendentes = sorted(pendentes, key=lambda x: x["Prioridade_Score"], reverse=True)
            for t in pendentes:
                print(f"Nome: {t['Nome']} | Descrição: {t['Descrição']} | Dificuldade: {t['Dificuldade']} | Data: {t['Data']} | Tempo Restante: {t['Tempo_restante']} | Status: {t['Status']}")

            print("Tarefas atrasadas")
            atrasadas = [t for t in lista_tarefas if t["Status"] == "Pendente" and t["Data_obj"] < hoje]
            for t in atrasadas:
                print(f"Nome: {t['Nome']} | Descrição: {t['Descrição']} | Dificuldade: {t['Dificuldade']} | Data: {t['Data']} | Tempo Restante: {t['Tempo_restante']} | Status: Atrasada")

            print("Tarefas concluidas")
            concluidas = [t for t in lista_tarefas if t["Status"] == "Concluída"]
            for t in concluidas:
                print(f"Nome: {t['Nome']} | Descrição: {t['Descrição']} | Dificuldade: {t['Dificuldade']} | Data: {t['Data']} | Status: {t['Status']}")
        n = ''
    elif n == 3:
        if not lista_tarefas:
            print("A lista de tarefas está vazia")
        else:
            nome_busca = input("Digite o nome da tarefa que deseja marcar como concluída: ").strip()
            encontrado = False
            for t in lista_tarefas:
                if padron(t["Nome"]) == padron(nome_busca):
                    t["Status"] = "Concluída"
                    print("Tarefa marcada como concluída com sucesso")
                    encontrado = True
                    break
            if not encontrado:
                print("Tarefa não encontrada")
        n = ''
    elif n == 4:
        print("Finalizando o programa")
        sys.exit()