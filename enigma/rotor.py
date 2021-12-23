# Rotor Wiring and Notches
# If type I rotor steps from Q to R, the next rotor is advanced.
ROTOR_SPECS = {
    'I':   {'wiring': "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'notch': "Q"},
    'II':  {'wiring': "AJDKSIRUXBLHWTMCQGZNPYFVOE", 'notch': "E"},
    'III': {'wiring': "BDFHJLCPRTXVZNYEIWGAKMUSQO", 'notch': "V"},
    'IV':  {'wiring': "ESOVPZJAYQUIRHXLNFTGKDCMWB", 'notch': "J"},
    'V':   {'wiring': "VZBRGITYUPSDNHLXAWMJQOFECK", 'notch': "Z"}
}
# ROTOR_SPECS_NUMERIC = {k: {'wiring': [ord(c) - ord('A') for c in d['wiring']], 'notch': ord(d['notch']) - ord('A')} for k, d in ROTOR_SPECS_CHAR.items()}

class Rotor(object):
    '''Rotor'''
    
    def __init__(self, rotor_type, ring_setting, offset):
        self.type_ = rotor_type
        self.offset = offset
        self.ring_setting = ring_setting
        # self.notch_position = ROTOR_SPECS_NUMERIC[rotor_type]['notch']
        # self.forward_wiring = ROTOR_SPECS_NUMERIC[rotor_type]['wiring']
        self.notch_position = self.__char_to_int(ROTOR_SPECS[rotor_type]['notch'])
        self.forward_wiring = self.__char_wiring_to_int_wiring(ROTOR_SPECS[rotor_type]['wiring'])
        self.backward_wiring = self.__reverse_wiring(self.forward_wiring)

    def __char_wiring_to_int_wiring(self, char_wiring):
        return [self.__char_to_int(c)  for c in char_wiring]

    def __char_to_int(self, c):
        return ord(c) - ord('A')

    def __reverse_wiring(self, wiring):
        '''Get the wiring index list for the backward pass.'''
        inverse_wiring = [0] * len(wiring)
        for i in range(len(wiring)):
            inverse_wiring[wiring[i]] = i
        return inverse_wiring

    def encipher_forward(self, input):
        '''Forward (first) pass to substitute the input character.
        input : int, returns int'''
        return self.__encipher(input, self.offset, self.ring_setting, self.forward_wiring)

    def encipher_backward(self, input):
        '''Backward (return) pass to substitute the input character.
        input : int, returns int'''
        return self.__encipher(input, self.offset, self.ring_setting, self.backward_wiring)

    def __encipher(self, input, offset, ring_setting, wiring):
        shift = offset - ring_setting
        wiring_input = (input + shift) % 26
        wiring_output = wiring[wiring_input]
        output = (wiring_output - shift) % 26
        return output

    def is_at_notch(self):
        return self.offset == self.notch_position

    def turnover(self):
        self.offset = (self.offset + 1) % 26


r = Rotor(rotor_type='I',
          ring_setting=0,
          offset=0)
r.encipher_forward(0)
r.encipher_backward(0)
r.turnover()
r.encipher_forward(0)
r.encipher_backward(0)
r = Rotor(rotor_type='I',
          ring_setting=0,
          offset=1)
r.encipher_forward(0)
r.encipher_backward(0)
