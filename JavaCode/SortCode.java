import java.util.*;

/**
 * SortCode
 */
public class SortCode {
    static class User {
        int id;

        public User(int id) {
            this.id = id;
        }

        public String toString() {
            return Integer.toString(this.id);
        }
    }

    public static void main(String[] args) {
        demo();
    }

    public static void demo() {
        // Variables
        List<Integer> l1 = new ArrayList<>(Arrays.asList(3, 1, 2));
        Integer[] l2 = { 3, 1, 2 };
        User[] l3 = { new User(3), new User(1), new User(2) };

        // Sort in Ascending
        Collections.sort(l1);
        System.out.println("\n l1 =>" + l1);
        Arrays.sort(l2);
        System.out.println("\n l2 =>" + Arrays.toString(l2));
        Arrays.sort(l3, (a, b) -> a.id - b.id);
        System.out.println("\n l3 =>" + Arrays.toString(l3));

        // Sort in descending
        Collections.sort(l1, Collections.reverseOrder());
        System.out.println("\n l1 =>" + l1);
        Arrays.sort(l2, Collections.reverseOrder());
        System.out.println("\n l2 =>" + Arrays.toString(l2));
        Arrays.sort(l3, (a, b) -> b.id - a.id);
        System.out.println("\n l3 =>" + Arrays.toString(l3));
    }

}