from src.ro.ubb.calin.ui.console import run_ui
from test.ro.ubb.calin.domain.test_core import *

'''
    Functionalitati:

    (1). Adăugare
    F1.1* adaugă cheltuială pentru un apartament
        T1.1.1* construieste functie test
        T1.1.2*                      core
        T1.1.3*                      ui
        T1.1.4*                      validare
        T1.1.5* leaga toate functiile
    F1.2* modifică cheltuială

    (2). Ștergere
    F2.1* Șterge toate cheltuielile de la un apartament
    F2.2* Șterge cheltuielile de la apartamente consecutive (Ex. se dau două numere de
    apartament 2 și 5 și se sterg toate cheltuielile de la apartamentele 1,2,3,4 și 5)
    F2.3* Șterge cheltuielile de un anumit tip de la toate apartamentele

    (3). Căutări
    F3.1* Tipărește toate apartamentele care au cheltuieli mai mari decăt o sumă dată
    F3.2* Tipărește cheltuielile de un anumit tip de la toate apartamentele
    F3.3* Tipărește toate cheltuielile efectuate înainte de o zi și mai mari decât o sumă (se dă suma
    și ziua)

    (4). Rapoarte
    F4.1* Tipărește suma totală pentru un tip de cheltuială
    F4.2* Tipărește toate apartamentele sortate după un tip de cheltuială
    F4.3* Tipărește totalul de cheluieli pentru un apartament dat

    (5). Filtru
    F5.1* Elimină toate cheltuielile de un anumit tip
    F5.2* Elimină toate cheluielile mai mici decât o sumă dată

    (6). Undo the last operation.
    F6.1* Reface ultima operatie

    Plan Iteratii:
        i1: (1), (2)
        i2: (3)
        i3: (4), (5), (6)

'''


#test all the functions
#:param: [] because test functions will do the heavy work on this list. :)
test_all([])

#invoke the main function from ui
run_ui()
