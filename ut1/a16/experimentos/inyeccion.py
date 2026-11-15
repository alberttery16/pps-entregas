import os
import subprocess
entrada = "hola; echo ORDEN_INYECTADA"
print("INSEGURO: texto concatenado (2 órdenes echo)", flush=True)
os.system("echo " + entrada)
print("SEGURO: argumento separado (1 orden echo)", flush=True)
subprocess.run(["echo", entrada], check=True)
