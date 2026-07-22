# Exemplo de operadores aplicados
def aplicar_promocao(produto, percentual):
    if produto.preco > 10 and produto.quantidade > 5:  # condicional
        produto.aplicar_desconto(percentual)
