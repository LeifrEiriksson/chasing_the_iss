from Components import iss
from Components import me

teste = iss.ISS()
teste_1 = me.Where_am_I('João')

print(teste.position())
print(teste.whos_aboard())
print(teste.welcome, teste.iss_time, teste.verify())

print(teste_1.coordinates(), teste_1.current_location_name(), teste_1.nome, teste_1.current_time)