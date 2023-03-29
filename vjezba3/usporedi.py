import briskula
import igrac
import rezultati


if __name__ == "__main__":
    igrac1 = igrac.Igrac("agent1")
    igrac2 = igrac.Igrac("agent2")

    i = 0
    pobjede = {"igrac1": 0, "igrac2": 0}

    while(i < 5):
        briskula1 = briskula.Briskula(igrac1, igrac2, {})
        briskula1.odigraj_partiju()
        resolve = briskula1.bodovanjeBriskule()
        if(resolve == rezultati.POBJEDA_IGRACA_1):
            pobjede["igrac1"] += 1
        elif(resolve == rezultati.POBJEDA_IGRACA_2):
            pobjede["igrac2"] += 1
        else:
            pobjede["igrac1"] += 0
            pobjede["igrac2"] += 0
        i += 1

    while(i < 10):
        briskula2 = briskula.Briskula(igrac2, igrac1, {})
        briskula2.odigraj_partiju()
        resolve = briskula2.bodovanjeBriskule()
        if(resolve == rezultati.POBJEDA_IGRACA_1):
            pobjede["igrac2"] += 1
        elif(resolve == rezultati.POBJEDA_IGRACA_2):
            pobjede["igrac1"] += 1
        else:
            pobjede["igrac2"] += 0
            pobjede["igrac1"] += 0
        i += 1

    print(pobjede)
