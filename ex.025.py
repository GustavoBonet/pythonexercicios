a = str (input('Nome completo:')).strip()
print(' O seu nome tem Silva?','SILVA' in a.upper())
# 1. ele esta perguntando o nome
# 2. se tem silva , pra isso ele coloca tudo em maiusculo, n importa como o cliente escreveu
# 3. isso ajuda a colocar um padrão indifirente do jeito escrito, apenas para reconhecer a palavra no meio do input
