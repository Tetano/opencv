# Definindo funções que poderão ou não ser implementadas ao longo da disciplina ou curso.
# ------------- Funções p/ reconhecimento facial -----------#
import cv2

def camera():
    video = cv2.VideoCapture(0)
    while True:
        connectado, frame = video.read()
        cv2.imshow('Reconhecimento De Imagem', frame)

        if cv2.waitKey(1) == ord('q'):
            break
            video.release()
            cv2.DestroyAllWindowns


valor = ''
senhas = []
def autenticar():
    senhas = ['1234', '2345','3456', '4567']
    valor = input()
    if valor in senhas:
        print('Senha correta, autenticado')
       # index = senhas.index(valor)
       # print('É a',index,'Senha')
        camera()
    else:
        print(valor,'Não é uma senha valida')
#------------------------Funções Prototipo------------------
#------------------------Prioridade Máxima||||||||||||||||
#def cadastrar(): -- Será cadastrado no sistema podendo ser do tipo pessoa ou administrador.
#def excluir():  -- Fica excluido uma instancia do objeto pessoa.
#------------------------Prioridade 2|||||||||||||||||||||
#def promover(): -- Será promovido com uma instancia do objeto  administrador.
#def revogar(): -- Será revogado da instancia do objeto adiministrador e passará a ser comum.
#def categorizar(): -- Categorizar perfis de acesso mais alto ao mais baixo níveis de acesso.
#------------------------Prioridade 1|||||||||||||||||||||
#def notas(): -- Atualização controle de versão e parametrização
#def sobre(): -- Disponibilidade, desenvolvimento envolvidos
#def duvidas(): -- Solução de duvidas frequentes
#def opcoes(): -- Opções pequenas configurações
#-------------------Fora das Funções------------------------#
autenticar()


