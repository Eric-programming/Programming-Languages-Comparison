import java.util.*;

public class StackQueueCode {
    public static void main(String[] args) {
        demo();
    }

    public static void demo() {
        // Define
        Stack<Integer> stack = new Stack<>();// LIFO
        Queue<Integer> queue = new LinkedList<>();// FIFO

        // Insertion
        stack.push(1);
        stack.push(2);
        queue.add(1);
        queue.add(2);

        // Deletion
        stack.pop();
        queue.remove();
    }
}
