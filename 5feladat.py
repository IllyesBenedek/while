def paros_szam_bekero():
    # ez a fügvény folyamatosan kér be egy számot a felhasználótól, amíg
    # az páros számot nem ad meg.
  
    print("páros szám bekérése")
    while True:
        try:
            szam = int(input("Kérem, adjon meg egy páros számot: "))
           
            if szam % 2 == 0:
                print(f"Köszönöm! A megadott szám ({szam}) páros.")
                print("A program sikeresen befejeződött.")
                break
            else:
                print(f"A megadott szám ({szam}) páratlan. Kérem, próbálja újra!")
        except ValueError:
            print("Hiba: Nem számot adott meg! Kérem, próbálja újra!")      
paros_szam_bekero()