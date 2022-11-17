# A skeleton state machine that has different types of states, and transitions between them based on transition messages
# The state machine is a finite state machine, and the states are defined in a separate class
# The transitions are defined in a separate class

import random
import time
import threading

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
                elif message == "Message E1" or message == "Message E2" or message == "Message E3" or message == "Message E4":
                    self.state = transition.next_state
                    successful_transitions.append(transition)
        # print("Transitioned to state: " + str(self.state.name), ", Successful transitions: " + str([st.message for st in successful_transitions]))
        # print()
        return successful_transitions

    def check_transition(self):
        messages = []
        for transition in self.transitions:
            if transition.state == self.state:
                messages.append(transition.message)
        if len(messages) != 0:
            choice_num = random.randint(0,10)
            if choice_num > 9:
                out_message = messages[1]
            else:
                out_message = messages[0]
            #out_message = random.choice(messages)
            # print("Sending message: " + str(out_message))
            self.transition([out_message])
            return out_message
        return None

    def feed_messages_with_random_timing_per_message(self, messages, i):
        start_state = self.state
        total_delay = 0
        for message in messages:
            delay = random.random()
            total_delay += delay
            time.sleep(delay)
            self.transition([message])
        print("SM " + str(i) + " transition to " + self.state.name + " finished after " + str(total_delay) + " seconds, messages: " + str(messages) + ", start state: " + start_state.name)

    def __str__(self):
        return self.state.name

    def reset(self):
        self.state = self.states[0]
    
    # def receive_messages_with_random_delay(self, messages):
    #     time.sleep(random.random() / 10)
    #     self.transition(messages)

class State(object):
    def __init__(self, name):
        self.name = name
    
class Transition(object):
    def __init__(self, state, message, next_state):
        self.state = state
        self.message = message
        self.next_state = next_state
    
    def get_messages_for_state(self, state):
        return [transition.message for transition in self.transitions if transition.state == state]

# def run_state_checks(sm):
#     time.sleep(random.random() / 10)
#     out_message = sm.check_transition()
#     return out_message

# Define the states
state1 = State("State 1")
state2 = State("State 2")
state3 = State("State 3")
state4 = State("State 4")
#emergency state
stateE = State("Emergency")

# Define the transitions
#transition1 = Transition(state1, "Message 3", state3)
#transition2 = Transition(state1, "Message 2", state2)
#transition3 = Transition(state2, "Message 3", state4)
#transition4 = Transition(state3, "Message 2", state4)

#regular transitions
transition1 = Transition(state1, "Message 1", state2)
transition2 = Transition(state2, "Message 2", state3)
transition3 = Transition(state3, "Message 3", state4)
#transition4 = Transition(state3, "Message 4", state4)

#emergency transitions
transitionE1 = Transition(state1, "Message E1", stateE)
transitionE2 = Transition(state2, "Message E2", stateE)
transitionE3 = Transition(state3, "Message E3", stateE)
transitionE4 = Transition(state4, "Message E4", stateE)


# Define the state machine
state_machine1 = StateMachine([state1, state2, state3, state4, stateE], [transition1, transition2, transition3, transitionE1, transitionE2, transitionE3, transitionE4])
state_machine2 = StateMachine([state1, state2, state3, state4, stateE], [transition1, transition2, transition3, transitionE1, transitionE2, transitionE3, transitionE4])
state_machine3 = StateMachine([state1, state2, state3, state4, stateE], [transition1, transition2, transition3, transitionE1, transitionE2, transitionE3, transitionE4])
state_machine4 = StateMachine([state1, state2, state3, state4, stateE], [transition1, transition2, transition3, transitionE1, transitionE2, transitionE3, transitionE4])


for i in range(3):
    out_messages = []
    for sm in [state_machine1, state_machine2, state_machine3, state_machine4]:
        if random.random() > 0.5:
            out_messages.append(sm.check_transition())
        else:
            out_messages.append(None)
    print(out_messages)
    for sm, out_message in zip([state_machine1, state_machine2, state_machine3, state_machine4], out_messages):
        for i, other_sm in enumerate([state_machine1, state_machine2, state_machine3, state_machine4]):
            if other_sm != sm and out_message is not None:
                threading.Thread(target=other_sm.feed_messages_with_random_timing_per_message, args=([out_message], i,)).start()
    time.sleep(1.2)
    if state_machine1.state != state_machine2.state or state_machine1.state != state_machine3.state or state_machine1.state != state_machine4.state:
        print("State machines are not in the same state")
        break
    print([(i, sm.state.name) for i, sm in enumerate([state_machine1, state_machine2, state_machine3, state_machine4])])
    #for sm in [state_machine1, state_machine2, state_machine3, state_machine4]:
    #    sm.reset()

# # Test the state machine (python 3 syntax)
# print(state_machine)
# state_machine.transition(["Message 3", "Message 2"])
# print(state_machine)
# state_machine.transition(["Message 2"])
# print(state_machine)
