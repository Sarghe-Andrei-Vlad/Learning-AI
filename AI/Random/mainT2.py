#
# Reprezentarea unei stari:
# S = ((4, 2), 5, 3, 1)
#   = ((i, j), m, n, k) unde i <= m si j <= n, k <= max(m, n)
#             i si j fiind numarul de
#             litri din fiecare recipient
#
# Starile speciale sunt:
#     initiala -> ((0, 0), m, n, k)
#     finala   -> ((0, k), m, n, k) sau ((k, 0), m, n, k)

import copy
from queue import Queue
import math


class WaterJug:
    def __init__(self, m: int, n: int, k: int, state: list):
        self.max_capacity = [m, n]
        self.k = k
        self.state = state


def init_state(m: int, n: int, k: int):
    return WaterJug(m, n, k, [0, 0])


def is_final(jug_state: WaterJug):
    return jug_state.state[1] == jug_state.k or jug_state.state[0] == jug_state.k


def fill_is_valid(jug_state: WaterJug, jug_index: int):
    return (jug_index == 0 or jug_index == 1) and (
            jug_state.state[jug_index] < jug_state.max_capacity[jug_index]
    )


def empty_is_valid(jug_state: WaterJug, jug_index: int):
    return (jug_index == 0 or jug_index == 1) and (jug_state.state[jug_index] > 0)


def move_is_valid(jug_state: WaterJug, src: int, dest: int):
    if jug_state.state[src] == 0:
        return False

    if jug_state.state[dest] == jug_state.max_capacity[dest]:
        return False

    return True


def empty_jug(jug_state: WaterJug, jug_index: int):
    ret_value = copy_object(jug_state)
    if empty_is_valid(ret_value, jug_index):
        ret_value = copy_object(jug_state)
        ret_value.state[jug_index] = 0
        return ret_value
    else:
        return -1


def move_all_water(jug_state: WaterJug, src: int, dest: int):
    ret_value = copy_object(jug_state)
    if move_is_valid(ret_value, src, dest):
        tmp = ret_value.state[dest]
        ret_value.state[dest] = min(
            ret_value.state[dest] + ret_value.state[src], ret_value.max_capacity[dest]
        )
        ret_value.state[src] -= ret_value.state[dest] - tmp
        return ret_value
    else:
        return -1


def copy_object(jug_state):
    m = jug_state.max_capacity[0]
    n = jug_state.max_capacity[1]
    k = jug_state.k
    state = copy.deepcopy(jug_state.state)
    return WaterJug(m, n, k, state)


def fill_jug(jug_state: WaterJug, jug_index: int):
    ret_value = copy_object(jug_state)
    if fill_is_valid(ret_value, jug_index):
        ret_value.state[jug_index] = ret_value.max_capacity[jug_index]
        return ret_value
    else:
        return -1


def a_star_heuristic(jug: WaterJug):
    return abs(jug.state[0] - jug.k) + abs(jug.state[1] - jug.k)


def bfs(init_state):
    if (
            init_state.state[0] > init_state.max_capacity[0]
            or init_state.state[1] > init_state.max_capacity[1]
    ):
        print("Input state is invalid")
        return -1

    q = Queue()
    visited = []
    solution = []
    q.put(init_state)
    solution_queue = Queue()
    solution_queue.put([init_state.state])

    while q.qsize() > 0:
        first_element = q.get()
        first_solution: list = solution_queue.get()

        if first_element.state in visited:
            continue

        solution.append(first_element.state)
        visited.append(first_element.state)

        transitions_1 = [
            move_all_water(first_element, 0, 1),
            move_all_water(first_element, 1, 0),
            empty_jug(first_element, 0),
            empty_jug(first_element, 1),
            fill_jug(first_element, 0),
            fill_jug(first_element, 1),
        ]

        valid_transitions = [t for t in transitions_1 if t != -1]

        for t in valid_transitions:
            q.put(t)
            new_solution = copy.deepcopy(first_solution)
            new_solution.append(t.state)
            if t.k in t.state:
                return new_solution
            solution_queue.put(new_solution)

    return -1


def backtracking(jug: WaterJug, stack: list, visited: list):
    if is_final(jug):
        stack.append(jug)
        for s in stack:
            print(s.state)
        print('------------------------------------------------')
        return

    if jug.state in visited:
        return

    visited.append(jug.state)
    transitions_1 = [
        move_all_water(jug, 0, 1),
        move_all_water(jug, 1, 0),
        empty_jug(jug, 0),
        empty_jug(jug, 1),
        fill_jug(jug, 0),
        fill_jug(jug, 1),
    ]

    valid_transitions = [t for t in transitions_1 if t != -1]
    if len(valid_transitions) == 0:
        return
    else:
        for transition in valid_transitions:
            stack.append(jug)
            backtracking(transition, stack, visited)
            stack.pop()


# heuristic for hill climbing
def fitness(current_state: WaterJug, visited: list):
    transitions = [
        move_all_water(current_state, 0, 1),
        move_all_water(current_state, 1, 0),
        empty_jug(current_state, 0),
        empty_jug(current_state, 1),
        fill_jug(current_state, 0),
        fill_jug(current_state, 1),
    ]

    valid_transitions = [t for t in transitions if t != -1 and t.state not in visited]
    for transition in valid_transitions:
        if is_final(transition):
            return 10
    return len(valid_transitions)


def hill_climbing(init_state):
    solution = [init_state.state]
    is_found = False

    visited = [init_state.state]

    if is_final(init_state):
        return solution
    current_state = init_state

    while not is_found:
        transitions_1 = [
            empty_jug(current_state, 0),
            empty_jug(current_state, 1),
            fill_jug(current_state, 0),
            fill_jug(current_state, 1),
            move_all_water(current_state, 0, 1),
            move_all_water(current_state, 1, 0),
        ]
        valid_transitions = [t for t in transitions_1 if t != -1 and t.state not in visited]

        if len(valid_transitions) == 0:
            print(f"The algorithm failed at step {str(current_state.state)}. There are no more valid transitions.")
            return -1

        max_fitness = a_star_heuristic(current_state)
        best_jug = current_state
        for t in valid_transitions:
            if is_final(t):
                solution.append(t.state)
                return solution
            if a_star_heuristic(t) <= max_fitness:
                max_fitness = a_star_heuristic(t)
                best_jug = t
        if best_jug == current_state:
            print(f"The algorithm failed at step {str(current_state.state)}. No better fitness found.")
            return -1
        current_state = best_jug
        visited.append(current_state.state)
        solution.append(current_state.state)


def is_in_pq(jug: WaterJug, pq):
    for element in pq:
        if jug == element[1]:
            return True
    return False


def update(neighbour, pq, new_cost):
    for element in pq:
        if element[1] == neighbour:
            element[0] = new_cost
            return
    return


def get_solution(parents, current_state):
    steps = []
    solution = []
    last_state = copy_object(current_state)

    while parents.get(current_state) is not None:
        parent = parents.get(current_state)
        steps.append(parent)
        current_state = parent

    i = 0
    while len(steps) > 0:
        state = steps.pop()
        solution.append(state.state)
        i += 1

    solution.append(last_state.state)
    return solution


def is_element_of(element, vec):
    for v in vec:
        if v[1].state == element.state:
            return True
    return False


def remove(vec, element):
    for i, v in enumerate(vec):
        if v[1].state == element.state:
            vec.pop(i)


def a_star(current_state):
    cost = dict()
    heuristic = dict()
    visited = []
    parents = dict()

    cost[current_state] = 0
    heuristic[current_state] = a_star_heuristic(current_state)  # the distance to the final state

    pq = [(cost[current_state] + heuristic[current_state], current_state)]

    while len(pq) > 0:
        pq.sort(key=lambda x: x[0])  # sort by cost
        node = pq.pop(0)[1]
        visited.append(node.state)

        if is_final(node):
            return get_solution(parents, node)
        transitions_1 = [
            move_all_water(node, 0, 1),
            move_all_water(node, 1, 0),
            empty_jug(node, 0),
            empty_jug(node, 1),
            fill_jug(node, 0),
            fill_jug(node, 1),
        ]
        valid_transitions = [t for t in transitions_1 if t != -1 and t.state not in visited]

        for transition in valid_transitions:
            c = cost[node] + 1
            h = a_star_heuristic(transition)

            if is_in_pq(transition, pq):
                old_c = cost[transition]
                old_h = heuristic[transition]

                if old_h + old_c > c + h:
                    cost[transition] = c
                    heuristic[transition] = h

                    update(transition, pq, c + h)
                    parents[transition] = node
            else:
                cost[transition] = c
                heuristic[transition] = h

                pq.append((c + h, transition))
                parents[transition] = node


def check_data(jug: WaterJug):
    if jug.state[0] + jug.state[1] < jug.k:
        return False
    if jug.state[0] == 0 and jug.state[1] == 0:
        return jug.k == 0
    return jug.k % math.gcd(jug.state[0], jug.state[1]) == 0


def pick_parameters():
    m = int(input("Quantity in the first jug: "))
    n = int(input("Quantity in the second jug: "))
    k = int(input("k: "))
    return m, n, k


def main():
    m, n, k = pick_parameters()
    while True:
        init_problem = init_state(m, n, k)
        print("Pick an algorithm (1-4), validate data (5), change parameters(6) or press 0 to exit:")
        choice = int(input("1. BFS\n2. Backtracking\n3. Hill Climbing\n4. A*\n5. Check data\n6. Change parameters\n"))
        if choice == 0:
            break
        if choice == 1:
            print(bfs(init_problem))
        elif choice == 2:
            backtracking(init_problem, [], [])
        elif choice == 3:
            print(hill_climbing(init_problem))
        elif choice == 4:
            print(a_star(init_problem))
        elif choice == 5:
            print(check_data(init_problem))
        else:
            m, n, k = pick_parameters()


if __name__ == "__main__":
    main()
