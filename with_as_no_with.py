arquivo = open('Aula5 sem With.txt', 'w')
arquivo.write('''
Detroit: Become Human é um jogo eletrônico produzido pela Quantic Dream e publicado pela Sony
Interactive Entertainment para o PlayStation 4 e Microsoft Windows PC. ''')
arquivo = open('Aula5 sem With.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()