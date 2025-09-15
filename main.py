# Simulação de Banco de Dados com arrays
# ? Sistema de Alunos de Uma escola
# * Informações: ID_Aluno, Nome Completo, Data Nascimento, Em que ano esta

import numpy as np

informacoes = [
    ["ID_Aluno", "Nome", "Data Nascimento", "Ano Escolar"],
    [1, "Ana Beatriz Souza", "14-05-1998", 7],
    [2, "Carlos Henrique Silva", "03-11-2002", 5],
    [3, "Mariana Oliveira Costa", "29-08-1995", 9],
    [4, "João Pedro Almeida", "17-02-2000", 2],
    [5, "Fernanda Lima Rocha", "22-07-1993", 4],
    [6, "Gabriel Martins Duarte", "05-01-1999", 8],
    [7, "Larissa Gomes Ferreira", "11-09-2001", 3],
    [8, "Ricardo Alves Moreira", "27-12-1996", 6],
    [9, "Juliana Castro Ribeiro", "30-03-1994", 1],
    [10, "Lucas Pereira Nogueira", "16-08-1997", 9],
    [11, "Camila Mendes Rocha", "22-10-1992", 5],
    [12, "Felipe Barbosa Lima", "07-07-2003", 2],
    [13, "Patrícia Azevedo Moura", "19-06-1990", 4],
    [14, "Thiago Costa Pacheco", "02-02-1998", 7],
    [15, "Bianca Ferreira Torres", "25-04-1999", 6],
    [16, "Vinícius Lopes Andrade", "10-11-1995", 3],
    [17, "Natália Rodrigues Pinto", "18-12-2001", 8],
    [18, "André Oliveira Cardoso", "08-09-1997", 1],
    [19, "Sabrina Martins Faria", "13-05-1996", 2],
    [20, "Rodrigo Cunha Barbosa", "21-01-1994", 9]
]
# Cabeçalho das Informações ID_Aluno, Nome, Data_Nascimento e Ano_Escolar
cabecalho = (f" {informacoes[0][0]:<12} {informacoes[0][1]:<25} {informacoes[0][2]:<16} {informacoes[0][3]:<12} ")

# Transforma a Lista em Array e Depois em uma matriz 21x4
arr = np.array(informacoes)
reshaped = np.reshape(arr, (21, 4))

# Mostra as informações alinhadas
for c in informacoes:
    print(f" {c[0]:<12} {c[1]:<25} {c[2]:<16} {c[3]:<12} ")
    
print('-'*70)

# Pega o ID para Filtragem
id = int(input("Insira o ID do Aluno que você quer filtrar: "))

# Mostra as Informações do ID junto com o cabeçalho de informações
print(cabecalho)
for c in informacoes:
    if c[0] == id:
        print(f" {c[0]:<12} {c[1]:<25} {c[2]:<16} {c[3]:<12} ")
        print('-'*70)
    