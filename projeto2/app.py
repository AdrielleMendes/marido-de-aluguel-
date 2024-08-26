import sqlite3

# conectando...
conn = sqlite3.connect('clientes.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes  (
        id INTEGER NOT NULL,
        nome VARCHAR NOT NULL,
        idade INTEGER,
        cpf  VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        senha    VARCHAR(11) NOT NULL,   
        fone VARCHAR(11)NOT NULL,  
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        PRIMARY KEY (id));
""")
            
cursor.execute("""
        CREATE TABLE IF NOT EXISTS profissionais (
        id INTEGER NOT NULL,
        nome VARCHAR NOT NULL,
        idade INTEGER,
        cpf  VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        senha    VARCHAR(11) NOT NULL,   
        fone VARCHAR(11)NOT NULL,  
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        classificação VARCHER NOT NULL,
        profissão VARCHAR NOT NULL,
        PRIMARY KEY (id));

""")

print('Tabela de clientes e profissionais criada com sucesso.')
# desconectando...
conn.close()
