class Transition(object):
    def __init__(self, state, message, next_state):
        self.state = state
        self.message = message
        self.next_state = next_state