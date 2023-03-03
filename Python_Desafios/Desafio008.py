# Crie um programa que leia em metros e converta em centimetros e milimetros
medida = float(input('Uma distância em metros: ')) # 4 -metro na ordem do maior para o menor
cm = medida * 100     # 6 -centimetro
mm = medida * 1000    # 7 -milimetro
dm = medida * 10      # 5 -decimetro
dam = medida / 10     # 3 -decametro
hm = medida / 100     # 2 -hectometro
km = medida / 1000    # 1 -quilometro
print('A medida de {}m corresponde a\n{:.4f}km\n{:.4f}hm\n{:.4f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
