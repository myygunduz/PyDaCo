
__all__ = ['pdc', 'pycado']


from typing import overload


class pdc:
    __version__ = '0.1.1'
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

    def __setitem__(self, __name: str, __value: object) -> None: self.__setattr__(__name, __value)

    def __setattr__(self, __name: str, __value: object) -> None:
        
        if isinstance(__value, dict):
            self.__dictionary({__name: __value})
        elif isinstance(__value, list):
            super().__setattr__(__name, self.__list(__value))
        else:
            self.__dict__[__name] = __value
            super().__setattr__(__name, __value)

    def __getitem__(self, __name: str) -> object: return str(self.__dict__[__name])
    
    def __getattr__(self, __name: str) -> object:
        self.__dict__[__name] = pdc()
        return str(self.__dict__[__name])

    def __delitem__(self, __name: str) -> None: self.__dict__.__delitem__(__name)

    def __delattr__(self, __name: str) -> None: self.__dict__.__delitem__(__name)

    def clear(self) -> None:
        self.__dict__.clear()
    
    def add(self, __name: str, __value: object) -> None:
        self.__setattr__(__name, __value)

        
pydaco = pdc()