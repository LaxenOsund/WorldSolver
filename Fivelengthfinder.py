with open("Wordlesolver/filtered_words.txt", "r") as source:
    with open("Wordlesolver/Fivelength.txt", "w") as destination:
        alphabet = ["A","B","C","D","E","F",
                    "G","H","I","J","K","L",
                    "M","N","O","P","Q","R",
                    "S","T","U","V","W","X",
                    "Y","Z"]
        for line in source:
            line_upper = line.upper().strip()
            if len(line_upper) == 5:
                valid = True
                for symbol in line_upper:
                    if symbol not in alphabet:
                        print (symbol)
                        valid = False
                if valid:
                    destination.write(line_upper + "\n")
                    print("found 5 length word " + line_upper)