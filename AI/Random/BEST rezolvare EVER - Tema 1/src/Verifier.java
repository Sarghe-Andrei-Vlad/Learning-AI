public class Verifier {
    public static boolean isJugFull(int jugPosition, int jugCapacity, int[] capacities) {
        return jugCapacity == capacities[jugPosition];
    }

    public static boolean isJugEmpty(int jugCapacity) {
        return jugCapacity == 0;
    }

    public static boolean isFinalState(int[] state) {
        if (state[0] == Main.k || state[1] == Main.k)
            return true;
        return false;
    }

    public static boolean canPour(int[] state,int[] capacities, int fromJug, int toJug) {
        return !isJugEmpty(state[fromJug]) && !isJugFull(toJug, state[toJug], capacities);
    }

    public static boolean canFill(int[] state,int[] capacities, int pos) {
        return !isJugFull(pos, state[pos], capacities);
    }

    public static boolean canEmpty(int[] state, int pos) {
        return !isJugEmpty(state[pos]);
    }

    public static boolean isStateVisited(int[] state, boolean[][]visitedStates) {
        return visitedStates[state[0]][state[1]];
    }
    public static boolean isValidState(int[] state) {
        return state[0] != -1  && state[1] != -1;
    }
}
