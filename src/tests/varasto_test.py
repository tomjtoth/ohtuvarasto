import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_uusi_varasto_neg_tilavuus_neg_alkusaldo(self):
        v = Varasto(-10, -5)
        self.assertAlmostEqual(v.saldo, 0)

    def test_uusi_varasto_tilavuus_gt_alkusaldo(self):
        v = Varasto(10, 5)
        self.assertAlmostEqual(v.saldo, 5)

    def test_uusi_varasto_alkusaldo_gt_tilavuus(self):
        v = Varasto(10, 15)
        self.assertAlmostEqual(v.saldo, 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_neg_lisays(self):
        self.assertEqual(self.varasto.lisaa_varastoon(-2), None)

    def test_lisays_gt_mahtuisi(self):
        self.varasto.lisaa_varastoon(200)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ota_neg_arvo(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-2), 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_enemman_kuin_voi(self):

        # this is fishy, shouldn't this.setUp() take care of this?!?!
        self.varasto.saldo = 10
        self.assertAlmostEqual(10, self.varasto.ota_varastosta(300))
        self.assertAlmostEqual(0, self.varasto.saldo)

    def test_str(self):
        # this is also fishy...
        self.varasto.saldo = 10
        self.varasto.ota_varastosta(2)
        self.assertEqual(
            str(self.varasto),
            "saldo = 8, vielä tilaa 2"
        )
