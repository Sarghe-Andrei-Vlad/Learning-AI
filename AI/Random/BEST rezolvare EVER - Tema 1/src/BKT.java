import java.util.*;

public class BKT {

    private final int[] startingState;
    int[] capacities;
    boolean[][] visitedStates;
    private Deque<int[]> solution = new ArrayDeque<>();
    private int numberOfSolutions = 0;

    public BKT(int[] capacities, int[] state, boolean[][] visitedStates) {
        this.startingState = state;
        this.capacities = capacities.clone();
        this.visitedStates = visitedStates.clone();
    }

    public int getNumberOfSolutions() {
        return numberOfSolutions;
    }

    public void solve() {
        System.out.println("Solving with BKT:");
        solution = new ArrayDeque<>();
        bkt(startingState);
        System.out.println("Number of solutions: " + getNumberOfSolutions());

    }
    private void bkt(int[] currentState) {
        int[] state = currentState.clone();

        solution.push(state);


        if (Verifier.isFinalState(state)) {
            numberOfSolutions++;
//            Collections.reverse(Arrays.asList(solution.element()));
            solution.forEach(s -> System.out.print(Arrays.toString(s)));
            System.out.println();
            return;
        }
        if (state[0] == -1 || state[1] == -1) {
            return;
        }

        if (Verifier.isStateVisited(state, visitedStates)) {
            return;
        }

        StateManager.visitState(visitedStates, state);


        for (String ac : Main.ACTIONS) {
            bkt(MoveApplier.doAction(state, capacities, ac));
            solution.pop();
        }

    }
}
