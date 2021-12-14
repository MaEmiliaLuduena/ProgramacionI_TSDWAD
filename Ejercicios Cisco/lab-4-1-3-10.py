milla = 1609.344 #metros
galon = 3.785411784 #litros

def l100kmtompg(litros):
    galones = litros / galon
    millas = 100 * 1000 / milla
    return millas / galones

def mpgtol100km(millas):
    km100 = millas * milla / 1000 / 100
    litros = galon
    return litros / km100

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))