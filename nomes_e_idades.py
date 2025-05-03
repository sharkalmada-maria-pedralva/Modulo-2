from time import sleep

print("""
------------------------
Manipulação de ficheiros
------------------------
""")
name = input("Nome do ficheiro para abrir: \n>>>")
print("""
Aqui está o conteúdo do ficheiro aberto:
""")
with open(f"{name}.txt", 'r') as ficheiro:
    linhas = ficheiro.readlines()
    for linha in linhas:
        print(linha)

while True:
    sleep(2)
    nmi=input("""
----------------MENU----------------
Quer adicionar mais um nome e idade? 

0)Sair
1)Adicionar nome e idade
2)Procurar nome e idade
3)Ler o conteúdo do ficheiro
>>>
------------------------------------
""")
    if nmi =="1":
        conteudo = input("""
------------------------------------------
Digite o nome e a idade que quer adicionar 
>>>""")
        with open(f"{name}.txt", 'a', encoding="utf-8") as ficheiro:
            ficheiro.write(conteudo + "\n")
        print("Feito!")
    elif nmi == "2":
        palavra = input("Que nome gostaria de procurar? \n>")
        with open(f"{name}.txt", "r", encoding='utf-8') as ficheiro:
            for linha in ficheiro:
                if palavra in linha:
                    print("Aqui esta seu resultado:")
                    print(linha.rstrip())
    elif nmi == "3":
        print("""
Aqui está o conteúdo do ficheiro aberto:
        """)
        with open(f"{name}.txt", 'r') as ficheiro:
            linhas = ficheiro.readlines()
            for linha in linhas:
                print(linha)
    else:
        print("Até à próxima!")
        break



