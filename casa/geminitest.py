import re
# ==========================================
# FUNÇÕES DE VALIDAÇÃO E AUXILIARES
# ==========================================

def limpar_apenas_numeros(texto):
    """Remove qualquer caractere que não seja número."""
    return re.sub(r'\D', '', texto)

def obter_input_valido(mensagem, tipo_validacao):
    """Garante que o usuário digite um dado válido."""
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            print("❌ Este campo não pode ficar vazio. Tente novamente.")
            continue
            
        if tipo_validacao == "nome":
            if entrada.replace(" ", "").isalpha() or len(entrada) > 2:
                return entrada.title()
            print("❌ Nome inválido. Use apenas letras.")
            
        elif tipo_validacao == "idade":
            if entrada.isdigit() and 0 < int(entrada) < 120:
                return int(entrada)
            print("❌ Idade inválida. Digite um número inteiro.")
            
        elif tipo_validacao == "cpf":
            numeros = limpar_apenas_numeros(entrada)
            if len(numeros) == 11:
                return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
            print("❌ CPF inválido. Digite exatamente 11 números.")
            
        elif tipo_validacao == "telefone":
            numeros = limpar_apenas_numeros(entrada)
            if len(numeros) in [10, 11]:
                return f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}" if len(numeros) == 11 else f"({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}"
            print("❌ Telefone inválido. Digite o DDD + número.")

# ==========================================
# FLUXO PRINCIPAL DO SISTEMA
# ==========================================

def executar_sistema():
    largura = 60
    linha = "-" * largura
    dupla_linha = "=" * largura
    
    # --- 1. ETAPA DE CADASTRO ---
    print(linha)
    print("Realize seu cadastro :-]".center(largura))
    print(linha)
    
    nome = obter_input_valido("Digite seu nome: ", "nome")
    print(linha)
    idade = obter_input_valido("Digite sua idade: ", "idade")
    print(linha)
    cpf = obter_input_valido("Digite seu [CPF] (apenas números): ", "cpf")
    print(linha)
    tel = obter_input_valido("Digite seu telefone com DDD (apenas números): ", "telefone")
    print(linha)
    
    # --- 2. CONFIRMAÇÃO DO CADASTRO ---
    print("\n" + dupla_linha)
    print(" TABELA DE CONFIRMAÇÃO DE INFORMAÇÕES ".center(largura, "="))
    print(dupla_linha)
    print(f" Seu Nome:      {nome}")
    print(f" Sua Idade:     {idade} anos")
    print(f" Seu CPF:       {cpf}")
    print(f" Seu Telefone:  {tel}")
    print(dupla_linha)
    print("Você foi cadastrado com sucesso!".center(largura))
    print("Seja bem-vindo à Embare KRAF :-]".center(largura))
    print("Agradecemos a sua escolha!".center(largura))
    print(dupla_linha + "\n")
    
    # --- 3. MENU DE COMPRAS (SACOLAS) ---
    print(linha)
    print("Olá! Seja bem-vindo à EMBARE KRAFT".center(largura))
    print("Aqui vai a nossa lista de tamanhos disponíveis:".center(largura))
    print(linha)
    
    # Cadastro das sacolas e seus respectivos preços por unidade
    sacolas_precos = {
        "18x24x12": 1.10,
        "22x32x12": 1.20,
        "22x34x14": 1.40,
        "23x39x15": 1.60
    }
    
    # Exibe as opções formatadas
    for tamanho, preco in sacolas_precos.items():
        print(f" 🛍️  Tamanho: {tamanho:<12} | Preço Unitário: R$ {preco:.2f}".center(largura))
    print(linha)
    
    # Seleção do tamanho desejado
    while True:
        tamanho_escolhido = input("Qual tamanho de sacola você deseja?: ").strip()
        if tamanho_escolhido in sacolas_precos:
            break
        print("❌ Tamanho inválido ou não encontrado. Escolha um dos tamanhos da lista.")
    print(linha)
    
    # Seleção da quantidade
    while True:
        try:
            qnt = int(input("Digite a quantidade que você deseja: "))
            if qnt > 0:
                break
            print("❌ A quantidade deve ser maior que zero.")
        except ValueError:
            print("❌ Por favor, digite um número inteiro válido.")
    print(linha)
    
    # --- 4. CÁLCULO E FINALIZAÇÃO ---
    preco_unitario = sacolas_precos[tamanho_escolhido]
    total_pagamento = qnt * preco_unitario
    
    print("\n" + dupla_linha)
    print(" RESUMO DO PEDIDO ".center(largura, "="))
    print(dupla_linha)
    print(f" Item: Sacola Kraft {tamanho_escolhido}")
    print(f" Quantidade: {qnt} unidades")
    print(f" Valor Unitário: R$ {preco_unitario:.2f}")
    print(f" VALOR TOTAL A PAGAR: R$ {total_pagamento:.2f}")
    print(dupla_linha)
    
    # Instruções de Pix
    print("Para realizar o pagamento, utilize a chave Pix abaixo:".center(largura))
    print("\n🗝️  Chave Pix: pix@embarekraft.com.br\n".center(largura))
    print("Obrigado pela preferência e ótimas vendas!".center(largura))
    print(linha)

if __name__ == "__main__":
    executar_sistema()