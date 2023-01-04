# Este ficheiro contém as funções de suporte
import msg

NO_CHARS = 20
ACCOES = 'Adicionar', 'Consultar', 'Atualizar', 'Eliminar', 'Terminar'
KEYS = 'categoria', 'nome', 'quantidade', 'preco'

def draw_menu():
        menu = 'MENU'.center(NO_CHARS, '-')
        for idx, accao in enumerate(ACCOES):
                menu += '\n 0' + str(idx + 1) + ' - ' + accao
        else:
            menu += '\n' + '-' .center(NO_CHARS, '-')
        print(menu)

def check_input(accao: str):
        try:
                return int(accao)
        except ValueError:
                print(msg.erro_0)
                check:input(input(msg.ACCAO))

def find_product():

    """return idx"""

"""def set_product():
        categoria = input('Insira a categoria do produto: ')
        nome = input('Insira o nome do produto: ')
        quantidade = input('Insira a quantidade: ')
        valor = input('Insira o valor unitário: ')
        dict(categoria=categoria, nome=nome, quantidade=quantidade, valor=valor)"""

def set_product(keys = KEYS, catalogo={}):

    produto = dict(zip(keys, [0] * len(keys)))

    for k in keys:
        produto[k] = input(f'\t• Indique {k}: ')
    else:
        catalogo.setdefault(len(catalogo), produto)
        return produto, catalogo



def get_product():
        """Esta função consulta uma entrada/categoria"""



def delete_product():
        """Esta função elimina uma entrada/categoria"""
        # TODO: Desenvolve esta função
        pass

def update_product():
        """Esta função atualiza uma entrada/categoria"""
        # TODO: Desenvolve esta função
        pass




