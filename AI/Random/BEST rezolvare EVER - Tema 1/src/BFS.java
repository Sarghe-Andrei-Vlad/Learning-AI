import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class BFS {
    int[] startingState;

    Queue<int[]> queue = new LinkedList<>();
    int numberOfSolutions = 0;

    public BFS(int[] startingState) {
        this.startingState = startingState;
    }

    public void solve() {
        System.out.println("Solving with BFS: ");
        queue.add(startingState);

        int[] state;
        int[] newState;

        HashMap<int[], int[]> stateLink= new HashMap<>();
        stateLink.put(startingState, startingState.clone());

        while (!queue.isEmpty()) {
            state = queue.poll();

            if(Verifier.isFinalState(state)) {
                int[] prevState = state;
                do {
                    System.out.print(Arrays.toString(prevState));
                    prevState = stateLink.get(prevState);
                } while(stateLink.get(prevState) != null);

                System.out.println();
                numberOfSolutions++;
                continue;
            }

            StateManager.visitState(Main.visitedStates, state);

            for (String ac : Main.ACTIONS) {
                newState = MoveApplier.doAction(state, Main.capacities, ac);
                if(Verifier.isValidState(newState) && !Verifier.isStateVisited(newState, Main.visitedStates)) {
                    stateLink.put(newState, state);
                    queue.add(newState);
                }
            }
        }
        System.out.println("Number of solutions: " + numberOfSolutions);
    }
}
