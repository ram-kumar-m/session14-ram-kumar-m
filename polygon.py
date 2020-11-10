# polygon.py

import math

class Polygon:
    """Simple polygon class for stricly convex polygons
    """
    
    def __init__(self, edge , circumradius):
        if edge < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self.edge = edge
        self.circumradius = circumradius
        
    def __repr__(self):
        return f'Polygon(n={self.edge}, R={self.circumradius})'
        
    @property
    def edge(self):
        return self._edge

    @edge.setter
    def edge(self, edge):
        if edge <3:
            raise ValueError("Number of Edges must be greater than 2")
        else:
            self._edge = edge
            self._interior_angle = None
            self._apothem = None
            self._area = None
            self._perimeter = None
            self._edge_length = None 
    
    @property
    def vertices(self):
        return self.edge
    
    @property
    def count_edges(self):
        return self.edge
    
    @property
    def count_vertices(self):
        return self.edge

    @property
    def circumradius(self):
        return self._circumradius
    
    @circumradius.setter
    def circumradius(self, circumradius):
        if circumradius <=0:
            raise ValueError("Circumradius must be positive")
        else:
            self._circumradius = circumradius
            self._interior_angle = None
            self._apothem = None
            self._area = None
            self._perimeter = None
            self._edge_length = None 

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            print('Calculating Interior angle ...')
            self._interior_angle = (self.edge - 2) * (180/self.edge)
        return self._interior_angle
    
    @property
    def edge_length(self):
        if self._edge_length is None:
            print("Calculating Edge length ...")
            self._edge_length = 2 * self.circumradius * math.sin((math.pi/self.edge))
        return self._edge_length
    
    @property
    def side_length(self):
        return self.edge_length

    
    @property
    def apothem(self):
        if self._apothem is None:
            print("Calculating apothem ...")
            self._apothem = self.circumradius * math.cos(math.pi/self.edge)
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            print("Calculating area ...")
            self._area = (1/2) * self.edge * self.edge_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            print("Calculating circumference ...")
            self._perimeter = self.edge * self.edge_length
        return self._perimeter

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.edge == other.edge 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.edge > other.edge
        else:
            return NotImplemented