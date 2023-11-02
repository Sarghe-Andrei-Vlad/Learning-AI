import java.util.Objects;

public class MoveApplier {
    static final String FIRST = "first";
    static final String SECOND = "second";
    static final String FILL_FIRST = "fill first";
    static final String FILL_SECOND = "fill second";
    static final String EMPTY_FIRST = "empty first";
    static final String EMPTY_SECOND = "empty second";
    static final String FIRST_TO_SECOND = "first to second";
    static final String SECOND_TO_FIRST = "second to first";
    public static int[] pour(int[] currentState,int[] capacities, String into) {
        int[] state = currentState.clone();
        int fromJug = Objects.equals(into, Main.FIRST) ? 1 : 0;
        int toJug = Objects.equals(into, Main.FIRST) ? 0 : 1;

        if (!Verifier.canPour(state, capacities, fromJug, toJug)) {
            state[0] = -1;
            state[1] = -1;
            return state;
        }

        state[toJug] += state[fromJug];
        state[fromJug] = 0;
        int difference = state[toJug] - Main.capacities[toJug];
        if (difference > 0) {
            state[fromJug] = difference;
            state[toJug] = Main.capacities[toJug];
        }
        return state;
    }

    public static int[] fill(int[] currentState,int[] capacities, String jug) {
        int[] state = currentState.clone();

        int pos = Objects.equals(jug, Main.FIRST) ? 0 : 1;
        if (!Verifier.canFill(state, capacities, pos)) {
            state[0] = -1;
            state[1] = -1;
            return state;
        }
        state[pos] = capacities[pos];
        return state;
    }

    public static int[] empty(int[] currentState, String jug) {
        int[] state = currentState.clone();
        int pos = Objects.equals(jug, Main.FIRST) ? 0 : 1;
        if (!Verifier.canEmpty(state, pos)) {
            state[0] = -1;
            state[1] = -1;
            return state;
        }
        state[pos] = 0;
        return state;
    }

    static int[] doAction(int[] state,int[] capacities, String action) {

        switch (action) {
            case FILL_FIRST -> {
                return fill(state,capacities, FIRST);
            }
            case FILL_SECOND -> {
                return fill(state,capacities, SECOND);
            }
            case EMPTY_FIRST -> {
                return empty(state, FIRST);
            }
            case EMPTY_SECOND -> {
                return empty(state, SECOND);
            }
            case FIRST_TO_SECOND -> {
                return pour(state, capacities, SECOND);
            }
            case SECOND_TO_FIRST -> {
                return pour(state,capacities, FIRST);
            }
            default -> {
                return new int[2];
            }
        }
    }
}
