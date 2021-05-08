import java.util.*;

public class DynamicArrCode {
    public static void main(String[] args) {
        demo();
    }

    public static void demo() {
        // Define
        List<Integer> list = new ArrayList<>();
        list = new ArrayList<>(Arrays.asList(1, 2, 3));

        // Insertion
        Integer val = 4;
        list.add(val);

        // Deletion
        int index = 0;
        list.remove(index);

        // Access
        System.out.println(list.get(index));
    }
}