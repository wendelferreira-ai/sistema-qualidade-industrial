#Listas que simulam as caixas e peças.
pecas = []
caixas = []
caixa_atual = []

#Função de avaliação dentro dos critérios impostos.
def avaliar_peca(peso, cor, comprimento):
    motivos = []
    if not (95 <= peso <= 105):
        motivos.append("Peso fora do intervalo (95g a 105g)")
    if cor not in ["azul", "verde"]:
        motivos.append("Cor invalida (aceitas: azul ou verde)")
    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do intervalo (10cm a 20cm)")
    return motivos
    
#Função de cadastrar uma peça
def cadastrar_peca():
    id_peca = len(pecas) + 1
    peso = float(input("Peso (g): "))
    cor = input("Cor: ").strip().lower()
    comprimento = float(input("Comprimento (cm): "))

    motivos = avaliar_peca(peso, cor, comprimento)
    aprovada = len(motivos) == 0

    #Dicionário que é utilizado como banco de dados temporário
    peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento,
            "aprovada": aprovada, "motivos": motivos}
    pecas.append(peca)

    if aprovada:
        caixa_atual.append(id_peca)
        print(f"Peca {id_peca} APROVADA e adicionada na caixa atual ({len(caixa_atual)}/10)")
        if len(caixa_atual) == 10:
            caixas.append(list(caixa_atual))
            caixa_atual.clear()
            print(f"Caixa {len(caixas)} fechada!")
    else:
        print(f"Peca {id_peca} REPROVADA:")
        for m in motivos:
            print(f"  - {m}")
            
#Função de listar as peças
def listar_pecas():
    if not pecas:
        print("Nenhuma peca cadastrada.")
        return
    for p in pecas:
        status = "APROVADA" if p["aprovada"] else "REPROVADA"
        print(f"ID {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comp: {p['comprimento']}cm | {status}")
        if not p["aprovada"]:
            for m in p["motivos"]:
                print(f"  - {m}")

#Função de remover as peças.
def remover_peca():
    id_remover = int(input("ID da peca a remover: "))
    for p in pecas:
        if p["id"] == id_remover:
            pecas.remove(p)
            if p["aprovada"] and id_remover in caixa_atual:
                caixa_atual.remove(id_remover)
            print(f"Peca {id_remover} removida.")
            return
    print("Peca nao encontrada.")

#Função de listar as caixas
def listar_caixas():
    if not caixas:
        print("Nenhuma caixa fechada ainda.")
    for i, c in enumerate(caixas, 1):
        print(f"Caixa {i}: {c}")
    print(f"Caixa em aberto: {caixa_atual} ({len(caixa_atual)}/10 pecas)")


#Função de gerar o relatório.

def relatorio():
    aprovadas = [p for p in pecas if p["aprovada"]]
    reprovadas = [p for p in pecas if not p["aprovada"]]
    total_caixas = len(caixas) + (1 if caixa_atual else 0)

    print(f"\n--- RELATORIO FINAL ---")
    print(f"Total de pecas: {len(pecas)}")
    print(f"Aprovadas: {len(aprovadas)}")
    print(f"Reprovadas: {len(reprovadas)}")
    print(f"Caixas utilizadas: {total_caixas}")

    if reprovadas:
        print("\nMotivos de reprovacao:")
        for p in reprovadas:
            print(f"  ID {p['id']}: {', '.join(p['motivos'])}")


#Menu de opção que chama as funções
while True:
    print("\n1. Cadastrar nova peca")
    print("2. Listar pecas")
    print("3. Remover peca")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatorio final")
    print("0. Sair")

    opcao = input("Opcao: ")

    if opcao == "1":
        cadastrar_peca()
    elif opcao == "2":
        listar_pecas()
    elif opcao == "3":
        remover_peca()
    elif opcao == "4":
        listar_caixas()
    elif opcao == "5":
        relatorio()
    elif opcao == "0":
        break
    else:
        print("Opcao invalida.")
