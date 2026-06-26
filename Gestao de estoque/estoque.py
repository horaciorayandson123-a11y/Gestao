import sqlite3
from typing import List, Optional


class Produto:
    """Representa um produto do estoque."""
    def __init__(self, codigo: str, nome: str, quantidade: int, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self) -> str:
        return f"Código: {self.codigo} | Nome: {self.nome} | Qtd: {self.quantidade} | Preço: R${self.preco:.2f}"


class Estoque:
    """Gerencia as operações de estoque no banco de dados SQLite."""
    def __init__(self, db_name: str = "database.db"):
        self.db_name = db_name
        self._criar_tabela()

    def _conectar(self):
        return sqlite3.connect(self.db_name)

    def _criar_tabela(self):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    codigo TEXT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    preco REAL NOT NULL
                )
            """)
            conn.commit()

    def adicionar_produto(self, produto: Produto) -> bool:
        """Adiciona um novo produto. Retorna False se o código já existir."""
        try:
            with self._conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO produtos (codigo, nome, quantidade, preco) VALUES (?, ?, ?, ?)",
                    (produto.codigo, produto.nome, produto.quantidade, produto.preco)
                )
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False

    def buscar_produto(self, codigo: str) -> Optional[Produto]:
        """Busca um produto pelo código único."""
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo, nome, quantidade, preco FROM produtos WHERE codigo = ?", (codigo,))
            row = cursor.fetchone()
            if row:
                return Produto(row[0], row[1], row[2], row[3])
            return None

    def atualizar_quantidade(self, codigo: str, nova_quantidade: int) -> bool:
        """Atualiza a quantidade de um produto existente."""
        if nova_quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE produtos SET quantidade = ? WHERE codigo = ?", (nova_quantidade, codigo))
            conn.commit()
            return cursor.rowcount > 0

    def remover_produto(self, codigo: str) -> bool:
        """Remove um produto pelo código."""
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE codigo = ?", (codigo,))
            conn.commit()
            return cursor.rowcount > 0

    def listar_produtos(self) -> List[Produto]:
        """Retorna uma lista com todos os produtos cadastrados."""
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo, nome, quantidade, preco FROM produtos")
            rows = cursor.fetchall()
            return [Produto(row[0], row[1], row[2], row[3]) for row in rows]