from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


gui = Usuario("Gui")
yuri = Usuario("Yuri")

lanche_yuri = Lance(yuri, 100.0)
lanche_gui = Lance(gui, 150.0)

leilao = Leilao("Celular")

leilao.lances.append(lanche_yuri)
leilao.lances.append(lanche_gui)

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de: {avaliador.menor_lance} e o maior lance de {avaliador.maior_lance}')

for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} deu um lance de: {lance.valor}")