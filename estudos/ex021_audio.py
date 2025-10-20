#Reproduzir um arquivo MP3

import pygame
import os

# Caminho completo do arquivo MP3
arquivo = r"C:\Users\jailton.pereira\Documents\meus-projetos\Python\estudos\ex021_steve_wonder.mp3"

# Verifica se o arquivo existe
if not os.path.exists(arquivo):
    print(f"❌ Arquivo não encontrado: {arquivo}")
else:
    print("🎵 Iniciando reprodução de áudio...")

    # Inicializa o mixer e o pygame
    pygame.mixer.init()
    pygame.init()

    # Carrega e reproduz o arquivo MP3
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

    # Aguarda até terminar de tocar
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    print("✅ Reprodução finalizada.")
