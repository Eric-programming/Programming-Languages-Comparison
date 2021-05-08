import java.util.*;

public class HeapCode {
    public static void main(String[] args) {
        demo();
    }

    public static void demo() {
        // Define
        List<Integer> list = Arrays.asList(4, 2, 5, 1);
        Queue<Integer> minHeap = new PriorityQueue<>(list);
        Queue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        for (Integer num : list) {
            maxHeap.add(num);
        }
        // Insertion
        minHeap.add(9);
        maxHeap.add(0);

        // Access
        System.out.println(minHeap.peek());
        System.out.println(maxHeap.peek());

        // Deletion
        System.out.println(minHeap.poll());
        System.out.println(maxHeap.poll());
    }
}