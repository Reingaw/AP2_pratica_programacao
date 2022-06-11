import cliente
import motocicletas
import venda

client = cliente.Clientes()
moto = motocicletas.Motocicletas()
sales = venda.Venda()


def cadastrarCliente():
    nome = input('Digite o nome do cliente: ')
    cpf = input('Digite o cpf do cliente: ')
    try:
        client.setClient(nome, cpf)
        print('Cliente cadastrado com sucesso!')
    except:
        print("Não foi possível salvar os dados do cliente.")


def chooseClient():
    cpf = input('Digite o cpf do cliente: ')
    try:
        res = client.getClient(cpf)
        return res
    except:
        print("Não foi possível encontrar os dados do cliente.")


def cadastrarMoto():
    modelo = input('Digite o modelo da motocicleta: ')
    marca = input('Digite a marca da motocicleta: ')
    preco = input('Digite o preco da motocicleta: ')
    try:
        moto.setMoto(modelo, marca, preco)
        print('Motocicleta cadastrada com sucesso!')
    except:
        print("Não foi possível salvar os dados da motocicleta.")


def chooseMoto():
    res = moto.getAllMotos()

    print('Escolha a Motocicleta:\n')
    print('Código - Modelo - Marca - Preço')

    for item in res:
        print(f'{item[0]} - {item[1]} - {item[2]} - {item[3]}')

    id = int(input('Digite o código da motocicleta: '))
    motoescolhida = moto.getMoto(id)

    return motoescolhida


def efetuarVenda():
    clienteRetornado = chooseClient()
    print(f'Cliente: {clienteRetornado[0]}')

    motoretornada = chooseMoto()
    print(f'Motocicleta Escolhida: {motoretornada[0]} -'
          f' {motoretornada[1]} -'
          f' {motoretornada[2]}')

    # sales.setSale()


def setIsOver():
    sales.Over()
    print(sales.over)


def chooseOption(option):
    if option == '1':
        cadastrarCliente()
    elif option == '2':
        cadastrarMoto()
    elif option == '3':
        efetuarVenda()
    elif option == '4':
        setIsOver()


isOver = sales.over
while not isOver:
    option = input('1 - Cadastrar Cliente\n'
                   '2 - Cadastrar Motocicleta\n'
                   '3 - Efetuar Venda\n'
                   '4 - Sair\n'
                   'Escolha uma opção: ')

    chooseOption(option)
    isOver = sales.over