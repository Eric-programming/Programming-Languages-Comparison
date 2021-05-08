import java.util.*;

public class HashTableCode {
    public static void main(String[] args) {
        demo();
    }

    public static void demo() {
        // Define
        Map<Integer, Integer> hm = new HashMap<>();

        // Insertion
        Integer key = 0, value = 0;
        hm.put(key, value);

        // Access
        System.out.println(hm.get(key));
        System.out.println(hm.getOrDefault(key + 1, value + 1));

        hm.put(key + 1, hm.getOrDefault(key + 1, value + 1));

        // Deletion
        hm.remove(key);

        // Contains
        System.out.println(hm.containsKey(key));

        // Iterate
        for (Integer curKey : hm.keySet()) {
            Integer curValue = hm.get(curKey);
            System.out.println(curValue);
        }
    }
}