print("\nManipulação de ficheiros\n")
name = input("Nome do ficheiro \n>")
with open(f"{name}.txt", 'r') as ficheiro:
    linhas = ficheiro.readlines()
    for linha in linhas:
        print(linha)

while True:
    nmi=input("\nQuer adicionar mais um nome e idade? \n1)Sim \n2)Não \n3)Procurar nome e idade\n \n>")
    if nmi =="1":
        conteudo = input("Digite o nome e a idade \n>")
        with open(f"{name}.txt", 'a', encoding="utf-8") as ficheiro:
            ficheiro.write(conteudo + "\n")
        print("Feito!")
    elif nmi == "2":
        print("Até a próxima.")
        break
    else:
        palavra = input("Que palavra gostaria de procurar? \n>")
        with open(f"{name}.txt", "r", encoding='utf-8') as ficheiro:
            for linha in ficheiro:
                if palavra in linha:
                    print("Aqui esta seu resultado:")
                    print(linha.rstrip())


