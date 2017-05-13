##Line storing module

#Idea behind this is to create an effective way of storing things like binary trees


class BranchMap(object):
    def __init__(self,start_pos):
        self.map = {start_pos:[]}
        self.current_coordinate = start_pos
        
    def __iter__(self):
        return self.map.iteritems()

    class BranchError(Exception):
        pass

    def select_coordinate(self,coord):
        if self.map.has_key(coord):
            self.current_coordinate = coord
        else:
            raise self.BranchError("Coordinate '"+str(coord)+"' does not exist in this map.")

    def add_branch(self,coord):
        self.map[self.current_coordinate].append(coord)
        if not self.map.has_key(coord):
            self.map[coord] = []

    def remove_branch(self,coord):
        self.map[self.current_coordinate].remove(coord)

    def remove_coordinate(self,coord):
        self.map.pop(coord)
