public class Main {
    public static void main(String[] args) {
        int len = 5;
        int initialValue = 10;

        int[] array = createArray(len, initialValue);

        for (int value : array) {
            System.out.print(value + " ");
        }
    }

    public static int[] createArray(int len, int initialValue) {
        int[] array = new int[len];
        for (int i = 0; i < len; i++) {
            array[i] = initialValue;
        }
        return array;
    }
}