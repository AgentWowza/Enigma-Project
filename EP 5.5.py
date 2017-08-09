#Plugboard (Change if required):
plugs = {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}

#Internal rotor wiring from Enigma I:
r1 = {"A":"E","B":"K","C":"M","D":"F","E":"L","F":"G","G":"D","H":"Q","I":"V","J":"Z","K":"N","L":"T","M":"O","N":"W","O":"Y","P":"H","Q":"X","R":"U","S":"S","T":"P","U":"A","V":"I","W":"B","X":"R","Y":"C","Z":"J"}
r2 = {"A":"A","B":"J","C":"D","D":"K","E":"S","F":"I","G":"R","H":"U","I":"X","J":"B","K":"L","L":"H","M":"W","N":"T","O":"M","P":"C","Q":"Q","R":"G","S":"Z","T":"N","U":"P","V":"Y","W":"F","X":"V","Y":"O","Z":"E"}
r3 = {"A":"B","B":"D","C":"F","D":"H","E":"J","F":"L","G":"C","H":"P","I":"R","J":"T","K":"X","L":"V","M":"Z","N":"N","O":"Y","P":"E","Q":"I","R":"W","S":"G","T":"A","U":"K","V":"M","W":"U","X":"S","Y":"Q","Z":"O"}

#Reflector settings from Enigma I:
ref = {"A":"E","B":"J","C":"M","D":"Z","E":"A","F":"L","G":"Y","H":"X","I":"V","J":"B","K":"W","L":"F","M":"C","N":"R","O":"Q","P":"U","Q":"O","R":"N","S":"T","T":"S","U":"P","V":"I","W":"K","X":"H","Y":"G","Z":"D"}

#Rotor starting positions:
rp1 = {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}
rp2 = {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}
rp3 = {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}

choice = 0
print "Welcome to the Enigma!"
while choice != 3:
    print "1.Begin encryption/decryption."
    print "2.Write current configuration to file."
    print "3.Enigma settings."
    print "4.Exit"
    choice = raw_input("Please enter the number of your choice (1/2/3/4): ")
    if choice == "3":
        print "ENIGMA SETTINGS"
        c = ""
        while c != "3": #Settings
            print "1.Plugboard settings."
            print "2.Rotor position settings."
            print "3.Exit."
            c = raw_input("Please enter the number of your choice (1/2/3) or enter 0 to reset all settings: ")
            if c == "1": #Plugboard reconfig - letter are mapped in couples
                done = ()
                for i in range(65,79,1):
                    if chr(i) in done:
                        continue
                    else:
                        out = raw_input("Please enter an uppercase letter to map to the letter "+str(chr(i))+" on the plugboard, or press enter to continue: ")
                        done = done + (out,)
                        done = done + (chr(i),)
                        plugs[out] = plugs[chr(i)]
                        plugs[chr(i)] = out
                        
                bplugs = plugs
                print "Plugboard reconfiguration complete!"
            elif c == "2": #Rotor repositioning
                start = raw_input("Please enter an uppercase letter to set the initial position of the first rotor: ")
                count = ord(start) - 65
                c = 1
                while c <= count:
                    for k in rp1:
                        if rp1[str(k)] == "Z":
                            rp1[str(k)] = "A"
                        else:
                            rp1[str(k)] = str(chr(ord(rp1[str(k)])+1))
                    c = c + 1
                brp1 = rp1
                start = raw_input("Please enter an uppercase letter to set the initial position of the second rotor: ")
                count = ord(start) - 65
                c = 1
                while c <= count:
                    for m in rp2:
                        if rp2[str(m)] == "Z":
                            rp2[str(m)] = "A"
                        else:
                            rp2[str(m)] = str(chr(ord(rp2[str(m)])+1))
                    c = c + 1
                brp2 = rp2
                start = raw_input("Please enter an uppercase letter to set the initial position of the third rotor: ")
                count = ord(start) - 65
                c = 1
                while c <= count:
                    for n in rp3:
                        if rp3[str(n)] == "Z":
                            rp3[str(n)] = "A"
                        else:
                            rp3[str(n)] = str(chr(ord(rp3[str(n)])+1))
                    c = c + 1
                brp3 = rp3
                print "Rotors reconfiguration complete!"
            elif c == "3":
                break
            elif c == "0":
                plugs = {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}
                rp1 = {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}
                rp2 = {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}
                rp3 = {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}
                print "All settings reset!"
            else:
                print "Invalid choice, please try again."
    elif choice == "4": #Exit condition
        print "Thank your for supporting the Enigma Project!"
        a = raw_input()
        break
    elif choice == "1": #Actual encryption process
        choice = ""
        bplugs = dict(plugs)
        brp1 = dict(rp1)
        brp2 = dict(rp2)
        brp3 = dict(rp3)
        while choice != "E":
            clear = raw_input("Enter a sentence of only uppercase letters to encrypt or decrypt: ")
            char = ()

            #Isolating all characters
            for i in range(0,len(clear),1):
                char = char + (clear[i],)

            #Plugboard encryption
            charp = ()
            for i in range(0,len(char),1):
                if char[i] != " ":
                    key = char[i]
                    out = plugs[key]
                    charp = charp + (out,)
                else:
                    charp = charp + (" ",)
            out = ""
            #Rotor encryption and reflection:
            for i in range(0,len(charp),1):
                if charp[i] != " ":
                    letter = charp[i]
                    letter = rp1[letter]
                    letter = r1[letter] 
                    letter = rp2[letter]
                    letter = r2[letter]
                    letter = rp3[letter]
                    letter = r3[letter]
                    letter = ref[letter]
                    letter = [k for k, v in r3.iteritems() if v == letter] #Going in reverse, therefore need to find key with given value in dictionary
                    letter = str(letter[0])
                    letter = [k for k, v in rp3.iteritems() if v == letter]
                    letter = str(letter[0])
                    letter = [k for k, v in r2.iteritems() if v == letter]
                    letter = str(letter[0])
                    letter = [k for k, v in rp2.iteritems() if v == letter]
                    letter = str(letter[0])
                    letter = [k for k, v in r1.iteritems() if v == letter]
                    letter = str(letter[0])
                    letter = [k for k, v in rp1.iteritems() if v == letter]
                    letter = str(letter[0])
                    out = out + letter
                    for k in rp1: #Rotor 1 rotation
                        if rp1[str(k)] == "Z":
                            rp1[str(k)] = "A"
                        else:
                            rp1[str(k)] = str(chr(ord(rp1[str(k)])+1))
                    if i%26 == 0: #Rotor 2 rotation
                        for m in rp2:
                            if rp2[str(m)] == "Z":
                                rp2[str(m)] = "A"
                            else:
                                rp2[str(m)] = str(chr(ord(rp2[str(m)])+1))
                    if i%676 == 0: #Rotor 3 rotation
                        for n in rp3:
                            if rp3[str(n)] == "Z":
                                rp3[str(n)] = "A"
                            else:
                                rp3[str(n)] = str(chr(ord(rp3[str(n)])+1))
                else:
                    out = out + " "

            print out
            choice = raw_input("Press enter to encrypt/decrypt another message or type E to exit: ")
            if choice == "E":
                plugs = dict(bplugs)
                rp1 = dict(brp1)
                rp2 = dict(brp2)
                rp3 = dict(brp3)
    elif choice == "2": #Writing configuration to txt
        f = open("config.txt","a")
        f.write("Plugboard settings: ")
        for i in plugs:
            f.write("\n"+str(i) + "-->" + plugs[i])
        f.write("\nRotor 1 starting position: " + rp1["A"])
        f.write("\nRotor 2 starting position: " + rp2["A"])
        f.write("\nRotor 3 starting position: " + rp3["A"])
        f.close()
        print "Configuration written to config.txt in program directory!"
    else:
        print "Invalid choice, please try again."
    choice = 0




    
        
    


    
