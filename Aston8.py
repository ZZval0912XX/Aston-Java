public class Main {
    public static void main(String[] args) {
        int year = 2024;
        boolean isLeap = isLeapYear(year);
        System.out.println(year + " год високосный? " + isLeap);
    }

    public static boolean isLeapYear(int year) {
        if (year % 4 != 0) {
            return false;
        } else if (year % 100 != 0) {
            return true;
        } else {
            return year % 400 == 0;
        }
    }
}