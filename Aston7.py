public

class Main {
    public static void main(String[] args) {
        printStringMultipleTimes("Hello!", 5);
    }
    public static void printStringMultipleTimes(String str, int times) {
        for (int i = 0; i < times; i++) {
            System.out.println(str);
        }
    }
}