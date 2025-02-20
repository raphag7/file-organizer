import os
import shutil

def organizar_arquivos(diretorio):
  
    if not os.path.exists(diretorio):
        print("Diretório não encontrado.")
        return

       for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)

               if os.path.isfile(caminho_arquivo):
                       extensao = os.path.splitext(arquivo)[1][1:].lower()
            if not extensao:
                extensao = "Sem_Extensao"  
            
            
            pasta_destino = os.path.join(diretorio, extensao)
            os.makedirs(pasta_destino, exist_ok=True)

            
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
