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

    def test_lisaaminen_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(12)

        # saldon pitäisi olla yhtä suuri, kuin tilavuus, eli 10

        self.assertEqual(self.varasto.saldo, 10)

    def test_negatiivisen_maaran_lisaaminen_ei_onnistu(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertEqual(self.varasto.saldo, 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivisen_maaran_ottaminen_ei_onnistu(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_yli_saldon_palauttaa_saldon(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(12)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_yli_saldon_nollaa_saldon(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(12)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_print_self_toimii(self):
        syote = str(self.varasto)
        self.assertEqual(syote, "saldo = 0, vielä tilaa 10")

    def test_konstruktori_negatiivisella_tilavuudella(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_negatiivisella_saldolla(self):
        self.varasto = Varasto(10, -5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_saldo_suurempi_kuin_tilavuus(self):
        self.varasto = Varasto(10, 15)
        self.assertAlmostEqual(self.varasto.saldo, 10)