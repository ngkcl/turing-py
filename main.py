from turing import TuringMachine

#  Example configuration ----------
tape = '01_'
initial_state = 'q0'
final_states = {'q1'}

transition_function = {
    ('q0', '0'): ('q0', '1', 'R'),
    ('q0', '1'): ('q0', '0', 'R'),
    ('q0', '_'): ('q1', '_', 'N')
}
# ---------------------------------

turing_machine = TuringMachine(
    tape,
    initial_state,
    final_states,
    transition_function
)

print("initial tape: " + turing_machine.get_tape())

while not turing_machine.final():
    turing_machine.step()

print("final tape: " + turing_machine.get_tape())