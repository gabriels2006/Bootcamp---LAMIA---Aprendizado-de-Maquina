from Card_2.Card_2_pratica.Mercado_pratica.oo_pratica.funcionario_pratica import Funcionario
from Card_2.Card_2_pratica.Mercado_pratica.oo_pratica.produto_pratica import Produto
from Card_2.Card_2_pratica.Mercado_pratica.oo_pratica.estoque_pratica import Estoque

from Card_2.Card_2_pratica.Mercado_pratica.funcoes_pratica.calculos_pratica import calcular_valor_total
from Card_2.Card_2_pratica.Mercado_pratica.controle_pratica.menu_pratica import exibir_menu
from Card_2.Card_2_pratica.Mercado_pratica.pacote_pratica.sub_pratica.arquivo_pratica import mensagem_boas_vindas



# Variável do mercado
nome_mercado = "Mercado do Gabriel"

# Mensagem inicial usando pacote
print(mensagem_boas_vindas(nome_mercado))

# Criando funcionários
funcionarios = [
    Funcionario("Ana", 30, "Caixa", 2500),
    Funcionario("Carlos", 40, "Gerente", 5000)
]

# Criando estoque
estoque = Estoque()
estoque.adicionar_produto(Produto("Arroz", 25.90, 50))
estoque.adicionar_produto(Produto("Feijão", 8.50, 100))
estoque.adicionar_produto(Produto("Leite", 4.20, 200))

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        estoque.listar_produtos()

    elif opcao == "2":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        qtd = int(input("Quantidade: "))
        estoque.adicionar_produto(Produto(nome, preco, qtd))
        print("Produto adicionado!")

    elif opcao == "3":
        nome = input("Digite o nome do produto: ")
        produto = estoque.buscar_produto(nome)
        if produto:
            print("Produto encontrado:", produto)
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        total = calcular_valor_total(estoque)
        print(f"Valor total do estoque: R$ {total:.2f}")

    elif opcao == "5":
        print("Funcionários:")
        for f in funcionarios:
            print(f)

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, tente novamente.")
