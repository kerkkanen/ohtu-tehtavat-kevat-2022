import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ei_lisata_tyhjaa_tai_yli_mahtuvuuden(self):
        self.varasto.lisaa_varastoon(-3)
        self.varasto.lisaa_varastoon(12)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)
    
    def test_ei_oteta_tyhjasta_eika_tyhjaa(self):
        self.varasto.lisaa_varastoon(10)
        self.assertEqual(self.varasto.ota_varastosta(12), 10)
        self.assertEqual(self.varasto.ota_varastosta(12), 0)
        self.assertEqual(self.varasto.ota_varastosta(-3), 0)

    def test_ei_luoda_negatiivista(self):
        olematon = Varasto(0, -2)
        self.assertEqual(olematon.paljonko_mahtuu(), 0)

    def test_lisataan_mita_mahtuu(self):
        tila = Varasto(10, 12)
        self.assertEqual(str(tila), "saldo = 10, vielä tilaa 0")
        self.assertEqual(tila.ota_varastosta(11), 10)
        
        
