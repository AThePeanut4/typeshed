"""
This module implements a Finite State Machine (FSM). In addition to state
this FSM also maintains a user defined "memory". So this FSM can be used as a
Push-down Automata (PDA) since a PDA is a FSM + memory.

The following describes how the FSM works, but you will probably also need to
see the example function to understand how the FSM is used in practice.

You define an FSM by building tables of transitions. For a given input symbol
the process() method uses these tables to decide what action to call and what
the next state will be. The FSM has a table of transitions that associate:

        (input_symbol, current_state) --> (action, next_state)

Where "action" is a function you define. The symbols and states can be any
objects. You use the add_transition() and add_transition_list() methods to add
to the transition table. The FSM also has a table of transitions that
associate:

        (current_state) --> (action, next_state)

You use the add_transition_any() method to add to this transition table. The
FSM also has one default transition that is not associated with any specific
input_symbol or state. You use the set_default_transition() method to set the
default transition.

When an action function is called it is passed a reference to the FSM. The
action function may then access attributes of the FSM such as input_symbol,
current_state, or "memory". The "memory" attribute can be any object that you
want to pass along to the action functions. It is not used by the FSM itself.
For parsing you would typically pass a list to be used as a stack.

The processing sequence is as follows. The process() method is given an
input_symbol to process. The FSM will search the table of transitions that
associate:

        (input_symbol, current_state) --> (action, next_state)

If the pair (input_symbol, current_state) is found then process() will call the
associated action function and then set the current state to the next_state.

If the FSM cannot find a match for (input_symbol, current_state) it will then
search the table of transitions that associate:

        (current_state) --> (action, next_state)

If the current_state is found then the process() method will call the
associated action function and then set the current state to the next_state.
Notice that this table lacks an input_symbol. It lets you define transitions
for a current_state and ANY input_symbol. Hence, it is called the "any" table.
Remember, it is always checked after first searching the table for a specific
(input_symbol, current_state).

For the case where the FSM did not match either of the previous two cases the
FSM will try to use the default transition. If the default transition is
defined then the process() method will call the associated action function and
then set the current state to the next_state. This lets you define a default
transition as a catch-all case. You can think of it as an exception handler.
There can be only one default transition.

Finally, if none of the previous cases are defined for an input_symbol and
current_state then the FSM will raise an exception. This may be desirable, but
you can always prevent this just by defining a default transition.

Noah Spurrier 20020822

PEXPECT LICENSE

    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt

    Copyright (c) 2012, Noah Spurrier <noah@noah.org>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from _typeshed import Incomplete

class ExceptionFSM(Exception):
    """This is the FSM Exception class."""
    value: Incomplete
    def __init__(self, value) -> None: ...

class FSM:
    """
    This is a Finite State Machine (FSM).
    
    """
    state_transitions: Incomplete
    state_transitions_any: Incomplete
    default_transition: Incomplete
    input_symbol: Incomplete
    initial_state: Incomplete
    current_state: Incomplete
    next_state: Incomplete
    action: Incomplete
    memory: Incomplete
    def __init__(self, initial_state, memory=None) -> None: ...
    def reset(self) -> None: ...
    def add_transition(self, input_symbol, state, action=None, next_state=None) -> None: ...
    def add_transition_list(self, list_input_symbols, state, action=None, next_state=None) -> None: ...
    def add_transition_any(self, state, action=None, next_state=None) -> None: ...
    def set_default_transition(self, action, next_state) -> None: ...
    def get_transition(self, input_symbol, state): ...
    def process(self, input_symbol) -> None: ...
    def process_list(self, input_symbols) -> None: ...

PY3: Incomplete

def BeginBuildNumber(fsm) -> None: ...
def BuildNumber(fsm) -> None: ...
def EndBuildNumber(fsm) -> None: ...
def DoOperator(fsm) -> None: ...
def DoEqual(fsm) -> None: ...
def Error(fsm) -> None: ...
def main() -> None:
    """
    This is where the example starts and the FSM state transitions are
    defined. Note that states are strings (such as 'INIT'). This is not
    necessary, but it makes the example easier to read. 
    """
    ...
