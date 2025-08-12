public class Main {
    public static void main(String[] args) {
        checkNumber(5);
        checkNumber(-3);
        checkNumber(0);
    }

    public static void checkNumber(int number) {
        if (number >= 0) {
            System.out.println(number + " — положительное число.");
        } else {
            System.out.println(number + " — отрицательное число.");
        }
    }
}