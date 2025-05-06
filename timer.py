import argparse
import time
import platform
import os

def notificar(mensagem):
    sistema = platform.system()
    
    if sistema == "Linux":
        os.system(f'notify-send "Timer" "{mensagem}"')
    elif sistema == "Darwin":  # macOS
        os.system(f'''osascript -e 'display notification "{mensagem}" with title "Timer"' ''')
    elif sistema == "Windows":
        print("⚠️ Notificação visual não suportada no Windows nesse script. Mensagem:")
        print(mensagem)
    else:
        print("Sistema não suportado. Mensagem:")
        print(mensagem)

def iniciar_timer(minutos):
    segundos = minutos * 60
    print(f"⏳ Iniciando temporizador por {minutos} minutos...")
    time.sleep(segundos)
    notificar("⏰ Tempo encerrado!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Temporizador simples de linha de comando")
    parser.add_argument("--minutos", type=int, required=True, help="Duração do temporizador em minutos")

    args = parser.parse_args()
    iniciar_timer(args.minutos)
