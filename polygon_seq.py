from polygon import Polygon
from numbers import Real
import typing
from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

class Polygons():
    """Generates a sequence of Polygon Objects with given max number of vertices and common \
        circumscribing radius.
        It also implents:
        indexing and slicing within the sequence,
        finding and returning max efficinecy polygon from the sequence.
        
    """

    def __init__(self, m, R):
            if m < 3:
                raise ValueError('m must be greater than 3')
            self._m = m
            self._R = R
            self._polygons = [Polygon(i, R) for i in range(3, m+1)]
            
    def __len__(self):
        return self._m - 2
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __getitem__(self, s):
        return self._polygons[s]
    
    @property
    def max_efficiency_polygon(self):
        # with suppress_stdout():
        sorted_polygons = sorted(self._polygons, 
                                key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]
    
    class PolygonIterator:
        def __init__(self, polygons_obj):
            self._polygons_obj = polygons_obj
            self._idx = 0
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._idx > self._polygon_obj._m:
                raise StopIteration
            else:             
                p = self._polygons_obj[self._idx]
                self._idx += 1
                return p