class Material:
    _Eg = 0
    _Ev = 0
    _me = 0
    _mhh = 0
    _mlh = 0
        
    def __init__(self):
        pass
    
    def __del__(self):
        del self._Eg
        del self._Ev
        del self._me
        del self._mhh
        del self._mlh
        
    def GetEg(self):
        return self._Eg
    
    def GetEv(self):
        return self._Ev
    
    def Getme(self):
        return self._me
    
    def Getmhh(self):
        return self._mhh
    
    def Getmlh(self):
        return self._mlh

        
class AlGaAs(Material):
    
    __AlAs_Eg = 3.003
    __AlAs_Ev = -1.33
    __AlAs_me = 0.124
    __AlAs_mhh = 0.51
    __AlAs_mlh = 0.18

    __GaAs_Eg = 1.422
    __GaAs_Ev = -0.8
    __GaAs_me = 0.067
    __GaAs_mhh = 0.327
    __GaAs_mlh = 0.18
        
    def __init__(self, x):
        self.__x = x
        self.__p = -0.127 + 1.31 * self.__x
        
        self._Eg = self.__AlAs_Eg * self.__x + (1 - self.__x) * self.__GaAs_Eg - self.__x * (1 - self.__x) * self.__p
        self._Ev = self.__AlAs_Ev * self.__x + (1 - self.__x) * self.__GaAs_Ev
        self._me = self.__AlAs_me * self.__x + (1 - self.__x) * self.__GaAs_me
        self._mhh = self.__AlAs_mhh * self.__x + (1 - self.__x) * self.__GaAs_mhh
        self._mlh = self.__AlAs_mlh * self.__x + (1 - self.__x) * self.__GaAs_mlh
        
def get_mat(nazwa, x):
    if 'AlGaAs' in nazwa:
        material = AlGaAs(x)
    elif 'GaAs' in nazwa:
        material = AlGaAs(0)
    elif 'AlAs' in nazwa:
        material = AlGaAs(1)
    return material