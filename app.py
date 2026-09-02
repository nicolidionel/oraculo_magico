import os
import random


def exibir_nome_programa():
    os.system('cls')
    print(
        'Bem-vindo ao Oráculo Mágico!\n'
        'Onde a imaginação e a magia se encontram com a realidade '
        'para tornar cada dia mais divertido — sozinho ou comigo!\n'
        '\nEscolha sua jornada do dia:\n'
    )


def exibir_opcoes():
    print('1 - Quero partir sozinho em uma aventura fantástica!')
    print('2 - Quero me juntar à minha companheira em uma missão extraordinária!')
    print('3 - Quero ouvir uma mensagem especial do Oráculo!')
    print('4 - Quero encerrar minha jornada por hoje.\n')


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite aqui o número referente à sua escolha, e precione Enter para confirmar: '))

        if opcao_escolhida == 1:
            sorteio_missao_sozinho()
            voltar_menu()

        elif opcao_escolhida == 2:
            sorteio_desafio_acompanhado()
            voltar_menu()

        elif opcao_escolhida == 3:
            sorteio_mensagem()
            voltar_menu()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()

def voltar_menu():
    input('Pressione Enter para voltar ao menu principal.')
    main()


def finalizar_app():
    os.system('cls')
    print(
        'Encerrando a sua jornada por aqui? '
        'Ou dando uma pequena pausa? '
        'De qualquer forma, até logo! :)\n')
    voltar_menu()


def opcao_invalida():
    print('\nOps... Opção inválida!\n')
    input('Pressione Enter para voltar ao menu principal.')
    main()


# ----------------------------------------------------------

missao_sozinho = [
    '\nPense em um final surpreendentemente inesperado para uma história de ficção e escreva um pequeno conto sobre.\n',
    '\nBater e ultrapassar a sua atual meta de caminhada!\n',
    '\nPrepare uma receita culinária do seu jogo favorito!\n',
    '\nAprenda e faça um origami de nivel difícil\n',
    '\nAprenda uma posição nova de yoga!\n',
    '\nPense em uma situação rotineira e trasforme em um universo paralelo caótico, escreva sobre.\n',
    '\nEscreva uma carta para ser lida nessa mesma data do ano que vem, sobre você mesmo ou o que achar importânte.\n',
    '\nSeu desafio hoje é: Trazer para casa um objeto aleatório e engraçado que encontrar por ai.\n',
    '\nFaça um\n',

]


def sorteio_missao_sozinho():
    if len(missao_sozinho) == 0:
        print('\nVocê esgotou todas as missões! Parabéns!\n')
        return

    definido = random.choice(missao_sozinho)
    print(definido)
    missao_sozinho.remove(definido)


desafio_acompanhado = [
    '\nQue tal desbravar um campo isolado, estender uma toalha quadriculada, comer alguma besteira e jogar conversa fora?\n',
    '\nDesafio ancestral: Montar um quebra-cabeça contendo uma fotografia da época em que as guilhotinas ainda eram retas...\n',
    '\nCaça ao tesouro no estilo, você morreu, virou fantasma e agora eu preciso descobrir quem foi o maldito.\n',
    '\nDesafio da comida colorida (não é sobre salada).\n',
    '\nPreparar a própria pizza não remunerada e de sabor duvidoso.\n',
    '\nEnsinar o outro algo novo. (vpn de club penguim não conta mais)\n',
    '\nAcordar cedo, ver o nascer do sol, voltar para casa e dormir de novo.\n',
    '\nDegustação de comidas duvidosas do mercadinho da esquina.\n',
    '\nPintura as cegas de carictura... nem precisa das vendas. \n',

]

def sorteio_desafio_acompanhado():
    if len(desafio_acompanhado) == 0:
        print(
            'Que pena! Os desafios em casal acabaram por aqui. '
            'Logo teremos mais!')
        return

    escolhido = random.choice(desafio_acompanhado)
    print(escolhido)
    desafio_acompanhado.remove(escolhido)


mensagem = [
    '\nO Oráculo diz: confie na sua intuição! Realmente...\n',
    '\nUma surpresa está esperando por você! As vezes dizer sim pode surpreender.\n',
    '\nHoje a chance de encontrar moedas rolando por ai é grande... Fique de olho.\n',
    '\nSe você é o Supla, então por que tenta imitar a Ana Maria Braga?\n',
    '\nDa uma chance para aquele salgado duvidoso, vai que é gostosinho.\n',
    '\nHoje é o dia! Hora de treinar a mão ruim da punheta!\n',
    '\nSeu futuro revela uma soneca inesperada, seu ou do seu chefe? Não posso revelar todas as informações...\n',
    '\nAlgo incrível acontecerá hoje, ou talvez amanhã... O Oráculo também tem seus limites, descanse.\n',
    '\nA sorte virá até você. Provavelmente de delivery.\n',

]

def sorteio_mensagem():
    if len(mensagem) == 0:
        print(
            'Que pena! As mensagens acabaram por agora... '
            'Volte mais tarde :)')
        return

    e = random.choice(mensagem)
    print(e)
    mensagem.remove(e)


# ----------------------------------------------------------

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()