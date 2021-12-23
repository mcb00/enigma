class Plugboard(object):
    '''Plugboard component for Enigma Machine'''

    def __init__(self, connections):
        self.wiring = self.__char_connections_to_int_wiring(connections)

    def __char_connections_to_int_wiring(self, connections):
        pairs = [(ord(chars[0]) - ord('A'), ord(chars[1]) - ord('A')) for chars in connections.split()]
        wiring = list(range(26))
        for a, b in pairs:
            wiring[a] = b
            wiring[b] = a 
        return wiring
    
    def encipher(self, input):
        return self.wiring[input]

p = Plugboard(connections='AB XY')
p.wiring 
p.encipher(0)
p.encipher(24)

p = Plugboard(connections='')
p.wiring 
p.encipher(0)
p.encipher(24)