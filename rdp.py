import socket
import getpass
import os
import subprocess

def get_ip():
    try:
        # Conecta a um endereço externo para garantir que pega o IP da interface de rede ativa
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "Não foi possível identificar o IP"

def set_windows_password(username, password):
    try:
        # Executa o comando net user para definir a senha
        result = subprocess.run(['net', 'user', username, password], capture_output=True, text=True)
        if result.returncode == 0:
            return True
        else:
            print(f"Erro ao definir senha: {result.stderr}")
            return False
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False

def main():
    print("--- Configuração de Acesso Remoto ---")
    
    user = getpass.getuser()
    ip = get_ip()
    
    print(f"\n[+] Usuário identificado: {user}")
    print(f"[+] Endereço IP Local: {ip}")
    
    # No Windows, é difícil checar se "tem senha" sem tentar logar,
    # então vamos perguntar ou forçar a criação para garantir o RDP.
    
    print("\nO Acesso Remoto exige uma senha obrigatória.")
    opcao = input(f"Você já tem uma senha definida para '{user}'? (s/n): ").lower()
    
    if opcao == 'n':
        nova_senha = input("Digite a nova senha que deseja criar: ")
        confirmacao = input("Confirme a nova senha: ")
        
        if nova_senha == confirmacao:
            if set_windows_password(user, nova_senha):
                print("\n[OK] Senha definida com sucesso!")
                senha_final = nova_senha
            else:
                print("\n[!] Falha ao definir senha. Verifique se rodou o script como ADMINISTRADOR.")
                return
        else:
            print("\n[!] As senhas não coincidem.")
            return
    else:
        senha_final = "Sua senha atual"

    print("\n" + "="*30)
    print("DADOS PARA LOGIN REMOTO:")
    print(f"Computador/IP: {ip}")
    print(f"Usuário:       {user}")
    print(f"Senha:         {senha_final}")
    print("="*30)
    print("\nCertifique-se de que o 'Acesso Remoto' está habilitado nas Configurações do Windows.")

if __name__ == "__main__":
    main()
