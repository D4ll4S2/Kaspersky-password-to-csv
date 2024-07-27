import csv

# Define o nome do arquivo de entrada e saída
arquivo_entrada = 'pass.txt'
arquivo_saida = 'dados.csv'

# Abre o arquivo de texto para leitura
with open(arquivo_entrada, 'r') as txt_file:
    linhas = txt_file.readlines()

# Lista de chaves que esperamos encontrar (para garantir a ordem)
chaves = ['Website name', 'Website URL', 'Login name', 'Login', 'Password', 'Comment']

# Lista para armazenar os registros
registros = []

# Dicionário para armazenar o registro atual
registro_atual = {}

# Processa cada linha
for linha in linhas:
    if linha.strip() == '':  # Se a linha estiver em branco, significa que o próximo registro começou
        if registro_atual:  # Se tivermos um registro atual, salvamos e iniciamos um novo
            registros.append([registro_atual.get(chave, '') for chave in chaves])
            registro_atual = {}
    else:
        # Divide a linha na chave e no valor
        chave_valor = linha.split(':', 1)
        if len(chave_valor) == 2:
            chave, valor = chave_valor
            registro_atual[chave.strip()] = valor.strip()

# Adiciona o último registro se houver
if registro_atual:
    registros.append([registro_atual.get(chave, '') for chave in chaves])

# Escreve os registros no arquivo CSV
with open(arquivo_saida, 'w', newline='') as csv_file:
    escritor = csv.writer(csv_file)
    # Escreve o cabeçalho
    escritor.writerow(chaves)
    # Escreve os dados
    escritor.writerows(registros)
