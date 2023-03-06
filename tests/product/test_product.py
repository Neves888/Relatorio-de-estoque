from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        id=1546,
        nome_da_empresa='elemento-x',
        nome_do_produto='tetraborato de sódio',
        data_de_fabricacao='07/07/2017',
        data_de_validade='07/07/2037',
        numero_de_serie='5489BD25',
        instrucoes_de_armazenamento='manter em local seco',
    )
    assert produto.id == 1546
    assert produto.nome_da_empresa == 'elemento-x'
    assert produto.nome_do_produto == 'tetraborato de sódio'
    assert produto.data_de_fabricacao == '07/07/2017'
    assert produto.data_de_validade == '07/07/2037'
    assert produto.numero_de_serie == '5489BD25'
    assert produto.instrucoes_de_armazenamento == 'manter em local seco'
