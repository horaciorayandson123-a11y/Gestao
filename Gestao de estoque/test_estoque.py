import unittest
from estoque import Estoque, Produto


class TestEstoque(unittest.TestCase):
    def setUp(self):
        # Utiliza banco em memória para isolar os testes
        self.estoque = Estoque(db_name=":memory:")

    def test_adicionar_e_buscar_produto(self):
        prod = Produto("100", "Caderno", 10, 15.50)
        sucesso = self.estoque.adicionar_produto(prod)
        
        self.assertTrue(sucesso)
        buscado = self.estoque.buscar_produto("100")
        self.assertIsNotNone(buscado)
        self.assertEqual(buscado.nome, "Caderno")

    def test_adicionar_codigo_duplicado(self):
        prod1 = Produto("100", "Caderno", 10, 15.50)
        prod2 = Produto("100", "Caneta", 5, 2.00)
        
        self.estoque.adicionar_produto(prod1)
        falha = self.estoque.adicionar_produto(prod2)
        
        self.assertFalse(falha)

    def test_atualizar_quantidade(self):
        prod = Produto("200", "Borracha", 50, 1.50)
        self.estoque.adicionar_produto(prod)
        
        atualizado = self.estoque.atualizar_quantidade("200", 35)
        self.assertTrue(atualizado)
        
        buscado = self.estoque.buscar_produto("200")
        self.assertEqual(buscado.quantidade, 35)

    def test_atualizar_quantidade_negativa(self):
        prod = Produto("200", "Borracha", 50, 1.50)
        self.estoque.adicionar_produto(prod)
        
        with self.assertRaises(ValueError):
            self.estoque.atualizar_quantidade("200", -5)

    def test_remover_produto(self):
        prod = Produto("300", "Lápis", 100, 1.00)
        self.estoque.adicionar_produto(prod)
        
        removido = self.estoque.remover_produto("300")
        self.assertTrue(removido)
        
        buscado = self.estoque.buscar_produto("300")
        self.assertNone(buscado)


if __name__ == "__main__":
    unittest.main()