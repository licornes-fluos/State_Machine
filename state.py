# A skeleton state machine that has different types of states, and transitions between them based on transition messages
# The state machine is a finite state machine, and the states are defined in a separate class
# The transitions are defined in a separate class

import random
import time

class StateMachine(object):
    def __init__(self, states, transitions):
        self.states = states
        self.transitions = transitions
        self.state = self.states[0]

    def transition(self, messages):
        successful_transitions = []
        for message in messages:
            for transition in self.transitions:
                if transition.message == message and transition.state == self.state:
                    self.state = transition.next_state
                    successful_transitions.append(transition)
        print("Transitioned to state: " + str(self.state.name), ", Successful transitions: " + str([st.message for st in successful_transitions]))
        print()
        return successful_transitions

    def __str__(self):
        return self.state.name
    
    def reset(self):
        self.state = self.states[0]
    
    def send_messages_with_random_delay(self, messages):
        time.sleep(random.random() / 10)
        self.transition(messages)

class State(object):
    def __init__(self, name):
        self.name = name
    
class Transition(object):
    def __init__(self, state, message, next_state):
        self.state = state
        self.message = message
        self.next_state = next_state

# Define the states
state1 = State("State 1")
state2 = State("State 2")
state3 = State("State 3")
state4 = State("State 4")

# Define the transitions
transition1 = Transition(state1, "Message 3", state3)
transition2 = Transition(state1, "Message 2", state2)
transition3 = Transition(state2, "Message 3", state4)
transition4 = Transition(state3, "Message 2", state4)

# Define the state machine
state_machine = StateMachine([state1, state2, state3, state4], [transition1, transition2, transition3, transition4])

# Test the state machine (python 3 syntax)
print(state_machine)
state_machine.transition(["Message 3", "Message 2"])
print(state_machine)
state_machine.transition(["Message 2"])
print(state_machine)
