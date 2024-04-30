def refeicao(prato_principal, acompanhamento, bebida):
    return f"Olá aqui está o seu pedido de {prato_principal}, {acompanhamento} e {bebida}. Bom apetite!"

pedido = refeicao('hamburguer', 'batatas fritas', 'refrigerante de laranja')
print(pedido)