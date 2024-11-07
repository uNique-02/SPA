class Node:
  
    name = ""
    connected_vertices = []
    
    def __init__(self, name):
        self.name = name
    
    def set_name(self, name):
      self.name = name
      
    def get_name(self):
      return self.name
  
    def set_connected_vertices(self, connected, weight):
      self.connected_vertices = f'{connected}:{weight}'
      
    def get_connected_vertices(self):
      return self.connected_vertices
    
    def append_connected_vertices(self, connected, weight):
      self.connected_vertices.append(f'{connected}:{weight}')