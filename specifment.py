# ti dice se un numero è pari o dispari
def paridispari():
    # il while True serve a ripetere all'infinito oppure finchè non viene ritornato False
    while True:
        # ti chiede un  numero e lo salva sulla variabile
        inp = input("\n\nInserisci un  numero: ")
        #prova un comando e se non funzione esegue l'altro    
        try:
            numero = int(inp)
        except:
            numero = inp
        # ti dice se è un numero intero
        if (isinstance(numero, int)):
            # trasforma in un numero intero la stringa superiore
            modulo = numero % 2
            # se il modulo, che corrisponde al numero inserito diviso per due, è diverso da zero risponde con la frase presente nelle tonde
            if modulo == 0:
                print("Numero Pari")
            # oppure se il modulo è diverso da zero risponde con la frase nelle tonde
            else:
                print("Numero Dispari")
        else:
            numero = str(inp)
            # se la risposta all'input è "exit" allora esce dal programma 
            if (numero == 'exit'):
                return False 
            else:
                print("Puoi inserire solo numeri o il comando \"exit\" per uscire")

paridispari()