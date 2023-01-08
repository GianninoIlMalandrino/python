prenotazioni = []
nomi = []
num_tel = []
ora = []
giorno = []
n_clienti = []
n_fumatori = []
cameriere_scelto = []
camerieri = ["Marco", "Luciano", "Alessio"]
menu = ["Tagliere di salumi e formaggi - 10€", "Tagliatelle al ragù - 15€", "Fritto misto - 15€", "Tiramisù - 12€"]
spese = 0

opzione = 0
while (opzione != 4):
    print("1) effettua prenotazione")
    print("2) cancella prenotazione")
    print("3) INVIA")
    opzione = int(input())

    if opzione == 1:
        print("Inserisci il nome della prenotazione:")
        nome = input()
        nomi.append(nome)

        print("Inserisci numero di telefono:")
        num_telefono = int(input())
        num_tel.append(num_telefono)

        print("Inserisci l'ora:")
        orario = input()
        ora.append(orario)

        print("Inserisci la data: (gg/mm/aaaa)")
        data = input()
        giorno.append(data)

        print("Inserisci il numero di persone:")
        persone = int(input())
        n_clienti.append(persone)

        print("Inserisci il numero di fumatori:")
        fumatori = int(input())
        n_fumatori.append(fumatori)

        print("Selezionare cameriere: 1)MARCO 2)LUCIANO 3) ALESSIO")
        scelta = int(input())
        if scelta == 1:
            cameriere_scelto.append("Marco")
            
        if scelta == 2:
            cameriere_scelto.append("Luciano")
            
        if scelta == 3:
            cameriere_scelto.append("Alessio")

        print("Seleziona le portate:")
        s = 0
        while s != 5:
            print("1) Tagliere di salumi e formaggi - 10€")
            print("2) Tagliatelle al ragù - 15€")
            print("3) Fritto misto - 15€")
            print("4) Tiramisù - 12€")
            print("5) INVIA LA TUA SCELTA")
            s = int(input())
            if s == 1:
                spese += 10
            if s == 2:
                spese += 15
            if s == 3:
                spese += 15
            if s == 4:
                spese += 12
            if s == 5:
                print("Prenotazione Inviata con SUCCESSO!")

        
            prenotazioni.append(nomi)
            prenotazioni.append(num_tel)
            prenotazioni.append(ora)
            prenotazioni.append(giorno)
            prenotazioni.append(n_clienti)
            prenotazioni.append(n_fumatori)
            prenotazioni.append(cameriere_scelto)
            prenotazioni.append(spese)
           
            
        
    if opzione == 2:
        print("Inserisci il numero della prenotazione da cancellare")
        n_cancellare = int(input())

        print("prenotazione n°{n_cancellare} cancellata!")
        '''
        if len(prenotazioni) >= n_cancellare:
            del prenotazioni[n_cancellare]
        else:
            print("Non c'è nessuna prenotazione a questo nome!")
        '''
        
    if opzione == 3:
        print("PRENOTAZIONI CONFERMATE!")
        exit()
        

    
