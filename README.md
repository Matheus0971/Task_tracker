# TaskTracker CLI - Conteinerização e Orquestração (Bootcamp II)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v2-2496ED?style=flat&logo=docker&logoColor=white)](https://docs.docker.com/compose/)

O **TaskTracker** é uma aplicação interativa via linha de comando (CLI) desenvolvida em Python para gerenciamento inteligente de tarefas, cálculo dinâmico de score de prioridade e rastreamento de prazos.

Este repositório representa a **Fase 3: Engenheiro(a) DevOps** do Desafio Final do Bootcamp II, contendo a infraestrutura completa de conteinerização com Docker e orquestração interativa com Docker Compose.

---

## 🚀 Como Executar a Aplicação

Os comandos abaixo foram desenhados para reprodução rápida e sem atrito.

### 1. Como construir a imagem:
```bash
docker build -t tasktracker-app .
```

### 2. Como rodar o container em modo isolado:
```bash
docker run -it tasktracker-app
```

### 3. Como rodar via orquestração (Recomendado):
```bash
docker compose run tasktracker-app
```

---

## 📁 Árvore de Diretórios (Rastreabilidade)

O projeto mantém rigorosamente o histórico evolutivo de todas as etapas (Fase 1: Arquiteto de Software, Fase 2: Desenvolvedor, Fase 3: Engenheiro DevOps):

```text
tasktracker-projeto/
├── .gitignore               # Regras de exclusão de arquivos transitórios e caches
├── docs/                    # Documentos de entrega e planejamento
│   ├── Entrega Etapa Inicial.pdf
│   └── Entrega_Final_Fase3.pdf
├── src/
│   └── main.py              # Código Python funcional da CLI (Fase 2)
├── Dockerfile               # Receita de empacotamento da aplicação (Fase 3)
├── docker-compose.yml       # Orquestração do canal interativo de terminal (Fase 3)
└── README.md                # Guia técnico e documentação da infraestrutura (Fase 3)
```

---

## 🛠️ Decisões Técnicas de Engenharia DevOps

### Deep Dive: `Dockerfile`
O empacotamento foi concebido seguindo as melhores práticas de imagens enxutas e eficientes:

- **`FROM python:3.11-slim`**: Utiliza uma distribuição Linux mínima com o runtime oficial do Python 3.11, reduzindo expressivamente o tamanho final da imagem e a superfície de vulnerabilidades.
- **`WORKDIR /app`**: Define o diretório central de execução no container, garantindo isolamento e previsibilidade de caminhos relativos.
- **`ENV PYTHONUNBUFFERED=1`**: Desativa o buffer interno de entrada/saída padrão do Python. Essencial para que os menus, perguntas e mensagens sejam exibidos instantaneamente na tela sem atrasos de buffer.
- **`COPY src/ /app/src/`**: Injeta apenas o código-fonte necessário para dentro do container, respeitando a separação de responsabilidades.
- **`CMD ["python", "src/main.py"]`**: Define o comando de inicialização padrão da CLI.

### Deep Dive: `docker-compose.yml` (Orquestração e Interatividade)
Por padrão, contêineres Docker executam em modo não interativo e desconectados do canal de entrada do usuário (`stdin`). Como a aplicação necessita interagir com o usuário via `input()`:

- **`stdin_open: true`**: Mantém o canal de entrada padrão (`stdin`) aberto e aguardando dados da máquina local.
- **`tty: true`**: Aloca um pseudoterminal (TTY virtual), permitindo que a CLI renderize menus, quebras de linha e receba comandos do teclado como em um terminal nativo.

| Parâmetro | Dockerfile | docker-compose.yml |
| :--- | :--- | :--- |
| **Papel** | Empacota a aplicação e dependências estáticas | Orquestra a execução interativa da CLI |
| **Saída** | Imagem Docker (`tasktracker-app`) | Container interativo conectado ao terminal |
| **Comando Chave** | `docker build` | `docker compose run` |
| **Obrigatório na Raiz** | Sim | Sim |

---

## 💻 Funcionalidades do TaskTracker CLI

A aplicação oferece um menu interativo com validações robustas:

1. **Cadastrar nova tarefa**:
   - Validação de nome obrigatório e unicidade.
   - Normalização Unicode para tratamento de acentos e maiúsculas/minúsculas.
   - Classificação de dificuldade (`fácil`, `média`, `difícil`).
   - Validação avançada de datas (anos bissextos, meses e dias válidos).
   - Cálculo automático de dias restantes e **Score de Prioridade** ponderado pelo nível de dificuldade.
2. **Visualizar tarefas cadastradas**:
   - **Tarefas pendentes e no prazo**: Ordenadas de forma decrescente pelo Score de Prioridade.
   - **Tarefas atrasadas**: Identificadas automaticamente com base na data do sistema.
   - **Tarefas concluídas**: Histórico de tarefas finalizadas.
3. **Marcar tarefa como concluída**:
   - Localização por nome (insensível a acentuação) e atualização do status.
4. **Sair da aplicação**:
   - Encerramento seguro do processo (`sys.exit()`).

---


## 👤 Autor

- **Nome:** Matheus Henrique Santos de Almeida
- **GitHub:** [@Matheus0971](https://github.com/Matheus0971)
- **Repositório:** [Task_tracker](https://github.com/Matheus0971/Task_tracker)
