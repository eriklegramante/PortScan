# PortScan.py

Um scanner de portas simples e rápido desenvolvido em Python, com suporte a identificação de serviços conhecidos, animação de carregamento e múltiplos modos de varredura.  
O projeto foi estruturado em módulos para facilitar manutenção e expansão.

---

## 📂 Estrutura do Projeto

```
📁 projeto/
│── PortScan.py                # Arquivo principal do programa
│── verify.py                  # Módulo de verificação com funções utilitárias
│── port_database.py           # "Database" de portas e serviços conhecidos
│── README.md                  # Documentação do projeto
```

---

## 🛠 Bibliotecas Utilizadas

- **socket** → Comunicação TCP/IP para testar portas.
- **pyfiglet** → Gera arte ASCII para título do programa.
- **sys** → Manipulação de saída no terminal.
- **time** → Animação de carregamento e medição de tempo de execução.
- **colorama** → Cores no terminal para realçar mensagens.
- **concurrent.futures** → Execução de múltiplas verificações de porta em paralelo (melhor desempenho).
- **verify (módulo interno)** → Contém funções `display_port_services()` e `print_port_status()` para exibir resultados.
- **port_database (módulo interno)** → Contém o dicionário `PORT_SERVICES` com portas e serviços conhecidos.

---

## 📜 Funcionalidades

- **[1] Specific port** → Verifica uma porta específica em um IP.
- **[2] Test all ports (1-65535)** → Varre todas as portas TCP.
- **[3] Choose ports** → Verifica apenas as portas informadas manualmente.
- **[4] Available Port Services** → Lista todas as portas e serviços conhecidos no `port_database`.
- **[5] Exit** → Fecha o programa.

---

## 🔍 Detalhes Técnicos

- O programa identifica portas abertas e mostra o serviço correspondente (se estiver no banco de dados).
- O modo de varredura usa **ThreadPoolExecutor** para verificar várias portas simultaneamente, acelerando o processo.
- Exibe tempo total da varredura.
- Mensagens coloridas com **Colorama**:
  - **Verde** → Porta aberta
  - **Vermelho** → Porta fechada
- Usa `pyfiglet` para exibir um título estilizado.

---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/eriklegramante/portscan.git
cd portscan
```

### 2️⃣ Instalar dependências
```bash
pip install pyfiglet colorama
```

---

## ▶️ Como Executar

No terminal:
```bash
python PortScan.py
```

---

## 📌 Exemplo de Uso

**Varredura de porta única**
```
[1] - Specific port
[IP]: scanme.nmap.org
[PORT]: 22

[OPEN] Port 22 (SSH)
```

**Varredura de múltiplas portas**
```
[3] - Choose ports
[IP]: scanme.nmap.org
[PORTS] (separated by commas): 21,22,80

[CLOSED] Port 21 (FTP Control)
[OPEN] Port 22 (SSH)
[OPEN] Port 80 (HTTP)
```

---

## 📦 Módulos

### **PortScan.py**  
Arquivo principal com o loop do menu, leitura de entrada do usuário, controle da execução e chamada das funções.

### **port_database.py**  
Contém o dicionário:
```python
PORT_SERVICES = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    ...
}
```

### **verify.py**  
- **`print_port_status(port, status)`** → Exibe porta, status e serviço.
- **`display_port_services()`** → Lista todas as portas conhecidas.

---

## ⚠️ Aviso Legal

Este projeto é destinado a **uso educacional e testes autorizados**.  
Nunca execute varreduras em redes ou sistemas sem permissão explícita do proprietário.  
O uso indevido pode violar leis locais e resultar em penalidades.

---

## 📄 Licença
Você pode distribuir, modificar e usar este código livremente, desde que não seja para fins ilegais.
