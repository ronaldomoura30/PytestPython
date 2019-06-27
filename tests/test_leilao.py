from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario("Gui", 500.0)
        self.lance_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao("Celular")

    def test_nao_deve_permitir_propor_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            yuri = Usuario("Yuri", 500.0)
            lance_yuri = Lance(yuri, 100.0)

            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_yuri)

    def test_deve_retornar_menor_valor_de_dois_lance_em_ordem_crescente(self):
        yuri = Usuario("Yuri", 500.0)

        lance_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_yuri)
        self.leilao.propoe(self.lance_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_maior_valor_menor_valor_quando_leilao_tiver_um_unico_lance(self):
        self.leilao.propoe(self.lance_gui)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_maior_valor_menor_valor_quando_leilao_tiver_tres_lances(self):
        yuri = Usuario("Yuri", 500.0)
        lance_yuri = Lance(yuri, 100.0)

        vini = Usuario("Vini", 500.0)
        lance_vini = Lance(vini, 200.0)

        self.leilao.propoe(lance_yuri)
        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_caso_nao_exista_lance(self):
        self.leilao.propoe(self.lance_gui)

        qtd_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(1, qtd_lances_recebidos)

    def test_deve_permitir_propor_lance_caso_ultimo_usuario_seja_diferente_usuario_ultimo_lance(self):
        yuri = Usuario("Yuri", 500.0)
        lance_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_yuri)
        self.leilao.propoe(self.lance_gui)

        qtd_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, qtd_lances_recebidos)

    def test_nao_deve_permitir_propor_lances_caso_usuario_seja_igual_ao_usuario_ultimo_lance(self):
        lance_qui_200 = Lance(self.gui, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_qui_200)
