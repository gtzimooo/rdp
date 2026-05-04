import os
import subprocess
import time

# Seus dados
TOKEN = "3DExStdf915LNZ3Xu3Vujp1sRku_gbRaCzoMM2eqz89CgBXg"

def setup_ngrok():
    print("--- Iniciando Tunelamento para Acesso Remoto ---")
    
    # 1. Configura o Token (Isso só precisa ser feito uma vez)
    print("[+] Configurando Token...")
    os.system(f"ngrok config add-authtoken {TOKEN}")
    
    # 2. Abre o túnel TCP na porta 3389 (Porta padrão do Windows Remote Desktop)
    print("[+] Abrindo túnel na porta 3389...")
    print("[!] ATENÇÃO: Copie o endereço que aparecer em 'Forwarding' abaixo.")
    print("[!] Exemplo: 0.tcp.sa.ngrok.io:12345\n")
    
    try:
        # Inicia o ngrok
        subprocess.run(["ngrok", "tcp", "3389"])
    except FileNotFoundError:
        print("\n[ERRO] O ngrok.exe não foi encontrado!")
        print("Baixe o ngrok.exe e coloque na mesma pasta deste script.")

if __name__ == "__main__":
    setup_ngrok()
    
