CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS adm_campanha (
cod_adm INTEGER PRIMARY KEY FOREIGN KEY NOT NULL,
cod_campanha INTEGER PRIMARY KEY FOREIGN KEY NOT NULL,
papel TEXT NOT NULL
)
"""

INSERIR = """
INSERT INTO adm_campanha (cod_adm, cod_campanha, papel) 
VALUES (?, ?, ?)
"""

OBTER_TODOS = """
SELECT 
cod_adm, cod_campanha, papel
FROM adm_campanha
""" 