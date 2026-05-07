import anthropic
import os
import sys

# ─────────────────────────────────────────
#  Configuração
# ─────────────────────────────────────────
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "sua-api-key-aqui")

SYSTEM_PROMPT = """You are a helpful, concise and friendly AI assistant. 
Answer clearly and directly. If the user writes in Portuguese, respond in Portuguese.
If in English, respond in English."""

# ─────────────────────────────────────────
#  Cores para o terminal
# ─────────────────────────────────────────
class Colors:
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"

def print_banner():
    print(f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════╗
║         Claude Terminal Chat          ║
║     Powered by Anthropic Claude       ║
╚═══════════════════════════════════════╝
{Colors.RESET}
{Colors.YELLOW}Comandos:{Colors.RESET}
  {Colors.GREEN}sair{Colors.RESET} ou {Colors.GREEN}exit{Colors.RESET}  → encerra o chat
  {Colors.GREEN}limpar{Colors.RESET}         → limpa o histórico
  {Colors.GREEN}historico{Colors.RESET}      → mostra mensagens anteriores
""")

def print_message(role: str, content: str):
    if role == "user":
        print(f"\n{Colors.GREEN}{Colors.BOLD}Você:{Colors.RESET} {content}")
    else:
        print(f"\n{Colors.CYAN}{Colors.BOLD}Claude:{Colors.RESET} {content}\n")

def show_history(messages: list):
    if not messages:
        print(f"\n{Colors.YELLOW}Histórico vazio.{Colors.RESET}\n")
        return
    print(f"\n{Colors.YELLOW}─── Histórico ───{Colors.RESET}")
    for msg in messages:
        role = "Você" if msg["role"] == "user" else "Claude"
        color = Colors.GREEN if msg["role"] == "user" else Colors.CYAN
        print(f"{color}{role}:{Colors.RESET} {msg['content']}")
    print(f"{Colors.YELLOW}─────────────────{Colors.RESET}\n")

# ─────────────────────────────────────────
#  Chat principal
# ─────────────────────────────────────────
def chat():
    client = anthropic.Anthropic(api_key=API_KEY)
    messages = []

    print_banner()

    while True:
        try:
            user_input = input(f"{Colors.GREEN}Você:{Colors.RESET} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{Colors.YELLOW}Encerrando... Até logo!{Colors.RESET}\n")
            sys.exit(0)

        if not user_input:
            continue

        # Comandos especiais
        if user_input.lower() in ["sair", "exit", "quit"]:
            print(f"\n{Colors.YELLOW}Até logo!{Colors.RESET}\n")
            break

        if user_input.lower() in ["limpar", "clear"]:
            messages = []
            print(f"\n{Colors.YELLOW}Histórico limpo!{Colors.RESET}\n")
            continue

        if user_input.lower() in ["historico", "histórico", "history"]:
            show_history(messages)
            continue

        # Adiciona mensagem do usuário ao histórico
        messages.append({"role": "user", "content": user_input})

        # Chama a API
        try:
            print(f"\n{Colors.CYAN}{Colors.BOLD}Claude:{Colors.RESET} ", end="", flush=True)

            response = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                messages=messages
            )

            assistant_reply = response.content[0].text
            print(assistant_reply)
            print()

            # Salva resposta no histórico
            messages.append({"role": "assistant", "content": assistant_reply})

        except anthropic.AuthenticationError:
            print(f"\n{Colors.RED}Erro: API Key inválida. Verifique sua chave no arquivo .env{Colors.RESET}\n")
            break
        except anthropic.RateLimitError:
            print(f"\n{Colors.RED}Erro: Limite de requisições atingido. Aguarde um momento.{Colors.RESET}\n")
        except Exception as e:
            print(f"\n{Colors.RED}Erro inesperado: {e}{Colors.RESET}\n")

if __name__ == "__main__":
    chat()
