#das ist planA
spiel = True
spieler = 1
drehen = False
buchstaben = [["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"]]
blau = '\x1b[34m'           #'\033[34m'
grün = '\x1b[32m'
gelb = '\x1b[93m'
rot = '\x1b[31m'
hgrau = '\033[47m'
hschwarz = '\033[40m'

def aufstellung():
    spielbrett = [[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        if i == 8:
            spielbrett[i] = [[rot+" A"],[rot+" B"],[rot+" C"],[rot+" D"],[rot+" E"],[rot+" F"],[rot+" G"],[rot+" H"], [rot+" /"]]
        else:
            spielbrett[i] = [[gelb+" X"],[gelb+" X"],[gelb+" X"],[gelb+" X"],[gelb+" X"],[gelb+" X"],[gelb+" X"],[gelb+" X"],[rot+" "+str(i+1)]]

    spielbrett[0][0] = [blau+" T"]
    spielbrett[0][1] = [blau+" R"]
    spielbrett[0][2] = [blau+" L"]
    spielbrett[0][3] = [blau+" D"]
    spielbrett[0][4] = [blau+" K"]
    spielbrett[0][5] = [blau+" L"]
    spielbrett[0][6] = [blau+" R"]
    spielbrett[0][7] = [blau+" T"]

    spielbrett[7][0] = [grün+" T"]
    spielbrett[7][1] = [grün+" R"]
    spielbrett[7][2] = [grün+" L"]
    spielbrett[7][3] = [grün+" D"]
    spielbrett[7][4] = [grün+" K"]
    spielbrett[7][5] = [grün+" L"]
    spielbrett[7][6] = [grün+" R"]
    spielbrett[7][7] = [grün+" T"]
    for j in range(8):
        spielbrett[1][j] = [blau+" B"]
    for j in range(8):
        spielbrett[6][j] = [grün+" B"]

    return spielbrett


def ausgabe(spielbrett, drehen):
    if drehen == False:
        for i in range(7,-1,-1):
            print(hgrau + spielbrett[i][0][0]+spielbrett[i][1][0]+spielbrett[i][2][0]+spielbrett[i][3][0]+spielbrett[i][4][0]+spielbrett[i][5][0]+spielbrett[i][6][0]+spielbrett[i][7][0]+" "+hschwarz+spielbrett[i][8][0], "\033[0m")
        print(hschwarz + spielbrett[8][0][0]+spielbrett[8][1][0]+spielbrett[8][2][0]+spielbrett[8][3][0]+spielbrett[8][4][0]+spielbrett[8][5][0]+spielbrett[8][6][0]+spielbrett[8][7][0]+" "+spielbrett[8][8][0], "\033[0m")
    else:
        print(hschwarz + spielbrett[8][0][0]+spielbrett[8][1][0]+spielbrett[8][2][0]+spielbrett[8][3][0]+spielbrett[8][4][0]+spielbrett[8][5][0]+spielbrett[8][6][0]+spielbrett[8][7][0]+" "+spielbrett[8][8][0], "\033[0m")
        for i in range(8):
            print(hgrau + spielbrett[i][0][0]+spielbrett[i][1][0]+spielbrett[i][2][0]+spielbrett[i][3][0]+spielbrett[i][4][0]+spielbrett[i][5][0]+spielbrett[i][6][0]+spielbrett[i][7][0]+" "+hschwarz+spielbrett[i][8][0], "\033[0m")


def zugdecodieren(spielbrett, zug):
    print("decodieren...")
    if len(zug)==4:
        zug = list(zug)
        zug[1]=str(int(zug[1])-1)
        zug[3]=str(int(zug[3])-1)
        for i in range(8):                              #von 0-7 (8 einträge)
            if zug[0]==buchstaben[i][0]:
                zug[0] = i
            if zug[2]==buchstaben[i][0]:
                zug[2] = i

    # print(spielbrett[int(zug[1])][int(zug[0])])                                                 #Wichtig beim aufrufen des spielbretts erst die y-achse dann die x-achse sprich spielbrett[y][x]
    # print(zug)
    figur = [spielbrett[int(zug[1])][int(zug[0])], int(zug[1]), int(zug[0])]  
    ziel = [spielbrett[int(zug[3])][int(zug[2])], int(zug[3]), int(zug[2])]                       
    print(figur, ziel)                                                                                      
    return figur, ziel

def zugprüfen(figur, ziel, spieler):
    print("prüfung...")

    def nurhorizontal(schritte):
        for h in range(schritte):
            if (ziel[2]+h == figur[2] or ziel[2]-h == figur[2]) and ziel[1] == figur[1]:
                return True
        return False


    def nurvertikal(schritte):
        for v in range(schritte):
            if (ziel[1]+v == figur[1] or ziel[1]-v == figur[1]) and ziel[2] == figur[2]:
                return True
        return False


    def quer(schritte):
        for q in range(schritte):
            if (ziel[1]+q == figur[1] and ziel[2]+q == figur[2]) or (ziel[1]-q == figur[1] and ziel[2]-q == figur[2]) or (ziel[1]+q == figur[1] and ziel[2]-q == figur[2]) or (ziel[1]-q == figur[1] and ziel[2]+q == figur[2]):
                return True
        return False

    def reiter():
        pass

    if spieler == 1:                                    #spieler 2 muss noch eingefügt werden
        if figur[0][0].split(" ")[0] == grün:           # die eingegebene figur ist grün also dem spieler 1 entsprechend
            if ziel[0][0].split(" ")[0] == gelb or ziel[0][0].split(" ")[0] == blau:
                if figur[0][0].split(" ")[1] == "B":                                                                                                        #es handelt sich um einen bauern
                    if ziel[1]+1 == figur[1] and ziel[2] == figur[2] and ziel[0][0].split(" ")[0] == gelb:                                                      #normaler zug
                        valid_zug = True
                    elif ziel[1]+1 == figur[1] and (ziel[2]+1 == figur[2] or ziel[2]-1 == figur[2]) and ziel[0][0].split(" ")[0] == blau:                       #bauern schlag züge
                        valid_zug = True
                    elif ziel[1]+2 == figur[1] and ziel[2] == figur[2] and figur[1] == 6:                                                                       #bauern start zug (2)
                        valid_zug = True
                    else:
                        valid_zug = False
                elif figur[0][0].split(" ")[1] == "D":                                                                                                      #es handelt sich um eine dame       
                    if nurhorizontal(9) or nurvertikal(9) or quer(9):                          
                        valid_zug = True
                    else:
                        valid_zug = False
                elif figur[0][0].split(" ")[1] == "L":
                    if quer(9):
                        valid_zug = True
                    else:
                        valid_zug = False
                elif figur[0][0].split(" ")[1] == "T":
                    if nurvertikal(9) or nurhorizontal(9):
                        valid_zug = True
                    else:
                        valid_zug = False
                elif figur[0][0].split(" ")[1] == "K":
                    if nurvertikal(2) or nurhorizontal(2) or quer(2):
                        valid_zug = True
                    else:
                        valid_zug = False
                elif figur[0][0].split(" ")[1] == "R":
                    if reiter():
                        valid_zug = True
                    else:
                        valid_zug = False
                else:
                    valid_zug = False
            else:
                valid_zug = False
        else:
            valid_zug = False


    elif spieler == 2:                                    #spieler 2 muss noch eingefügt werden
        if figur[0][0].split(" ")[0] == blau:           # die eingegebene figur ist grün also dem spieler 1 entsprechend
            if ziel[0][0].split(" ")[0] == gelb or ziel[0][0].split(" ")[0] == grün:
                valid_zug = True
            else:
                valid_zug = False
        else:
            valid_zug = False
    return valid_zug


def figursetzen(spielbrett, figur, ziel):
    print("hier")
    print(figur)
    print(spielbrett[4][4])
    spielbrett[ziel[1]][ziel[2]] = figur[0]
    spielbrett[figur[1]][figur[2]] = [gelb+" X"]
    print(spielbrett[ziel[1]][ziel[2]])
    return spielbrett


spielbrett = aufstellung()

while spiel:
    if spieler == 1:
        ausgabe(spielbrett, drehen)
        zug = input("spieler1 (bsp. e7e5): ")
        figur, ziel = zugdecodieren(spielbrett, zug)
        valid_zug = zugprüfen(figur, ziel, spieler)
        if valid_zug == True:
            spielbrett = figursetzen(spielbrett, figur, ziel)
            # spieler = 2
        else:
            print("zug ist nicht möglich")
    if spieler == 2:
        ausgabe(spielbrett, drehen)
        zug = input("spieler2 (bsp. e2e4): ")
        figur, ziel = zugdecodieren(spielbrett, zug)
        valid_zug = zugprüfen(spielbrett, figur, ziel, spieler)
        if valid_zug == True:
            spielbrett = figursetzen(spielbrett, figur, ziel)
            # spieler = 1
        else:
            print("zug ist nicht möglich")