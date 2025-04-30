'''
    IMD1151 - CIÊNCIAS DE DADOS - T01 (2025.1)

    Resultados Censo Escolar
    Numeros de aluno da Educação Básica na educação especial(Inclusiva ou Exclusiva)
    Aluno: Douglas Alexandre dos Santos
    Matricula: 20210096853
    Fonte: https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar/resultados

    Geração de gráficos
'''


import matplotlib.pyplot as plt
import pandas as pd

'''
    Carregando os dataframes com os dados já tratados
'''
publicas = pd.read_csv('../data/public_school_Brazil_2024.csv', sep=';')
privadas = pd.read_csv('../data/private_school_Brazil_2024.csv', sep=';')

print('Número de escolar públicas: {}'.format(len(publicas)))
print('Número de escolar privadas: {}'.format(len(privadas)))

'''
    Agora plotar os graficos
'''

'''

    Problema a ser explorado:
        - "Há desigualdade na oferta de Educação Especial(inclusiva ou exclusiva)
        entre escolas públicas e privadas nas diferentes regiões do Brasil?"
    
    Questões sobre o perfil das escolas brasileiras, especialmente com foco na Educação especial.

    Podemos explorar:

    O perfil geral das escolas:
        - Quantas escolas existem por estado, região?(publica e privada)
            + OBS: seria legal fazer um grafico de colunas sobrepostas
            + OBS será que seria melhor colocar os 2 dataframes me só 1?
        - Qual a proporção de escolas públicas e privadas por estado, região?
        - Qual o número médio de matrículas por escola?

    Educação Infantil e Fundamental
        - Qual a distribuição das modalidades entre as escolas publicas e privadas?
        - 
    
    Educação Especial
        - Quantas escolas oferecem Educação Especial Inclusiva? E Exclusiva?
        - Qual o total de matriculas na Educação Especial por estado, região?
        - Qual a proporção de escolas com classes comuns x classes especiais?
        - Qual a distribuição dos docentes e as turmas de Educação Especial?

    Comparativos entre escolas públicas e privadas
        - Qual a média de alunos por escola publica x privada?
        - A educação especial é mais oferecida em escolas publicas ou privadas?
        - Em quais estados há maior participação da rede privada na educação infantil?

    Indicadores e relações?
        - Qual a razão aluno/docente em escolas com educação especial?
        - Existe correlação entre o número de turmas e o número de matrículas?
        - Há diferenças significativas entre regiões no acesso à Educação Especial?
'''
