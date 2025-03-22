from time import sleep
with open('Aula5.txt', 'w') as ficheiro:
    conteudo = ficheiro.write('''
Detroit: Become Human é um jogo eletrônico produzido pela Quantic Dream e publicado pela Sony
Interactive Entertainment para o PlayStation 4 e Microsoft Windows PC. 
A história gira em torno de Kara, Markus e Connor, três androides concebidos pela empresa
fictícia CyberLife que, consoante as decisões que o tomar, mudarão o rumo da cidade
de Detroit e, consequentemente, dos Estados Unidos da América.
Além disso, será testemunhado o surgimento de uma nova raça: 
Os Divergentes (androides que manifestam emoções humanas).''')


with open('Aula5.txt', 'r') as ficheiro:
    linhas = ficheiro.readlines()
    for linha in linhas:
        sleep(2)
        print(linha)




    # linhas= ficheiro.readlines()
    # for linha in linhas
    #print(linha)

    #print(linhas)



    #linhas = ficheiro.readline()
    # #print(linhas)
   # linhas2 = ficheiro.readline()
   # print(linhas2)