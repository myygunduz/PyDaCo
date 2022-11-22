
__all__ = ['pdc', 'pycado']


from typing import overload


class pdc:
    __version__ = '0.1.0'
    __name__    = 'PyDaCO'

    @overload
    def __init__(self, data: dict) -> object: ...
    @overload
    def __init__(self, data: list) -> object: ...
    @overload
    def __init__(self) -> object: ...
    def __init__(self, data = None):
    
        if data is None:...
        elif isinstance(data, dict):
            self.__dictionary(data)
        elif isinstance(data, list):
            self.__list(data)
        else:
            raise TypeError("data must be a dict, a list or None", type(data))

    def __repr__(self) -> object:
        return str(self.__dict__.__repr__())

    def __dictionary(self, __data) -> None:
        for key, value in __data.items():
            if isinstance(value, dict):
                self.__setattr__(key, pdc(value))
            elif isinstance(value, list):
                self.__setattr__(key, self.__list(value))
            else:
                self.__setattr__(key, value)
    
    def __list(self, __data) -> list:
        return [pdc(value) if isinstance(value, dict) else value for value in __data]

    def __setattr__(self, __name: str, __value: object) -> None:
        
        if isinstance(__value, dict):
            self.__dictionary({__name: __value})
        elif isinstance(__value, list):
            super().__setattr__(__name, self.__list(__value))
        else:
            self.__dict__[__name] = __value
            super().__setattr__(__name, __value)

    def __getattr__(self, __name: str) -> object:
        self.__dict__[__name] = pdc()
        return str(self.__dict__[__name])
    
    #get data use subscriptable
    def __getitem__(self, __name: str) -> object:
        return str(self.__dict__[__name])

    def clear(self) -> None:
        self.__dict__.clear()
    
    def add(self, __name: str, __value: object) -> None:
        self.__setattr__(__name, __value)

        
pydaco = pdc()

# class pdcStats:
#     """will be implemented in the future"""
#     def __init__(self, data: pdc) -> None:
#         self.data = data
#         self.length = 0
#         self.__len__(self.data)    
                
#     def __repr__(self) -> str:
#         return f"""pdcStats:
#         data: {self.data}
#         length: {self.length}
#         """

#     def __len__(self, data: pdc = None) -> int:
#         if data is None: return self.length

#         for key, value in data.__dict__.items():
#             if isinstance(value, pdc):
#                 print(value)
#                 self.length += 1
#                 self.__len__(value)
#             else:
#                 if(isinstance(value, list)):
#                     print(value)
#                     self.length += len(value)
#                 else:
#                     print(value)
#                     self.length += 1
            
#         return self.length