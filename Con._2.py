def empty():
    return Nas_cen(15,20,1000,9.81,0.7,2)

def Nas_cen(V,t,p,g,n,z):
    def Nas_r():
        return V/t, "м3/с"
    def Nas_m():
        return p*g*V/t*n, "Вт"
    return Nas_r, Nas_m

Nas_r, Nas_m = empty()
print("\nПарам. центроб. насоса:")
print("\nРасход:", Nas_r())
print("Мощность:", Nas_m(), "\n")