import sqlite3

import Database


def test_conexao_cria_banco_e_tabela(tmp_path, monkeypatch):
    # roda numa pasta temporária, sem tocar no Ark.db real
    monkeypatch.chdir(tmp_path)

    Database.Conexao()

    assert (tmp_path / "Ark.db").exists()
    con = sqlite3.connect(tmp_path / "Ark.db")
    colunas = [c[1] for c in con.execute("PRAGMA table_info(users)")]
    con.close()
    assert colunas == ["id", "website", "email", "password_hash"]


def test_conexao_pode_rodar_duas_vezes(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Database.Conexao()
    Database.Conexao()  # não deve dar erro (CREATE TABLE IF NOT EXISTS)
    assert (tmp_path / "Ark.db").exists()