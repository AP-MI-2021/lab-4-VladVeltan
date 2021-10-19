def data_introduction():
    """
    citeste o lista de stringuri
    :return: returneaza lista de stringuri citita
    """
    lst = []
    givenstring = input("Introduceti lista de numebere insiruite prin virgula: ")
    string = givenstring.split(",")
    for x in string:
        lst.append((x))
    return lst


def gasit_in_lista(lst, listacitita):
    """
    verifica daca listacitita se afla in lst
    :param lst: lista de stringuri initiala
    :param listacitita: lista care se citeste
    :return: DA daca listacitata in lst si NU in caz contrar
    """
    if listacitita in lst:
        return "DA"
    else:
        return "NU"


def afisare_palindrom(lst):
    """
    pune in rezultat o lista stringurile in care se afla acele stringuri din lst care sunt palindroame
    :param lst: lista de stringuri
    :return: returneaza o lista de stringuri noua in care se afla acele stringuri din lst care sunt palindroame
    """
    rezultat = []
    for x in lst:
        if x == x[::-1]:
            rezultat.append(x)
    return rezultat


def test_afisare_palindrom():
    assert afisare_palindrom(['ada', 'abc', 'cmtc', 'drd', 'aaa']) == ['ada', 'drd', 'aaa']


def afisare_sir_care_se_repeta(lst):
    """
    pune in rezultat stringurile care se repeta sau afiseaza UNIC in caz ca nu se repeta niciun string
    :param lst: lista de stringuri
    :return: UNIC in cazul in care lst nu contine stringuri care se repeta
    sau o lista noua care contine stringuri care se repeta
    """
    rezultat = []
    for i in range(len(lst) - 1):
        ajutor = lst.count(lst[i])
        if ajutor >= 2:
            rezultat.append(lst[i])
    for i in range(len(rezultat)-1):
        ajutor=rezultat.count(rezultat[i])
        if ajutor >=2:
            rezultat.remove(rezultat[i])
    if rezultat == []:
        return "UNIC"
    return rezultat

def test_afisare_sir_care_se_repeta():
    assert afisare_sir_care_se_repeta(['aaa', 'bbb', 'cmtc', 'drd', 'aaa']) == ["aaa"]
def test_gasit_in_lista():
    assert gasit_in_lista(['aaa', 'bbb', 'cmtc', 'drd'],'aaa') == "DA"

def frecventa_caracterului_maxim(lst):
    """
    calculeaza frecventa unui caracter si inlocuieste caracterul cu frecventa maxima in stringurile in care apare
    :param lst: lista de stringuri
    :return: Afișați lista obținută prin înlocuirea șirurilor care conțin caracterul care apare de cele mai
multe ori în toată lista cu numărul de apariții ale acestui caracter.
    """
    rezultat= []
    all_freq = {}
    from collections import Counter
    for x in lst:
        res = Counter(x)
        print(str(res))


def main():
    test_gasit_in_lista()
    test_afisare_palindrom()
    test_afisare_sir_care_se_repeta()
    lst = []
    while True:
        print("1.Citirea datelor")
        print("2.Verficare lista citita de la tastatura se afla in lista de stringuri")
        print("3.Verifica daca sirul este unic sau nu ")
        print("4.Verficare daca stringurile din lista sunt palindroame ")
        print("5.Afișați lista obținută prin înlocuirea șirurilor care conțin caracterul cu cea mai mare frecventa")
        print("a.Afisare")
        print("x.Iesire")
        option = input("Alegeti optiunea dorita: ")
        if option == '1':
            lst = data_introduction()
        elif option == 'a':
            print(lst)
        elif option == '2':
            listacitita = input("Introduceti lista care doriti sa o cititi: ")
            print(gasit_in_lista(lst, listacitita))
        elif option == '3':
            print(afisare_sir_care_se_repeta(lst))
        elif option == '4':
            print(afisare_palindrom(lst))
        elif option =='5':
            frecventa_caracterului_maxim(lst)
        elif option == 'x':
            break
        else:
            print("Optiune gresita! Reincercati: ")


main()
