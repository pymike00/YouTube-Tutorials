import argparse

def calcolatrice(n1, n2, operazione):
    if operazione == "add":
        return n1 + n2
    elif operazione == "sot":
        return n1 - n2
    elif operazione == "mol":
        return n1 * n2
    elif operazione == "div":
        return n1 / n2

parser = argparse.ArgumentParser(description="Semplice Calcolatrice per addizioni, sottrazioni, moltiplicazioni e divisioni")

parser.add_argument("n1", type=float, help="Primo Numero")
parser.add_argument("n2", type=float, help="Secondo Numero")
parser.add_argument("operazione", 
                    type=str, 
                    help="Operazione consentite: add | sot | mol | div")

args = parser.parse_args()

if __name__ == "__main__":
    risultato = calcolatrice(args.n1, args.n2, args.operazione)
    print(risultato)
