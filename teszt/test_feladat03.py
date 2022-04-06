from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestJelesDiákok(TestCase):
    def test_diakok_vannak_diakok(self):
        adat = "Kis János+15,5;Nagy Éva+14,8;Szabó Éva+21.4;Péter Imre+20,4;Kis Gergő+17,8;Magony Nóra+19,2;Szántó Regő+14,8"
        aktualis = feladatok.fizetendo_osszeg(adat)
        import math
        elvart = math.fabs(aktualis-123.9)
        print(elvart)
        eredmeny=elvart<0.001
        self.assertTrue(eredmeny, "Rosszul határozta meg a diákoknak fizetendő teljes összeget.")

    def test_diakok_nincsenek_diakok(self):
        adat = ""
        aktualis = feladatok.fizetendo_osszeg(adat)
        import math
        elvart = math.fabs(aktualis-0)
        print(elvart)
        eredmeny=elvart<0.001
        self.assertTrue(eredmeny, "Rosszul határozta meg a diákoknak fizetendő teljes összeget.")