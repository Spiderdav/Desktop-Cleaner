import os
import sys

import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

IMAGENS = [".png", ".jpeg", ".jpg", ".gif", ".bmp"]
VIDEOS = [".mp4", ".avi", ".mkv", ".mov", ".wav"]
DOCUMENTOS = [".pdf", ".docx", ".xlsx", ".txt", ".pptx"]
ETC = [".zip", ".rar", ".exe", ".dll"]

def janela():
    janela = ctk.CTk()
    janela.title("Desktop Cleaner")
    janela.geometry("800x600")

    janela.resizable(True, True)

    frame_imagens = ctk.CTkFrame(master=janela, border_width=5)
    frame_imagens.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

    frame_videos = ctk.CTkFrame(master=janela, border_width=5)
    frame_videos.grid(row=1, column=0,pady=10, padx=10, sticky="ew")

    frame_documentos = ctk.CTkFrame(master=janela, border_width=5)
    frame_documentos.grid(row=2, column=0,pady=10, padx=10, sticky="ew")

    frame_etc = ctk.CTkFrame(master=janela, border_width=5)
    frame_etc.grid(row=3, column=0,pady=10, padx=10, sticky="ew")

    botões(frame_imagens, frame_videos, frame_documentos, frame_etc)

    opcao_escolha_extensoes = ctk.CTkOptionMenu(janela, values=["Escolhe uma extensão"])
    opcao_escolha_extensoes.grid(row=7, column=0, padx=20, pady=20, sticky="ew")

    # janela.grid_columnconfigure(0, weight=1)
    # Escolha das opções das categorias
    opcao_menu = ctk.StringVar(value="Escolhe uma categoria")
    opcao_escolha = ctk.CTkOptionMenu(janela, values=["IMAGENS", "DOCUMENTOS", "ETC", "VIDEOS"],
                                      command=lambda escolha: atualizar_submenu(escolha, opcao_escolha_extensoes))
    opcao_escolha.grid(row=6, column=0, padx=20, pady=20, sticky="ew")

    janela.grid_rowconfigure(0, minsize=80)
    janela.grid_rowconfigure(1, minsize=80)
    janela.grid_rowconfigure(2, minsize=80)
    janela.grid_rowconfigure(3, minsize=80)

    janela.mainloop()

def organizar():
    pass
def botões(frame_imagens, frame_videos, frame_documentos, frame_etc):

    label_imagens = ctk.CTkLabel(frame_imagens, text="label de teste imagens", fg_color="transparent", anchor="w", justify="left")
    label_imagens.grid(row=0, column=0, sticky="w", pady=5, padx=5)

    label_videos = ctk.CTkLabel(frame_videos, text="label de teste videos", fg_color="transparent", anchor="w", justify="left")
    label_videos.grid(row=0, column=0, sticky="w", pady=5, padx=5)

    label_documentos = ctk.CTkLabel(frame_documentos, text="label de teste documentos", fg_color="transparent", anchor="w", justify="left")
    label_documentos.grid(row=0, column=0, sticky="w", pady=5, padx=5)

    label_etc = ctk.CTkLabel(frame_etc, text="label de teste etc", fg_color="transparent", anchor="w", justify="left")
    label_etc.grid(row=0, column=0, sticky="w", pady=5, padx=5)

def atualizar_submenu(escolha, opcao_escolha_extensoes):
    categorias = {
        "IMAGENS": IMAGENS,
        "VIDEOS": VIDEOS,
        "DOCUMENTOS": DOCUMENTOS,
        "ETC": ETC
    }
    if escolha in categorias:
        extensoes = categorias[escolha]
    else:
        extensoes = []
    extensoes = categorias.get(escolha, ["Escolhe uma extensão"])
    opcao_escolha_extensoes.configure(values=extensoes)

janela()