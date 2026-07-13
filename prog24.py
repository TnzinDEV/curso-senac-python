c = int(input("Digite o codigo de error: "))
match c:
    case 200:
        print("sucesso! tudo certo com a sua requisiçao.")
    case 400:
        print("erro do cliente: requisiçao mal formada. ")
    case 401 | 403:
        print("erro de permissao: voce nao tem acesso a esta pagina.")
    case 404:
        print("pagina nao encontrada. ")
    case 500 | 503:
        print("erro no servidor: nosso sistema esta instavel no momento")
    case _:
        print("codigo http {codigo_status} desconhecido. ")