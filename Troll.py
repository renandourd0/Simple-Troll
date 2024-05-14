import subprocess

input('vamos jogar ?')
# Lista de programas para abrir no Loop Infinito
while True:
    programas = [
        "notepad.exe",
        "mspaint.exe",
        "calc.exe"
        
    ]

    # Abrir os programas em segundo plano
    processos = [subprocess.Popen(programa) for programa in programas]
