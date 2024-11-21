def letter_diversity_score(word):
    # Calculate the score based on the number of unique letters
    return len(set(word))

with open("Wordlesolver/Fivelength.txt", "r") as file:
    möjligaord = [ord.strip() for ord in file.readlines()]

print("Hej mitt namn är Wordbot och jag är här för att hjälpa dig hitta dagens ord på Wordle så snabbt som möjligt.")
print("Mitt tips är att börja med att gissa 'adieu' då det innehåller många vokaler.")
print("Hur använder man mig då?")
print("Jo, om bokstaven är rätt och på rätt plats använder du G, är bokstaven rätt men på fel plats använder du Y och är den helt fel använder du X.")
print("Du svarar på denna form: ORD G/Y/R för varje bokstav, t.ex. rätt ord är SENAP och du har gissat MENAT, så skriver du: MENAT XGGGX")
while True:
    gissat_ord = input("Vad gissade du och hur blev resultatet? ")
    gissat_ord = gissat_ord.split(" ")
    Result = gissat_ord[1]
    gissat_ord = gissat_ord[0]
    print(gissat_ord)

    # Remove words based on the user's guess and result
    for i in range(len(Result)):
        if Result[i] == "X":
            # Remove words containing the incorrect letter
            bokstav = gissat_ord[i]
            möjligaord = [ord for ord in möjligaord if bokstav not in ord]
        elif Result[i] == "G":
            # Keep only words where the letter is in the correct position
            bokstav = gissat_ord[i]
            möjligaord = [ord for ord in möjligaord if len(ord) > i and ord[i] == bokstav]
        elif Result[i] == "Y":
            # Keep only words where the letter is in the word but not in the correct position
            bokstav = gissat_ord[i]
            möjligaord = [ord for ord in möjligaord if bokstav in ord and (len(ord) <= i or ord[i] != bokstav)]

    # Sort the remaining possible words based on letter diversity score
    möjligaord.sort(key=letter_diversity_score, reverse=True)

    # Display remaining possible words
    if len(möjligaord) == 1:
        print("Rätt ord är", möjligaord[0])
        break
    elif len(möjligaord) > 5:
        print("Det finns", len(möjligaord), "Möjliga ord")
        print("Jag hade gissat på ", möjligaord[0], möjligaord[1], möjligaord[2], möjligaord[3])
    elif len(möjligaord) < 5:
        print("Det finns", len(möjligaord), "Möjliga ord")
        print("Jag hade gissat på ", möjligaord[0], möjligaord[1])
