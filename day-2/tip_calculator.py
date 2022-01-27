import random


def calcula_taxa_servico(valor_total_conta, gorjeta):
    taxa_servico = (gorjeta / 100) * valor_total_conta
    taxa_servico = round(taxa_servico, 2)
    return taxa_servico


def calcula_valor_por_pessoa(gorjeta, total_pessoas, valor_total_conta):
    taxa_servico = calcula_taxa_servico(valor_total_conta, gorjeta)
    return (valor_total_conta + taxa_servico) / total_pessoas


def calcula_conta():
    numero_mesa = random.randrange(1, 10)
    valor_total_conta = random.randrange(50, 300)
    print("************ Volte Sempre ************")
    print(f'Mesa: {numero_mesa}')
    print(f'Valor Total sem Serviço: ${valor_total_conta}')

    gorjeta = int(input('Quanto deseja pagar de serviço? [5%, 10% ou 15%]....: '))
    taxa_servico = calcula_taxa_servico(valor_total_conta, gorjeta)
    print(f'Taxa de Serviço: ${taxa_servico}')
    print(f'Valor Total com Serviço: ${taxa_servico + valor_total_conta}')

    total_pessoas = int(input('Dividir por quantas pessoas?....: '))
    valor_por_pessoa = calcula_valor_por_pessoa(gorjeta, total_pessoas, valor_total_conta)
    valor_por_pessoa = round(valor_por_pessoa, 2)
    print(f'Valor por pessoa: ${valor_por_pessoa}')


if __name__ == '__main__':
    calcula_conta()

# Mesa: 4
# Valor Total: $22
# Quanto deseja pagar de serviço? [5%, 10% ou 15%]....: 5
# Taxa de Serviço: $1.1
# Dividir por quantas pessoas?....: 4
# Valor por pessoa: $5.775