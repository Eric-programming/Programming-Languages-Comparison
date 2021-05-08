public class StringCode {
    public static void main(String[] args) {
        demo();
    }

    public static void demo() {
        // String to number
        String str = "123";
        int num = Integer.parseInt(str);

        // Number to String
        str = Integer.toString(num * 10);

        // String to Char[]
        char[] charArr = str.toCharArray();

        // String compare
        System.out.println(str == "1230");
        System.out.println(str.equals("1230"));

        // substring
        System.out.println(str.substring(1));
        System.out.println(str.substring(1, 3));

        // Append char
        StringBuilder sb = new StringBuilder(str);
        sb.append('0');
        System.out.println(sb.toString());
    }
}
