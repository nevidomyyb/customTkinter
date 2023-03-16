import customtkinter as ctk
from mensagems import mensagem, mensagem_funcionamento, mensagem_hardware
janela = ctk.CTk() #Criando a janela

janela._set_appearance_mode("light") #Setando a aparência 
janela.title("Wikipedia") #Setando o titulo da janela
janela.geometry("1280x700") #Setando o tamanho inicial da janela
janela.resizable(width=False, height=False) #Pode configurar se a altura/largura é reconfiguravel

frame_header = ctk.CTkFrame(master=janela, width=1280, height=30, fg_color="#DCDAD9").place(x=1, y=1)
frame_menu = ctk.CTkFrame(master=janela, width=280, height=700, fg_color="#DCDAD9").place(x=1, y=1)

historia_ativada = False
funcionamento_ativada =  False
hardware_ativada = False

def historia():
    global historia_ativada 
    global funcionamento_ativada
    global hardware_ativada
    funcionamento_ativada = False
    hardware_ativada = False
    if historia_ativada: return
    historia_ativada = True
    textbox.delete("0.0", "end")
    textbox.insert("0.0", mensagem)

def funcionamento():
    global funcionamento_ativada
    global historia_ativada
    global hardware_ativada
    historia_ativada = False
    hardware_ativada = False
    if funcionamento_ativada: return
    funcionamento_ativada = True
    textbox.delete("0.0", "end")
    textbox.insert("0.0", mensagem_funcionamento)

def hardware():
    global funcionamento_ativada
    global historia_ativada
    global hardware_ativada
    historia_ativada = False
    funcionamento_ativada = False
    if hardware_ativada: return
    hardware_ativada = True
    textbox.delete("0.0", "end")
    textbox.insert("0.0", mensagem_hardware)

btn_1 = ctk.CTkButton(
    janela, text="História dos Sistemas Operacionais",
    border_width=0,
    border_color="black",
    fg_color = "#DCDAD9",
    text_color="black",
    hover=True,
    hover_color="#BFBFBF",
    corner_radius=0,
    command=historia
    ).place(x=10, y=50)
btn_2 = ctk.CTkButton(
    janela, text="Funcionamento do SO",
    border_width=0,
    border_color="black",
    fg_color = "#DCDAD9",
    text_color="black",
    hover=True,
    hover_color="#BFBFBF",
    corner_radius=0,
    command=funcionamento
    ).place(x=10, y=130)
btn_3 = ctk.CTkButton(
    janela, text="Hardware e Software",
    border_width=0,
    border_color="black",
    fg_color = "#DCDAD9",
    text_color="black",
    hover=True,
    hover_color="#BFBFBF",
    corner_radius=0,
    command=hardware
    ).place(x=10, y=90)

label = ctk.CTkLabel(master=janela, text="Wikipedia", fg_color="#DCDAD9")
label.place(x=640, y=3)
assuntos = ctk.CTkLabel(master=janela, text="Assuntos", fg_color="#DCDAD9")
assuntos.place(x=100, y=3)

textbox = ctk.CTkTextbox(janela, width=800, height=600)
textbox.place(x=300, y=50)

janela.mainloop() #Iniciando a janela