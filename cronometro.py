import time
import os

class Cronometro:
    def __init__(self, segundos=0, minutos=0, horas=0, regressivo=False):
        self.tempo_total = segundos + (minutos * 60) + (horas * 3600)
        self.regressivo = regressivo
        self.pausado = False

    def formatar_visor(self, segundos_totais):
        h = segundos_totais // 3600
        m = (segundos_totais % 3600) // 60
        s = segundos_totais % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def ler_comando(self):
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit():
                return msvcrt.getch().decode().lower()
        return None

    def rodar(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            status = " [ PAUSADO ]" if self.pausado else ""
            modo = "Contagem Regressiva" if self.regressivo else "Cronômetro"
            
            print(f"--- {modo} ---")
            print(f"Tempo atual: {self.formatar_visor(self.tempo_total)} {status}")
            print("\nComandos: P (pausar) | C (continuar) | Q (sair)")

            tempo_inicial = time.time()
            while time.time() - tempo_inicial < 1:
                comando = self.ler_comando()
                if comando == 'p': self.pausado = True
                elif comando == 'c': self.pausado = False
                elif comando == 'q': return
                time.sleep(0.05)

            if not self.pausado:
                if self.regressivo:
                    if self.tempo_total <= 0:
                        print("\nO tempo acabou!")
                        os.system('pause' if os.name == 'nt' else 'read -p "Aperte Enter..."')
                        return
                    self.tempo_total -= 1
                else:
                    self.tempo_total += 1

def configurar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Como deseja usar o relógio?")
    print("1 - Começar do zero (Progressivo)")
    print("2 - Definir um tempo (Regressivo)")
    
    escolha = input("\nOpção: ")
    
    if escolha == '2':
        h = int(input("Quantas horas? ") or 0)
        m = int(input("Quantos minutos? ") or 0)
        s = int(input("Quantos segundos? ") or 0)
        relogio = Cronometro(s, m, h, regressivo=True)
    else:
        relogio = Cronometro(regressivo=False)

    relogio.rodar()

if __name__ == "__main__":
    try:
        configurar()
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")