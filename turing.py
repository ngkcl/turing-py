class Tape(object):
    blank_symbol = '_'

    def __init__(self, tape_string = ''):
        self._tape = dict(enumerate(tape_string))
    
    def __str__ (self):
        s = ""
        min_i = min(self._tape.keys())
        max_i = max(self._tape.keys())
        for i in range(min_i, max_i):
            s += self._tape[i]
        return s
    def __getitem__ (self, index):
        if index in self._tape:
            return self._tape[index]
        else:
            return Tape.blank_symbol
    
    def __setitem__ (self, index, value):
        self._tape[index] = value
    
class TuringMachine(object):

    def __init__ (
        self,
        tape = '',
        initial_state = '',
        final_states = None,
        transition_function = None
    ):

        self._tape = Tape(tape)
        self._head_position = 0
        self._blank_symbol = Tape.blank_symbol
        self._current_state = initial_state

        if transition_function == None:
            self._transition_function = {}
        else:
            self._transition_function = transition_function
        
        if final_states == None:
            self._final_states = set()
        else:
            self._final_states = final_states
    
    def get_tape(self):
        return str(self._tape)
    
    def step(self):
        under_head = self._tape[self._head_position]
        x = (self._current_state, under_head)
        if x in self._transition_function:
            y = self._transition_function[x]
            self._tape[self._head_position] = y[1]
            
            # TODO: Add checks for start/end of tape
            if y[2] == 'R':
                self._head_position += 1
            elif y[2] == 'L':
                self._head_position -= 1
            self._current_state = y[0]
    
    def final(self):
        if self._current_state in self._final_states:
            return True
        else:
            return False
