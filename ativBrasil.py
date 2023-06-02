from conexao import conectar

def listar(conn, cursor):
    
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tribosBrasil")
    
    resultados = cursor.fetchall()
    
    for resultado in resultados:
        print(resultado)
        
    cursor.close()
    conn.close()
    
    
def inserir(id, nome, habitantes, renda, escolaridade, assalariado):
    
    conn = conectar()
    cursor = conn.cursor()
    
    sql = "INSERT INTO tribosBrasil (id, nome, habitantes, renda, escolaridade, assalariado) VALUES (%s, %s, %s, %s, %s)"
    val = (id, nome, habitantes, renda, escolaridade, assalariado)
    cursor.execute(sql, val)
    
    conn.commit()
    
    print("Registro inserido com sucesso.")
    
    cursor.close()
    conn.close()
    
    
    
def atualizar(id, novoNome,novoHabitantes, novaRenda, novoEscolaridade, novoAssalariado):
    
    conn = conectar()
    cursor = conn.cursor()
    
    sql = "UPDATE tribosBrasil SET nome = %s, habitantes = %s, renda = %s, escolaridade = %s, assalariado = %s  WHERE id = %s"
    val = ( novoNome, novoHabitantes, novaRenda, novoEscolaridade, novoAssalariado)
    cursor.execute(sql, val)
    
    conn.commit()
    
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado")
    else:
        print("Atualizado com sucesso")
        
        
    cursor.close()
    conn.close()
    
    
    
    
def deletar(id):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para deletar o registro
    sql = "DELETE FROM tribosBrasil WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi deletado
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()
    
    
    

conn = conectar()

cursor = conn.cursor()
while True:
    print("O que deseja fazer?")
    print("1 - Listar tribos")
    print("2 - Inserir tribos")
    print("3 - Atualizar tribos")
    print("4 - Deletar tribos")
    print("0 - Sair")
    
    op = int(input("Digite o número da opção desejada: "))
    
    
    if op == 1:
        listar(conn, cursor)
        
    
    elif op == 2:  
        id = int(input("Digite o código da nova tribo: "))
        nome = input("Digite o nome da tribo:")
        habitantes = input("Digite o número de habitantes: ")
        renda = int(input("Digite a renda média mensal: "))
        escolaridade = input("Digite qual o nivel de escolaridade: ")
        assalariado = input("Digite se são assalariados ou não: ")
        inserir(id, nome, habitantes, renda, escolaridade, assalariado)
        
    elif op == 3:  
        id = int(input("Digite o código da tribo que deseja atualizar: "))
        novoNome = input("Digite o novo nome da tribo:")
        novoHabitantes = input("Digite a nova quantidade de habitantes: ")
        novaRenda = int(input("Digite a nova renda: "))
        novoEscolaridade = input("Digite o novo nível de escolaridade ")
        novoAssalariado = input("Atualize o status se for assalariado ou não: ")
        atualizar(id, novoNome novoHabitantes, novaRenda, novoEscolaridade, novoAssalariado)
        
        
    elif op == 4:  
        codigo = int(input("Digite o código da tribo que deseja deletar: "))
        deletar(id)
        
    elif op == 0:
        print("Você escolheu sair")
        break
    
    else: 
        print("Escolha uma opção válida")
        
        
        
    conn.close