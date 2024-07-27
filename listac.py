def compras():
    import random
    lista_compras = []
    while True:
        print("BEM VINDO A SUA LISTA DE COMPRAS\n")
        if lista_compras:
            for item in lista_compras:
                print(f"ID: {item['id']} Nome: {item['nome']} Quantidade: {item['quantidade']} {item['unidade']} Descrição: {item['descricao']}\n")

        else:
            print('Não há produtos em sua lista. Adicione-os\n')

        opcao = input("1.Adicionar produto\n2.Remover Produto\n3.Pesquisar Produto\n4.Sair")
        opcoes = ['1', '2', '3', '4']

        if opcao not in opcoes:
            print('Opção inválida.Escolha uma das cinco opções do menu')
            continue
        if opcao == '4':
            print('Volte sempre.')
            break

        if opcao == '1':
            nome = input('Insira o nome')
            nome = nome.lower()
            #entrada de str
            try:
                quantidade = int(input('Insira a quantidade desejada:'))
                if quantidade <=0:
                    print('O campo quantidade deve receber um número maior e diferente de zero.')
                    continue
            except ValueError:
                    print('Você deve inserir inserir numerais no campo quantidade.')
                    continue

            quantidade= quantidade
            print('OPÇÕES DE UNIDADE DE MEDIDA\n1.Quilograma(s)\n2.Grama(s)\n3.Litro(s)\n4.Mililitro(s)')
            print('5.Unidade(s)\n6.Metro(s)\n7.Centímetro(s)\n')
            unidade_medida = input('Insira o número correspondente a unidade desejada\n')

            if unidade_medida == '1':
                unidade = 'Quilograma(s)'
            elif unidade_medida == '2':
                unidade = 'Grama(s)'
            elif unidade_medida == '3':
                unidade = 'Litro(s)'
            elif unidade_medida == '4':
                unidade = 'Mililitro(s)'
            elif unidade_medida == '5':
                unidade = 'Unidade(s)'
            elif unidade_medida == '6':
                unidade = 'Metro(s)'
            elif unidade_medida == '7':
                unidade = 'Centímetro(s)'
            else:
                print("Opção inválida. Você deve escolher uma das opções da lista de unidade com base no número ao lado\n")
                continue

            descricao = input('Insira a descrição do produto.')
            aleatorio = random.randint(1, 10000)
            lista_compras.append({"id": aleatorio, "nome": nome, "quantidade": quantidade, "unidade": unidade, "descricao": descricao})
            print('Produto Adicionado!\n')

        elif opcao == '2':
            #lista vazia
            if not lista_compras:
                print('Não ha produtos na lista. Você sera redirecionado ao menu')
                continue
            else:
                print('Aqui estão os produtos de sua lista:')
                for item in lista_compras:
                    print(f"ID: {item['id']} Nome: {item['nome']} Quantidade: {item['quantidade']} {item['unidade']} Descrição: {item['descricao']}\n")
                #entrada str
                try:
                    identificador = int(input('Qual o ID do produto que deseja remover? '))
                except ValueError:
                    print('ID inválido. Você será redirecionado ao menu.')
                    continue

                remover = None
                for indice, dicionario in enumerate(lista_compras):
                    if dicionario['id'] == identificador:
                        remover = indice
                        break

                if remover is not None:
                    lista_compras.pop(remover)
                    print('Produto removido!')
                else:
                    print('ID inválido. Você será redirecionado ao menu.')

        elif opcao == '3':
            quantidade_itens = len(lista_compras)
            print('Você tem ', quantidade_itens, 'itens na lista.')
            pesquisador = input('Insira o nome do produto que deseja procurar:')
            pesquisador = pesquisador.lower()
            resultado_pesquisa = []
            quantidade_pesquisa = len(resultado_pesquisa)

            for dicionario in lista_compras:
                if pesquisador in dicionario.get('nome', ''):
                   resultado_pesquisa.append(dicionario)
                else:
                    print('Este produto não está na lista')

            print('Foram encontrados', quantidade_pesquisa, 'itens para sua pesquisa')
            for item in resultado_pesquisa:
                print(f"ID: {item['id']} Nome: {item['nome']} Quantidade: {item['quantidade']} {item['unidade']} Descrição: {item['descricao']}\n")
            print('Pesquisa encerrada')
            continue
compras()
