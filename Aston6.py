public class Main {
    public static void main(String[] args) {
        int number = -6;
        boolean isNegative = isNegative(number);
        System.out.println("Число " + number + " отрицательное? " + isNegative);
    }

    public static boolean isNegative(int number) {
        return number < 0;
    }
}