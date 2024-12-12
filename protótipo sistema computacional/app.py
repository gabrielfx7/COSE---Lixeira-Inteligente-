# Exemplo de controle de lixeira inteligente
peso_lixeira = 85  # 85% de capacidade
hora_dia = 1  # 1 = dia, 0 = noite

# Usando porta AND para determinar a necessidade de coleta
if peso_lixeira > 80 and hora_dia == 1:
    print("Lixeira cheia, agendar coleta!")
else:
    print("Lixeira não cheia, aguardar próxima verificação.")
# Exemplo de escalonamento de tarefas de coleta
tarefas = [("coleta_lixeira1", 1), ("coleta_lixeira2", 2), ("verificar_estado", 3)]  # (tarefa, prioridade)
tarefas.sort(key=lambda x: x[1])  # Ordena pela prioridade

for tarefa, prioridade in tarefas:
    print(f"Executando tarefa: {tarefa} com prioridade: {prioridade}")
from cryptography.fernet import Fernet

# Gerar chave
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Criptografar dado
data = "Lixeira 1: 85% cheia"
encrypted_data = cipher_suite.encrypt(data.encode())

# Descriptografar
decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
print(decrypted_data)
from cryptography.fernet import Fernet

# Gerar chave
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Criptografar dado
data = "Lixeira 1: 85% cheia"
encrypted_data = cipher_suite.encrypt(data.encode())

# Descriptografar
decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
print(decrypted_data)
