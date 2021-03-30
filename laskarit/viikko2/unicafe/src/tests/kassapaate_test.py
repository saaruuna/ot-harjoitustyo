import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_alkuasetelma_on_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maksu_edullisesti_kateisella_rahamaara_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(vaihtoraha, 260)

    def test_maksu_edullisesti_kateisella_rahamaara_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(vaihtoraha, 200)

    def test_maksu_maukkaasti_kateisella_rahamaara_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(vaihtoraha, 100)

    def test_maksu_maukkaasti_kateisella_rahamaara_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtoraha, 200)

    def test_maksu_edullisesti_kortilla_rahamaara_riittava(self):
        maksukortti = Maksukortti(1000)
        riittavat_rahat = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(riittavat_rahat, True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(str(maksukortti), "saldo: 7.6")

    def test_maksu_edullisesti_kortilla_rahamaara_ei_riittava(self):
        maksukortti = Maksukortti(200)
        riittavat_rahat = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(riittavat_rahat, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(str(maksukortti), "saldo: 2.0")

    def test_maksu_maukkaasti_kortilla_rahamaara_riittava(self):
        maksukortti = Maksukortti(1000)
        riittavat_rahat = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(riittavat_rahat, True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(str(maksukortti), "saldo: 6.0")

    def test_maksu_maukkaasti_kortilla_rahamaara_ei_riittava(self):
        maksukortti = Maksukortti(300)
        riittavat_rahat = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(riittavat_rahat, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(maksukortti), "saldo: 3.0")

    def test_kortin_lataaminen_onnistuu(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 700)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100700)
        self.assertEqual(str(maksukortti), "saldo: 10.0")

    def test_kortin_lataaminen_epaonnistuu(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(maksukortti), "saldo: 3.0")
