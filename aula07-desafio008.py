#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS
#E CONVERTA EM KM HM DAM DM CM MM
m = float(input('Digite o valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100 
mm = m*1000
print('O valor digitado é {:.0f}m. \nConvertendo:\n{}km; \n{}hm; \n{}dam; \n{:.0f}dm; \n{:.0f}cm; \n{:.0f}mm;'.format (m,km,hm,dam,dm,cm,mm))
