import customtkinter

janela = customtkinter.CTk() #Criando a janela

janela._set_appearance_mode("light") #Setando a aparência 
janela.title("Wikipedia") #Setando o titulo da janela
janela.geometry("1280x700") #Setando o tamanho inicial da janela
janela.maxsize(width=1280, height=700) #Setando o máximo que a janela pode expandir
janela.minsize(width=1280, height=700)#Setando o mínimo que a janela pode expandir
janela.resizable(width=False, height=False) #Pode configurar se a altura/largura é reconfiguravel

janela.mainloop() #Iniciando a janela