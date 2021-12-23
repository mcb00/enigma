
from .rotor import Rotor
from .reflector import Reflector
from .plugboard import Plugboard

class Enigma(object):
    '''Enigma Machine
    
    parameters
    ----------
    rotors : [str,str,str] in ['I', 'II', 'III', 'IV', 'V"]
    offsets : [int, int, int] in 0-25
    rings : [int, int, int] in 0-25
    reflector : str in ['B', 'C']
    plugbboard : str like 'AX BE LO DS'
    '''
    
    def __init__(self, 
                rotors=['I', 'II', 'III'],
                offsets=[0, 0, 0],
                rings=[0, 0, 0],
                reflector='B',
                plugboard=''):

        self.left_rotor = Rotor(rotor_type=rotors[0], ring_setting=rings[0], offset=offsets[0])
        self.middle_rotor = Rotor(rotor_type=rotors[1], ring_setting=rings[1], offset=offsets[1])
        self.right_rotor = Rotor(rotor_type=rotors[2], ring_setting=rings[2], offset=offsets[2])
        self.reflector = Reflector(reflector_type=reflector)
        self.plugboard = Plugboard(connections=plugboard)

    def encrypt(self, raw_input, verbose=False):
        '''Encrypt text by passing through the enigma machine'''
        out = ''
        for c in raw_input.upper():
            n = ord(c) - ord('A')
            # out += chr(self._encipher(n) + ord('A')) if n >= 0 and n < 26 else c
            out += chr(self._encipher(n, verbose) + ord('A')) if n >= 0 and n < 26 else c
        return out

    def decrypt(self, cypher_text):
        return self.encrypt(cypher_text)

    def _encipher(self, c, verbose):
        '''Pass single int-encoded character through the machine'''
        if verbose: return self._encipher_verbose(c)
        self._rotate_rotors()
        c1 = self.plugboard.encipher(c)
        c2 = self.right_rotor.encipher_forward(c1)
        c3 = self.middle_rotor.encipher_forward(c2)
        c4 = self.left_rotor.encipher_forward(c3)
        c5 = self.reflector.encipher(c4)
        c6 = self.left_rotor.encipher_backward(c5)
        c7 = self.middle_rotor.encipher_backward(c6)
        c8 = self.right_rotor.encipher_backward(c7)
        c9 = self.plugboard.encipher(c8)
        return c9

    def _encipher_verbose(self, c):
        '''Pass single int-encoded character through the machine'''
        to_char = lambda n: chr(n + ord('A'))
        f = 'Forward: '
        r = 'Reverse: '
        self._rotate_rotors()
        print(self.__repr__())
        f += f'{to_char(c)} -> |PB| -> '
        c1 = self.plugboard.encipher(c)
        f += f'{to_char(c1)} -> |R3| -> '
        c2 = self.right_rotor.encipher_forward(c1)
        f += f'{to_char(c2)} -> |R2| -> '
        c3 = self.middle_rotor.encipher_forward(c2)
        f += f'{to_char(c3)} -> |R1| -> '
        c4 = self.left_rotor.encipher_forward(c3)
        f += f'{to_char(c4)} -> |RF| -> '
        c5 = self.reflector.encipher(c4)
        f += f'{to_char(c5)}'
        r += f'{to_char(c5)} -> |R1| -> '
        c6 = self.left_rotor.encipher_backward(c5)
        r += f'{to_char(c6)} -> |R2| -> '
        c7 = self.middle_rotor.encipher_backward(c6)
        r += f'{to_char(c7)} -> |R3| -> '
        c8 = self.right_rotor.encipher_backward(c7)
        r += f'{to_char(c8)} -> |PB| -> '
        c9 = self.plugboard.encipher(c8)
        r += f'{to_char(c9)}'
        print(f)
        print(r)
        return c9

    def _rotate_rotors(self):
        # left rotor turnover and double stepping middle rotor
        if self.middle_rotor.is_at_notch():
            self.left_rotor.turnover()
            self.middle_rotor.turnover()
        # middle rotor turnover
        if self.right_rotor.is_at_notch():
            self.middle_rotor.turnover()
        # right rotor always turns
        self.right_rotor.turnover()

    def __repr__(self):
        r1, r2, r3 = self.left_rotor, self.middle_rotor, self.right_rotor
        n1, n2, n3 = r1.offset, r2.offset, r3.offset
        c1, c2, c3 = chr(n1 + ord('A')), chr(n2 + ord('A')), chr(n3 + ord('A'))
        t1, t2, t3 = r1.type_, r2.type_, r3.type_
        p1, p2, p3 = r1.notch_position, r2.notch_position, r3.notch_position
        out = f'<Enigma> offset: {c1}{c2}{c3} [{n1:2d},{n2:2d},{n3:2d}]; ' + \
            f'rotors: [{t1:3s},{t2:3s},{t3:3s}]; ' + \
            f'notch: [{p1:2d},{p2:2d},{p3:2d}]'
        return out

    

        



e = Enigma(rotors=['I', 'II', 'III'],
           offsets=[0, 0, 0],
           rings=[0, 0, 0],
           reflector='B',
           plugboard='')


e.encrypt('HELLO')
e.encrypt('hi there')