import os

lista_departamentos = ['Dpto Tributário', 'Dpto Tributario', 'Dpto Contabil', 'Dpto Contábil', 'Dpto Pessoal']

os.chdir('o:\clientes')

for path in os.listdir():
    try:
        for subpath in os.listdir(path):
            if subpath in lista_departamentos:
                nova_pasta = os.getcwd() + os.sep + path + os.sep + subpath + os.sep + '2023'
                if not os.path.exists(nova_pasta):
                    os.mkdir(nova_pasta)
                    print(nova_pasta)
    except NotADirectoryError:
        pass

    
    