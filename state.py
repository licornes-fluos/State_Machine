# A skeleton state machine that has different types of states, and transitions between them based on transition messages
# The state machine is a finite state machine, and the states are defined in a separate class
# The transitions are defined in a separate class

import random
import time
from transition import Transition

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

