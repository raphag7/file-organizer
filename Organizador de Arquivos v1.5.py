import os
import shutil

def organizar_arquivos(diretorio):
    """
    Organiza os arquivos de um diretório, movendo-os para pastas de acordo com suas extensões.
    """
    if not os.path.exists(diretorio):
        print("Diretório não encontrado.")
        return

    # Lista todos os arquivos no diretório
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)

        # Ignora diretórios, processa apenas arquivos
        if os.path.isfile(caminho_arquivo):
            # Obtém a extensão do arquivo (sem o ponto)
            extensao = os.path.splitext(arquivo)[1][1:].lower()
            if not extensao:
                extensao = "Sem_Extensao"  # Para arquivos sem extensão
            
            # Cria a pasta da extensão, se não existir
            pasta_destino = os.path.join(diretorio, extensao)
            os.makedirs(pasta_destino, exist_ok=True)

            # Move o arquivo para a pasta correspondente
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
            print(f"Movido: {arquivo} -> {pasta_destino}/")

if __name__ == "__main__":
    while True:
        pasta_alvo = input("Digite o caminho da pasta que deseja organizar: ")
        organizar_arquivos(pasta_alvo)
        
        continuar = input("Deseja organizar outra pasta? (s/n): ").strip().lower()
        if continuar != 's':
            print("Encerrando o programa...")
            break
