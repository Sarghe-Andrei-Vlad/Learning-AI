import math


def input_parameters():
    m = int(input("First jug capacity= "))
    n = int(input("Second jug capacity= "))
    k = int(input("k = "))
    return m, n, k


def initialize_state(m, n, k):
    return [0, 0, m, n, k]


def check_final_state(state):
    if state[4] == state[0] or state[4] == state[1]:
        return True

    return False


def validate_fill(state, dest):
    if dest not in [1, 2]:
        return False

    if dest == 1:
        if state[0] == state[2]:
            return False
    else:
        if state[1] == state[3]:
            return False

    return True


def fill(state, dest):
    if validate_fill(state, dest):
        test_state = state
        if dest == 1:
            quant_to_fill = test_state[2] - test_state[0]
            test_state[0] += quant_to_fill
        else:
            quant_to_fill = test_state[3] - test_state[1]
            test_state[1] += quant_to_fill
        return test_state

    return state




def is_solvable(state):
    if state[2] == 0 and state[3] == 0:
        if state[4] == 0:
            return True
        else:
            return False
    if state[2] < state[4] and state[3] < state[4]:
        return False
    if state[4] % math.gcd(state[2], state[3]) == 0:
        return True
    return False


def menu():
    m, n, k = input_parameters()
    initial_state = initialize_state(m, n, k)


menu()
