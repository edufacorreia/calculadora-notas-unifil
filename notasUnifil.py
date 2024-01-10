# verificando parcialidade
tipo = str(input('Já possui as notas das quatro avaliações? [S] - Sim, [N] - Não: '))
# solicitando as notas
print('Preencha com suas notas, caso ainda não tenha, preencha com 0')
ava1 = float(input('Nota do AVA1: '))
ava2 = float(input('Nota do AVA2: '))
ava3 = float(input('Nota do AVA3: '))
ava4 = float(input('Nota do AVA4: '))
# somando as notas por peso
somaNotas = (ava1*0.1) + (ava2*0.3) + (ava3*0.2) + (ava4*0.4)
# condicionais

# verificando notas parciais
faltaNotas = 70 - somaNotas
if tipo == 'N' or tipo == 'n':
    if somaNotas < 70:
        print(f'Sua nota parcial é de {somaNotas}. Você precisa de {faltaNotas} pontos para aprovação nos trabalhos restantes.')
    else:
        print(f'Sua nota {somaNotas} já está acima da média 70, aprovado!')

# condicional para exame, todas as notas
notaMinExame = 120 - somaNotas
if tipo == 'S' or tipo == 's':
    if somaNotas < 70:
        print(f'Sua nota foi {somaNotas}. Terá que fazer exame e tirar no mínimo: ', notaMinExame)
    else:
        print(f'Você foi aprovado com nota {somaNotas}')