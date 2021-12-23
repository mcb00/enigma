# Reflector Wiring and Notches
REFLECTOR_SPECS = {
    'B':  "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    'C':  "FVPJIAOYEDRZXWGCTKUQSBNMHL"
}

class Reflector(object):
    '''Reflector'''
    
    def __init__(self, reflector_type):
        self.wiring = self.__char_wiring_to_int_wiring(REFLECTOR_SPECS[reflector_type])

    def __char_wiring_to_int_wiring(self, char_wiring):
        return [self.__char_to_int(c) for c in char_wiring]

    def __char_to_int(self, c):
        return ord(c) - ord('A')

    def encipher(self, input):
        return self.wiring[input]

ref = Reflector(reflector_type='B')
ref.encipher(0)
ref.encipher(25)