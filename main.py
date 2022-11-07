from state import StateMachine, State
from transition import Transition

state1 = State("State 1")
state2 = State("State 2")
state3 = State("State 3")
state4 = State("State 4")

# Define the transitions
transition1 = Transition(state1, "Message 3", state3)
transition2 = Transition(state1, "Message 2", state2)
transition3 = Transition(state2, "Message 3", state4)
transition4 = Transition(state3, "Message 2", state4)

transitions = [transition1,transition2,transition3,transition4]
states = [state1,state2,state3,state4]

sm1 = StateMachine(states,transitions)
sm2 = StateMachine(states,transitions)
sm3 = StateMachine(states,transitions)
sm4 = StateMachine(states,transitions)

transitionSeries = ["Message 2","Message 3"]
sm1.transition(transitionSeries)