import csv

''' -------------------------------------------
Extract: 
     
  lendo arquivo .csv, extraindo as informações 
  e organizando os dados em lista
--------------------------------------------- '''

arquivo =  open('lista.csv')
dados = csv.reader(arquivo)


''' ---------------------------------------------------------------------
Transform: 
     
  Verificar o perfil do cliente:
       conservador: oferecer carteira de investimento 100% renda fixa
       Moderado:    oferecer investimentos 60% renda fixa e 40% ações
       arrojado:    oferecer investimentos 70% ações e 30% renda fixa
       
   Se perfil arrojado e idade >= 40 anos considerar investimentos em
   ações 20% de crescimento de 50% de dividendos
   
  criar um novo item ('ação') na primeira lista (cabeçalho) para guardar
  as orientações
  
  criar uma lista (tabela) para guardar as litas tratadas (matriz)
------------------------------------------------0----------------------- '''

tabela = list()

for dado in dados:
     
     if dado[3] == 'conservador':
          dado.append('Oferecer carteira com investimentos 100% renda fixa')
          tabela.append(dado)
     
     elif dado[3] == 'moderado':
          dado.append('Oferecer carteira com investimentos 60% renda fixa e 40% ações')
          tabela.append(dado)
     
     elif dado[3] == 'arrojado' and dado[2] < '40':
          dado.append('Oferecer carteira com investimentos 70% ações e 30% renda fixa')
          tabela.append(dado)
     
     elif dado[3] == 'arrojado' and dado[2] >= '40':
          dado.append('Oferecer carteira com investimentos 70% ações (20% crescimento + 50% dividendos) e 30% renda fixa')
          tabela.append(dado)
     else:
          dado.append('acao')
          tabela.append(dado)


''' ------------------------------------------------------------------------------
Load: 
  
     Criar um arquivo (orientações.csv) com as orientações de ação desejada 
     para cada cliente
------------------------------------------------------------------------------- '''

novo_arquivo open('orientações.csv', 'w', newline='')
orientacoes = csv.writer(novo_arquivo, delimiter=',')
orientacoes.writerows(tabela)


arquivo.close()
novo_arquivo.close()



