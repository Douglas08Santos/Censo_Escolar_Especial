'''
    IMD1151 - CIÊNCIAS DE DADOS - T01 (2025.1)

    Resultados Censo Escolar
    Numeros de aluno da Educação Básica na educação especial(Inclusiva ou Exclusiva)
    Aluno: Douglas Alexandre dos Santos
    Matricula: 20210096853
    Fonte: https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar/resultados
'''

from sys import argv
import pandas as pd

dataset = pd.read_csv('../data/microdados_ed_basica_2024.csv',
                      encoding='latin-1', sep=';')

# Exibir dados 
print('Informações do Dataset: {}'.format(dataset.info()))

# Mas vemos que tem muitas colunas - 476
print('Antes de filtrar as colunas importantes: {}'.format(len(dataset.columns)))

'''
    Agora faremos a seleção de colunas que precisamos, com auxilio do
    dicionario de dados

    NO_REGIAO   Nome da região geografica
    NO_UF   Nome da Unidade da Federação
    SG_UF   Sigla da Unidade da Federação
    NO_MUNICIPIO    Nome do Município
    NO_ENTIDADE	Nome da Escola
    TP_SITUACAO_FUNCIONAMENTO   Situação de funcionamento
        1 - Em Atividade
        2 - Paralisada
        3 - Extinta (ano do Censo)
        4 - Extinta em Anos Anteriores
    -------------
    IN_VINCULO_SECRETARIA_EDUCACAO	Órgão ao qual a escola pública está vinculada - Secretaria de Educação/Ministério da Educação
        0 - Não
        1 - Sim
        - Não aplicável para escolas privadas
    'IN_VINCULO_SEGURANCA_PUBLICA'	Órgão ao qual a escola pública está vinculada - Secretaria de Segurança Pública/Forças Armadas/Militar
        0 - Não
        1 - Sim
        - Não aplicável para escolas privadas
    IN_VINCULO_SECRETARIA_SAUDE	Órgão ao qual a escola pública está vinculada - Secretaria de Saúde/Ministério da Saúde
        0 - Não
        1 - Sim
        - Não aplicável para escolas privadas
    IN_VINCULO_OUTRO_ORGAO	Órgão ao qual a escola pública está vinculada - Outro órgão da administração pública
        0 - Não
        1 - Sim
        - Não aplicável para escolas privadas
    -------------
    IN_MANT_ESCOLA_PRIVADA_EMP	Mantenedora da escola privada - Empresa ou grupo empresarial do setor privado ou pessoa física
        0 - Não
        1 - Sim
        - Não aplicável para escolas públicas
    IN_MANT_ESCOLA_PRIVADA_ONG	Mantenedora da escola privada - Organização Não Governamental (ONG) - internacional ou nacional
        0 - Não
        1 - Sim
        - Não aplicável para escolas públicas
    IN_MANT_ESCOLA_PRIVADA_OSCIP	Mantenedora da escola privada - Organização da Sociedade Civil de Interesse Público (Oscip)
        0 - Não
        1 - Sim
        - Não aplicável para escolas públicas
    IN_MANT_ESCOLA_PRIV_ONG_OSCIP	Mantenedora da escola privada - Organização Não Governamental (ONG) - internacional ou nacional. Organização da Sociedade Civil de Interesse Público (Oscip)
        0 - Não
        1 - Sim
        - Não aplicável para escolas públicas
    IN_MANT_ESCOLA_PRIVADA_SIND	Mantenedora da escola privada - Sindicatos de trabalhadores ou patronais, associações e cooperativas
        0 - Não
        1 - Sim
        - Não aplicável para escolas públicas
    IN_MANT_ESCOLA_PRIVADA_SIST_S	Mantenedora da escola privada - Sistema S (Sesi, Senai, Sesc, outros)
        0 - Não
        1 - Sim
        - Não aplicável para escolas públicas
    IN_MANT_ESCOLA_PRIVADA_S_FINS	Mantenedora da escola privada - Instituições sem fins lucrativos
        0 - Não
        1 - Sim
        - Não aplicável para escolas públicas
    -------------
    TP_RESPONSAVEL_REGULAMENTACAO	Esfera administrativa do conselho ou órgão responsável pela Regulamentação/Autorização
        1 - Federal
        2 - Estadual
        3 - Municipal
        4 - Estadual e Municipal
        5 - Federal e Estadual
        6 - Federal, Estadual e Municipal
        9 - Não informado
        - Não aplicável para escolas sem regulamentação  
    -------------
    IN_INF	Etapa de Ensino - Educação Infantil (Possui uma ou mais matrículas)
        0 - Não
        1 - Sim
    IN_INF_CRE	Etapa de Ensino - Educação Infantil - Creche (Possui uma ou mais matrículas)
        0 - Não
        1 - Sim
    IN_INF_PRE	Etapa de Ensino - Educação Infantil - Pré-Escola (Possui uma ou mais matrículas)
        0 - Não
        1 - Sim
    IN_FUND	Etapa de Ensino - Ensino Fundamental (Possui uma ou mais matrículas)
        0 - Não
        1 - Sim
    IN_FUND_AI	Etapa de Ensino - Ensino Fundamental - Anos Iniciais (Possui uma ou mais matrículas)
        0 - Não
        1 - Sim
    IN_FUND_AF	Etapa de Ensino - Ensino Fundamental - Anos Finais (Possui uma ou mais matrículas)
        0 - Não
        1 - Sim
    IN_ESP	Educação Especial - Inclui a Educação Especial Inclusiva (em Classes Comuns) e a Educação Especial Exclusiva (Possui uma ou mais matrículas)
        0 - Não
        1 - Sim
    IN_ESP_CC	Educação Especial Inclusiva (em Classes Comuns) - Escola possui um ou mais alunos com deficiência, transtorno global do desenvolvimento
        ou altas habilidades/superdotação estudando em classes comuns do Ensino Regular e/ou Educação de Jovens e Adultos (Possui uma ou mais matrículas)
        0 - Não
        1 - Sim
    IN_ESP_CE	Educação Especial Exclusiva - Escola exclusivamente especializada e/ou que possui classe especial exclusiva para o atendimento de alunos
        com deficiência, transtorno global do desenvolvimento ou altas habilidades/superdotação (Possui uma ou mais matrículas)
        0 - Não
        1 - Sim
    -------------
    QT_MAT_BAS	Número de Matrículas da Educação Básica
    -------------
    QT_MAT_INF	Número de Matrículas da Educação Infantil [QT_MAT_INF_CRE + QT_MAT_INF_PRE]
    QT_MAT_INF_CRE	Número de Matrículas da Educação Infantil - Creche
    QT_MAT_INF_PRE	Número de Matrículas da Educação Infantil - Pré-Escola
    
    *** em duvida se uso esses numeros
    QT_MAT_FUND	Número de Matrículas do Ensino Fundamental [QT_MAT_FUND_AI + QT_MAT_FUND_AF]
    QT_MAT_FUND_AI	Número de Matrículas do Ensino Fundamental - Anos Iniciais [Anos: 1º-5º]
    QT_MAT_FUND_AF	Número de Matrículas do Ensino Fundamental - Anos Finais [Anos: 6º-9º]
    ***

    QT_MAT_ESP	Número de Matrículas da Educação Especial [QT_MAT_ESP_CC + QT_MAT_ESP_CE]
    QT_MAT_ESP_CC	Número de Matrículas da Educação Especial Inclusiva
    QT_MAT_ESP_CE	Número de Matrículas da Educação Especial Exclusiva
    -------------
    QT_DOC_ESP	Número de Docentes da Educação Especial [QT_DOC_ESP_CC + QT_DOC_ESP_CE]
    QT_DOC_ESP_CC	Número de Docentes da Educação Especial Inclusiva
    QT_DOC_ESP_CE	Número de Docentes da Educação Especial Exclusiva
    -------------
    QT_TUR_ESP	Número de Turmas de Educação Especial [QT_TUR_ESP_CC + QT_TUR_ESP_CE]
    QT_TUR_ESP_CC	Número de Turmas de Educação Especial Inclusiva
    QT_TUR_ESP_CE	Número de Turmas de Educação Especial Exclusiva


'''
# Agora reduzida para mais ou menos 40 colunas
important_columns = ['NO_REGIAO', 'NO_UF', 'SG_UF', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'TP_SITUACAO_FUNCIONAMENTO',
                       'IN_VINCULO_SECRETARIA_EDUCACAO', 'IN_VINCULO_SEGURANCA_PUBLICA', 'IN_VINCULO_SECRETARIA_SAUDE',
                       'IN_VINCULO_OUTRO_ORGAO', 'IN_MANT_ESCOLA_PRIVADA_EMP', 'IN_MANT_ESCOLA_PRIVADA_ONG', 
                       'IN_MANT_ESCOLA_PRIVADA_OSCIP', 'IN_MANT_ESCOLA_PRIV_ONG_OSCIP', 'IN_MANT_ESCOLA_PRIVADA_SIND',
                       'IN_MANT_ESCOLA_PRIVADA_SIST_S', 'IN_MANT_ESCOLA_PRIVADA_S_FINS', 'TP_RESPONSAVEL_REGULAMENTACAO',
                       'IN_INF', 'IN_INF_CRE', 'IN_INF_PRE', 'IN_FUND','IN_FUND_AI', 'IN_FUND_AF', 'IN_ESP', 'IN_ESP_CC',
                       'IN_ESP_CE', 'QT_MAT_BAS', 'QT_MAT_INF', 'QT_MAT_INF_CRE', 'QT_MAT_INF_PRE', 'QT_MAT_FUND', 
                       'QT_MAT_FUND_AI', 'QT_MAT_FUND_AF', 'QT_MAT_ESP', 'QT_MAT_ESP_CC','QT_MAT_ESP_CE', 'QT_DOC_ESP',
                       'QT_DOC_ESP_CC', 'QT_DOC_ESP_CE', 'QT_TUR_ESP', 'QT_TUR_ESP_CC', 'QT_TUR_ESP_CE']

dataset = dataset[important_columns]
print('Depois de escolher as colunas importantes: {}'.format(len(dataset.columns)))

'''
    Agora filtrar as escolas por TP_SITUACAO_FUNCIONAMENTO - Situação de funcionamento
        1 - Em Atividade
        2 - Paralisada
        3 - Extinta (ano do Censo)
        4 - Extinta em Anos Anteriores
    Tira do registro todas que tem o valor diferente de 1 - Em atividade
'''
# Antes do filtro
print('Antes de filtrar por escolas ativas: {}'.format(len(dataset))) # 215545

# Instituições em atividade
dataset = dataset[dataset['TP_SITUACAO_FUNCIONAMENTO'] == 1]

# Depois do filtro
print('Depois de filtrar por escolas ativas: {}'.format(len(dataset))) # 181065 - 34000 registro a menos

# Como essa coluna TP_SITUAÇÃO não é mais necessaria, vamos removê-la
dataset.drop(['TP_SITUACAO_FUNCIONAMENTO'], axis='columns', inplace=True)

'''
    Verificar escolas onde o numero matriculas - QT_MAT_BAS - é nulo
'''
#Retirando as escolas com QT_MAT_BAS nulo
dataset = dataset[~dataset['QT_MAT_BAS'].isnull()]
print('Número de escolas com QT_MAT_BAS não nulo: {}'.format(len(dataset)))

'''
    Podemos dividir as escolas em públicas ou privada, uma vez que as colunas:
        - IN_VINCULO_SECRETARIA_EDUCACAO
        - IN_VINCULO_SEGURANCA_PUBLICA
        - IN_VINCULO_SECRETARIA_SAUDE
        - IN_VINCULO_OUTRO_ORGAO
        [Não são aplicável para escolas privadas, se for nulo, então é privada]
        - IN_MANT_ESCOLA_PRIVADA_EMP
        - IN_MANT_ESCOLA_PRIVADA_ONG
        - IN_MANT_ESCOLA_PRIVADA_OSCIP
        - IN_MANT_ESCOLA_PRIV_ONG_OSCIP
        - IN_MANT_ESCOLA_PRIVADA_SIND
        - IN_MANT_ESCOLA_PRIVADA_SIST_S
        - IN_MANT_ESCOLA_PRIVADA_S_FINS
        [Não são aplicável para escolas públicas, se for nulo, então é pública]
'''
public_schools = dataset[dataset['IN_MANT_ESCOLA_PRIVADA_EMP'].isnull()]
private_schools = dataset[~dataset['IN_MANT_ESCOLA_PRIVADA_EMP'].isnull()]

'''
    Tamanho dos DataFrames:
'''
print('Número escolas públicas: {}'.format(len(public_schools)))
print('Número escolas privadas: {}'.format(len(private_schools)))
#print('Número de escolas: {}'.format(len(dataset)))

'''
    Após a separação, é possivel remover as colunas que não tem utilidade
'''
public_schools.drop(['IN_MANT_ESCOLA_PRIVADA_EMP', 'IN_MANT_ESCOLA_PRIVADA_ONG',
                      'IN_MANT_ESCOLA_PRIVADA_OSCIP', 'IN_MANT_ESCOLA_PRIV_ONG_OSCIP',
                      'IN_MANT_ESCOLA_PRIVADA_SIND', 'IN_MANT_ESCOLA_PRIVADA_SIST_S',
                      'IN_MANT_ESCOLA_PRIVADA_S_FINS'], axis='columns', inplace=True)

private_schools.drop(['IN_VINCULO_SECRETARIA_EDUCACAO', 'IN_VINCULO_SEGURANCA_PUBLICA',
                       'IN_VINCULO_SECRETARIA_SAUDE', 'IN_VINCULO_OUTRO_ORGAO'],
                       axis='columns', inplace=True)

'''
    Agora que o tratamento dos dados terminou, podemos exportar as 
    tabelas de escolas publicas e privadas para que sejam analisadas.
'''

public_schools.to_csv('../data/public_school_Brazil_2024.csv', sep=';', encoding='utf-8', index=False)
private_schools.to_csv('../data/private_school_Brazil_2024.csv', sep=';', encoding='utf-8',  index=False)