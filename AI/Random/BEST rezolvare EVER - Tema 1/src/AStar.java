import java.util.ArrayList;
import java.util.Arrays;

public class AStar {
    int[] startingState;
    int numberOfSolutions = 0;
    ArrayList<int[]> path = new ArrayList<>();

    public AStar(int[] startingState) {
        this.startingState = startingState;
    }

    public void solve() {
        System.out.println("Solving with Hill Climbing: ");
        hillClimbing(startingState);
        if (numberOfSolutions != 0)
            for (int[] state : path) {
                System.out.print(Arrays.toString(state));
            }
        System.out.println();
        System.out.println("Number of solutions: " + numberOfSolutions);
    }

    private int getHeuristic(int[] state) {
        return 1 - Math.min(Math.abs(Main.k - state[0]), Math.abs(Main.k - state[1]));
    }

    private int getReachCost(int[] state){
        return 1;
    }

    private ArrayList<int[]> getNeighbours(int[] currentState) {

        ArrayList<int[]> neighbourStates = new ArrayList<>();

        for (String action : Main.ACTIONS)
            neighbourStates.add(MoveApplier.doAction(currentState, Main.capacities, action));

        return neighbourStates;
    }

    private ArrayList<int[]> sortByCost(ArrayList<int[]> neighbourStates) {
        for (int i = 0; i < neighbourStates.size(); ++i) {
            for (int j = i + 1; j < neighbourStates.size(); ++j) {

                int x = getHeuristic(neighbourStates.get(i)) + getReachCost(neighbourStates.get(i));
                int y = getHeuristic(neighbourStates.get(j)) + getReachCost(neighbourStates.get(j));

                if (x < y) {
                    int[] aux = neighbourStates.get(i);
                    neighbourStates.set(i, neighbourStates.get(j));
                    neighbourStates.set(j, aux);
                }
            }
        }
        return neighbourStates;
    }

    private void hillClimbing(int[] startingState) {
        int[] currentState = startingState.clone();
        boolean allVisited = true;

        if (Verifier.isFinalState(currentState)) {
            numberOfSolutions++;
            return;
        }

        while (true) {
            ArrayList<int[]> neighbourStates = getNeighbours(currentState);

            neighbourStates = sortByCost(neighbourStates);

//            System.out.print(Arrays.toString(currentState));
            path.add(currentState);

            if (Verifier.isFinalState(currentState)) {
                numberOfSolutions++;
                break;
            }

            for (int[] neighbour : neighbourStates) {
                if (neighbour[0] == -1 || neighbour[1] == -1) {
                    return;
                }

                if (!Verifier.isStateVisited(neighbour, Main.visitedStates)) {
                    StateManager.visitState(Main.visitedStates, neighbour);
                    currentState = neighbour;
                    allVisited = false;
                    break;
                }
            }

            if (allVisited) {
                currentState = neighbourStates.get(0);
            }
        }
    }
}
