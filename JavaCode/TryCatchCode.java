public class TryCatchCode {
    public static void main(String[] args) {
        demo();
    }

    public static void demo() {
        try {
            int[] arr = { 1, 2, 3 };

            if (arr[0] < 10) {
                throw new Exception("Invalid Input");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        } finally {
            System.out.println("The 'try catch' is finished.");
        }
    }
}
