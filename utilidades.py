from time import sleep

incompletas = []
completas = []
tarefas = []
tarefa_nome = ''

class Cabecalho:
    def __init__(self):
        print("~"*25)
        print("    LISTA DE TAREFAS")
        print("~"*25)
        print("Opções:")
        print()
        print("[1] Criar tarefa\n[2] Mostrar tarefas\n[3] Sair\n")
        
          
class Opcoes:
    def __init__(self):
        while True:
            opc = input("Opção: ")
            if opc.isnumeric() and int(opc) <= 3:
                break
            print("Opção invalida")
        
        
        if opc == '1':
            while True:
                tarefa_nome = input("Nome da tarefa: ").upper()
                tarefas.append(tarefa_nome)
                incompletas.append(tarefa_nome)
                print("Tarefa adicionada!")
                sleep(0.5)
                saida = input("Tem mais alguma tarefa a ser adicionada? (Sim ou não)\n").upper()[0]
                if saida == 'N':
                    break
            sleep(0.5)
            Cabecalho()
            Opcoes()
    
                    
        if opc == '2':
            if len(incompletas) == 0:
                print("Você não tem tarefas pendentes\n")
                sleep(0.4)
                Cabecalho()
                Opcoes()
            else:
                while True:
                    print("Suas tarefas incompletas até o momento são: ")
                    for v in incompletas:
                        print(f"    {v}")
                    print("Qual você quer mudar o status?\n")
                    conf = str(input("Opção: ")).upper()
                    if conf not in incompletas:
                        print("\nOpção Inexistente ...\n")
                    else:
                        break
                status = str(input("Essa tarefa está completa ou incompleta?\n")).upper()[0]
                if conf in tarefas and status == 'C':
                    completas.append(conf)
                    incompletas.remove(conf)
                    print("\n  Essa tarefa foi feita!\n")
                    sleep(0.5)
                elif conf in tarefas and status == 'I':
                    incompletas.append(conf)
                    print("\n  Essa tarefa precisa ser feita ainda!\n")
                    sleep(0.5)
                Cabecalho()
                Opcoes()
        
                        
        if opc == '3':
            print("Finalizando aplicativo...")
            sleep(0.5)
        