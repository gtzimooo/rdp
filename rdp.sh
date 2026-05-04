#!/bin/bash

# Seu Token
TOKEN="3DExStdf915LNZ3Xu3Vujp1sRku_gbRaCzoMM2eqz89CgBXg"

echo "--- Configurando Acesso Remoto via Ngrok (Bash Edition) ---"

# 1. Aplica o token
./ngrok.exe config add-authtoken $TOKEN

echo "[+] Token configurado!"
echo "[+] Iniciando túnel na porta 3389 (Região: Brasil)..."
echo "[!] IMPORTANTE: Copie o endereço em 'Forwarding' (ex: 0.tcp.sa.ngrok.io:12345)"
echo "[!] Pressione CTRL+C para fechar o túnel."

# 2. Inicia o túnel TCP na região da América do Sul
./ngrok.exe tcp --region sa 3389
