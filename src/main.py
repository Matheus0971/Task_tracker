from datetime import datetime, date
import sys
import unicodedata


def padron(texto):
    nfkd=unicodedata.normalize('NFKD',texto)
    pad=nfkd.encode('ASCII', 'ignore').decode('ASCII')
    pad=pad.strip()
    pad=pad.lower()
    return pad
lista_tarefas=[]

##################################################
class cadastro:
    def __init__(self):
        self.nome=None
        self.dif=None
        self.data=None
        self.restante=None
        self.desc=None
    def nom(self):
        nome=""
        lis=None
        while True:
            nome=input("Digite o nome da tarefa: ").strip()
            for i in range (len(lista_tarefas)):
                lis=lista_tarefas[i]["Nome"]
            if nome == "":
                print("A tarefa deve ter obrigatoriamente um nome")
            elif nome == lis :
                print("Ja tem uma tarefa com esse nome")
            else :  
                desc=input("Digite a descrição: ")
                if desc == '':
                    desc="Sem descrição"
                self.desc=desc
                self.nome=nome
                return self.nome, self.desc
    def difi(self):
        dif=''
        while dif == '': 
            dif=input("Digite a dificuldade da tarefa(fácil, média ou difícil): ")
            dif=padron(dif)
            if dif == 'facil' or dif == 'media' or dif == 'dificil':
                if dif == 'facil':
                    dif= "Fácil"
                elif dif =='media':
                    dif ="Média"
                elif dif =="dificil":
                    dif="Difícil"
                self.dif=dif
                return self.dif
            else:
                print("Essa não é uma dificuldade reconhecida, tente novamente")
                dif=''
    def odata(self):
        hoje=date.today()
        while True:
            try:
                dia,mes,ano=int(input("Dia:")),int(input("Mês:")),int(input("Ano:"))
                try:
                    data=date(ano,mes,dia)
                    if data < hoje:
                        print("A data não pode ser anterior ao dia de hoje")
                        data=''
                    else:
                        self.data=data
                        return self.data
                except ValueError :
                    if dia ==0 or mes ==0 or ano ==0 :
                        print("Os valores não podem ser nulos")
                    elif dia == 29 and mes ==2 :
                        print("O ano não é bisexto")
                    elif dia not in range(1,31) or mes not in range (1,12) :
                        print("O valor digitado não pertence a uma data real")
                    elif ano not in range(1, 9999):
                        print("O ano está fora do alcance")
                    data=''
            except ValueError:
                print("Valor incorreto adicionado")
    def rest(self):
        a=self.data
        hoje=date.today()
        r=a-hoje
        self.restante=r
        return self.restante

    def prio(self):
        for i in range (len(lista_tarefas)):
            t=lista_tarefas[i]['Tempo_restante']
            print(t)

    def lista(self):
        a=self.data
        b=datetime.strftime(a,"%d/%m/%Y")
        r=self.restante
        res=r.days
        self.nome={
            "Nome": self.nome,
            "Descrição": self.desc,
            "dificuldade" : self.dif ,
            "data": b,
            "status": "Pendente",
            "Prioridade": "r",
            "Tempo_restante": (f"{res} dias")
            }
        lista_tarefas.append(self.nome)


##################################################################################################
n=''
while n == '' :
    print(120*"=")
    print("1.Cadastrar nova tarefa \n2.Visualizar tarefas cadastradas \n3.Sair da aplicação")
    try :
        n=int(input("Digite a opção que desejar: "))
    except :
        ValueError
        n=''
        print("Opção invalida, por favor tente novamente")
    print(120*"=")
    if n not in range(1,4):
        print("Opção invalida, por favor tente novamente")
        n=''
    if n == 1:
        c=cadastro()
        c.nom()
        c.difi()
        c.odata()
        c.rest()
        c.lista()
        c.prio()
        n=''
    elif n ==2:
        if (lista_tarefas) == []:
            print("A lista de tarefas está vazia")

        else :
            for i in range (len(lista_tarefas)):
                print(lista_tarefas[i])


        n=''
    elif n== 3 :
        print("Finalizando o programa")
        sys.exit()








#############################################################################
