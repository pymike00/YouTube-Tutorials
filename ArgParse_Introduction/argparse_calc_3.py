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
                    help="Tipo di Operazione", 
                    choices = ["add", "sot", "mol", "div"])
parser.add_argument("-v", "--verbose", 
                    help="Restituisce output verboso.", 
                    type=int, 
                    choices=[1,2])


args = parser.parse_args()


if __name__ == "__main__":
    risultato = calcolatrice(args.n1, args.n2, args.operazione)
    if args.verbose == 1:
        print(f"Il risultato dell'operazione '{args.operazione}' è: {risultato}")
    elif args.verbose == 2:
        print("Benvenuti al programma Calcolatrice!")
        print(f"Il risultato dell'operazione '{args.operazione}' tra '{args.n1}' e '{args.n2}' è: {risultato}")
    else:
        print(f"Il risultato dell'operazione è: {risultato}")
