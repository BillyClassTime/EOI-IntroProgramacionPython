ciudad=input('Entre la ciudad a repetir:')
N=input('Entre el numero de veces que desea repetir la ciudad:')
if(N.isdigit()):
    N=int(N)
    print("{}{}".format(ciudad,'\n')*N)
    #print((ciudad+'\n')*N)
else:
    print('Entre un valor numérico valido')
