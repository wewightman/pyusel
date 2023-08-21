from abc import ABC, abstractmethod

class DataAxis(dict):
    @classmethod
    @abstractmethod
    def __init__(self):
        raise NotImplementedError
    
    @classmethod
    @abstractmethod
    def geti(self, i:int):
        raise NotImplementedError

class SampledDataAxis(DataAxis):
    def __init__(self, start, delta, N:int):
        dict.__init__(self, start=start, delta=delta, N=N)
    
    def geti(self, i:int):
        if (i < 0) or (i >= self['N']): raise IndexError("i must be between 0 and N-1")
        return self['start'] + i * self['delta']
    
class ArbitraryDataAxis(DataAxis):
    def __init__(self, points):
        dict.__init__(self, points=points, N=len(points))
    
    def geti(self, i:int):
        if (i < 0) or (i >= self['N']): raise ValueError("i must be between 0 and N-1")
        return self['points'][i]
    
class DataAxisSet(dict):
    def __init__(self, **kwargs):
        dict.__init__(self)
        labels = []
        shape = []
        for key, item in kwargs:
            if not issubclass(DataAxis): raise ValueError("All inputs to DataAxisSet must be of type DataAxis")
            if (key in self.keys()): raise KeyError("Each key must be unique")
            self[key] = item
            labels.append(key)
            shape.append(item['N'])

        self.labels = tuple(labels)
        self.shape = tuple(shape)