public class StateManager {
    public static void visitState(boolean[][] visitedStates, int[] state) {
        visitedStates[state[0]][state[1]] = true;
    }

    public static void unvisitState(boolean[][] visitedStates, int[] state) {
        if (state[0] != -1 && state[1] != -1)
            visitedStates[state[0]][state[1]] = false;
    }
}
