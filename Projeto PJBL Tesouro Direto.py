# Importando bibliotecas
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Leitura arquivo csv
dfdados = pd.read_csv("TesouroDireto.csv", sep=";")

#Funções
def split (dfdados): #Separação nomes títulos
    linha = dfdados.iloc[0] 
    TipoTitulo = linha['Tipo Titulo']
    Titulo = []  
    for i in range(1,len(dfdados)): 
            linha = dfdados.iloc[i]
            TipoTitulo = linha['Tipo Titulo']

            if TipoTitulo == linha['Tipo Titulo']:
                if TipoTitulo not in Titulo:
                    Titulo.append(TipoTitulo)    
            else:
                
                linha = dfdados.iloc[0]
                TipoTitulo = linha['Tipo Titulo']         
    return Titulo

def valores (indice, dfdados): #Criação de lista com os valores de preço unitário de um título
   a = tesouros[indice] 
   pu = []
   for i in range(len(dfdados)):
       linha = dfdados.iloc[i]       
       Tesouro = linha['Tipo Titulo']
       preco = linha['PU']
       if a == Tesouro :
            preco = linha['PU']
            pu.append(preco)
   return pu

def somaquantidade (dfdados, indice, ano): #Cálculo e criação de lista a partir do número de quantidade de títulos vendidos em um período especificado pelo usuário
   a = tesouros[indice] 
   quantidade = [] 
   soma = 0
   colunas = 0
   for i in range(1,len(dfdados)):
       linha = dfdados.iloc[i]       
       Tesouro = linha['Tipo Titulo']
       for j in range(0,len(ano)):
            if int(dfdados.iloc[i]['Data Venda'][6:]) == int(ano[j]):
                if a == Tesouro :
                    for x in range(0,len(ano)):
                        if ano[x] == int(dfdados.iloc[i]['Data Venda'][6:]):
                            soma += linha['Quantidade']
                            quantidade.append(soma)
                            colunas +=1

   return quantidade,colunas

def quantidade (dfdados, aplicacao, coluna, coluna_2): #Criação de lista para os histogramas
    nomes = dfdados.iloc[0]
    qtde = nomes[coluna]
    Quantidade = []
    titulos = nomes[coluna_2]
    for i in range(len(dfdados)):
        nomes = dfdados.iloc[i]
        qtde = nomes[coluna]
        titulos = nomes[ coluna_2]
        if titulos == aplicacao :   
            if titulos == nomes[ coluna_2]:
                if qtde == nomes[coluna]:
                    Quantidade.append(qtde)
                else:
                    nomes = dfdados.iloc[0]
                    qtde = nomes[coluna]
                    Quantidade.append(qtde)
    return Quantidade


#Amostra de opções e funções do programa
print('Os títulos do tesouro direto a serem analisados nos gráficos são: ')
tesouros = split(dfdados)
for i in range(0,5): #Print títulos
    informacoes=tesouros[i]
    print(informacoes)
print('Opções de informações do programa:')   
print('Opção 0: Encerrar o programa')
print('Opção 1: Gráfico de curvas da evolução dos preços unitários dos títulos')
print('Opção 2: Gráfico de curvas da quantidade de títulos vendidos informado por um período ')
print('Opção 3: Histograma da quantidade vendida do título informado')
print('Opção 4: Histograma da quantidade do preço unitário de um título informado')

#Dicionário de cores para o histograma
cores = {'AZUL':'b', 'VERDE':'g', 'VERMELHO':'r','CIANO':'c','MAGENTA':'m','AMARELO':'y','PRETO':'k'} 

#Entrada de dados
while True:
    opcao_escolhida = int(input('Qual informação deseja visualizar - Opções 0,1,2,3 ou 4? '))
    if opcao_escolhida == 0: #Critério de parada de acordo com as opções escolhidas
        print('Obrigado(a) por utilizar o programa.')
        break
    if opcao_escolhida == 1: #Gráfico de curva com várias linhas 
    #-->  Em um dos gráficos \n de linhas, devem ser exibidas, ao menos,2 linhas.
        valor_1 = np.array(valores(0,dfdados))
        valor_2 = np.array(valores(1,dfdados))
        valor_3 = np.array(valores(2,dfdados))
        valor_4 = np.array(valores(3,dfdados))
        valor_5 = np.array(valores(4,dfdados))  
        eixo_x = np.linspace(2002,2021,936)
        plt.figure(figsize=(12,8))
        for i in range(valor_1.shape[0]):
            if valor_1[i] == 0: 
              valor_1[i] = None
            if valor_2[i] == 0: 
               valor_2[i] = None
            if valor_3[i] == 0: 
               valor_3[i] = None
            if valor_4[i] == 0: 
               valor_4[i] = None
            if valor_5[i] == 0: 
               valor_5[i] = None         
        #Plotagem do gráfico
        plt.plot(eixo_x, valor_1,label = str(tesouros[0]))
        plt.plot(eixo_x, valor_2,label = str(tesouros[1]))
        plt.plot(eixo_x, valor_3,label = str(tesouros[2]))
        plt.plot(eixo_x, valor_4,label = str(tesouros[3]))
        plt.plot(eixo_x,valor_5,label  = str(tesouros[4])) 
        plt.xticks(np.arange(2002,2021), rotation = 90)
        plt.yticks(np.arange(0,1800,200))
        plt.legend()
        plt.title('Evolução do preço unitário (PU)')
        plt.xlabel('Anos')
        plt.ylabel('Valor (R$)')
        plt.show() 
        
    if opcao_escolhida == 2: #Gráfico de curva referente a soma da quantidade comercializada de um título em um tempo específico 
    # --> A geração de, ao menos, um gráfico deve exigir a realização de algum cálculo sobre os dados lidos dos arquivos
    # --> O usuário deve poder parametrizar a exibição de pelo menos um dos gráficos de linha
        print('Opções de títulos do tesouro direto:')
        print('Título 0 = ' + str(tesouros[0]))
        print('Título 1 = ' + str(tesouros[1]))
        print('Título 2 = ' + str(tesouros[2]))
        print('Título 3 = ' + str(tesouros[3]))
        print('Título 4 = ' + str(tesouros[4]))
        titulo = int(input('Digite a numeração (0,1,2,3,4) do título escolhido : '))
        while titulo not in range(0,5):
            print('Erro...... Digite um número válido ')
            titulo = int(input('Digite a numeração (0,1,2,3,4,5) do título escolhido : '))
            
        inicio = int(input('Digite o ano de início entre 2002-2019: '))
        while inicio not in range(2002,2021):
            print('Erro...... Digite um ano válido ')
            inicio = int(input('Digite o ano de início entre 2002-2019: '))  
            
        fim = int(input('Digite o ano de fim entre 2003-2020: '))
        while fim not in range(2002,2021):
            print('Erro...... Digite um ano válido ')
            fim = int(input('Digite o ano de fim entre 2003-2020: '))
        while fim <= inicio:
                print('Erro...... Digite um ano final superior ao inicial ')
                fim = int(input('Digite o ano de fim entre 2003-2020: ')) 
                
        #Plotagem do gráfico
        intervalo = np.arange(inicio,fim + 1)
        teste,colunas = somaquantidade  (dfdados, titulo, intervalo.tolist())
        calendario = np.linspace(inicio,fim,colunas)
        plt.plot(calendario, teste)
        plt.title('Evolução da quantidade total comercializada do ' + str(tesouros[titulo]) + '\n Entre os anos: '+ str(inicio) + ' e ' + str(fim))
        plt.xlabel('Anos')
        plt.ylabel('Quantidade comercializada')
        plt.grid()
        plt.show()  
 
    if opcao_escolhida == 3: #Histrograma quantidade de títulos
        print('Opções de títulos do tesouro direto:')
        print('Título 0 = ' + str(tesouros[0]))
        print('Título 1 = ' + str(tesouros[1]))
        print('Título 2 = ' + str(tesouros[2]))
        print('Título 3 = ' + str(tesouros[3]))
        print('Título 4 = ' + str(tesouros[4]))
        titulo = int(input('Digite a numeração (0,1,2,3,4) do título escolhido : '))
        while titulo not in range(0,5):
            print('Erro...... Digite um número válido ')
            titulo = int(input('Digite a numeração (0,1,2,3,4,5) do título escolhido : '))
        Quantidade_titulos = quantidade(dfdados, tesouros[titulo], 'Quantidade', 'Tipo Titulo')
        if titulo == 0:
            intervalo = np.linspace(0,1000,20)
        if titulo in range(1,5):
            intervalo = np.linspace(0,1000,30)
        
        print(cores)
        cor = input('Entre com a cor do histograma: ')
        Cor = cor.upper()
        while Cor not in cores:
            print('Erro...... Digite uma cor válida ')
            cor = input('Entre com a cor do histograma: ')
            Cor = cor.upper()
        if Cor in cores:
            cor_grafico = cores[Cor]
            
        #Plotagem do histograma
        plt.hist(Quantidade_titulos,bins = intervalo, rwidth = 0.9, color = cor_grafico)
        plt.title('Histograma da quantidade de títulos ' + str(tesouros[titulo]))
        plt.xlabel('Números de títulos com mesma ocorrência')
        plt.ylabel('Ocorrência de títulos')
        plt.show()
        
    if opcao_escolhida == 4: #Histograma quantidade PU por título
        print('Opções de títulos:')
        print('Título 0 = ' + str(tesouros[0]))
        print('Título 1 = ' + str(tesouros[1]))
        print('Título 2 = ' + str(tesouros[2]))
        print('Título 3 = ' + str(tesouros[3]))
        print('Título 4 = ' + str(tesouros[4]))
        titulo = int(input('Digite a numeração (0,1,2,3,4) do título escolhido : '))
        while titulo not in range(0,5):
            print('Erro...... Digite um número válido ')
            titulo = int(input('Digite a numeração (0,1,2,3,4) do título escolhido : '))
        Pu_titulo = quantidade(dfdados, tesouros[titulo], 'PU', 'Tipo Titulo') 
        intervalo = np.linspace(0,1750,12)
        print(cores)
        cor = input('Entre com a cor do histograma: ')
        Cor = cor.upper()
        while Cor not in cores:
            print('Erro...... Digite uma cor válida ')
            cor = input('Entre com a cor do histograma: ')
            Cor = cor.upper()
        if Cor in cores:
            cor_grafico = cores[Cor]
            
        #Plotagem do histograma    
        plt.hist(Pu_titulo,bins = intervalo, rwidth = 0.9, color = cor_grafico)
        plt.title('Histograma referente ao Preço Unitário do ' + str(tesouros[titulo]))
        plt.xlabel('Preço Unitário')
        plt.ylabel('Contagem Preços Unitários')
        plt.show()   
        
    elif opcao_escolhida not in range(0,5): #Possível entrada de dados errada
         print('Erro........ Opção escolhida inválida. Insira uma opção válida.')
        

            
        

        
            
           