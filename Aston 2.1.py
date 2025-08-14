import java.time.LocalDate;

class Product {
    private String name;
    private LocalDate productionDate;
    private String manufacturer;
    private String countryOfOrigin;
    private double price;
    private boolean isReserved;

    public Product(String name, LocalDate productionDate, String manufacturer,
                   String countryOfOrigin, double price, boolean isReserved) {
        this.name = name;
        this.productionDate = productionDate;
        this.manufacturer = manufacturer;
        this.countryOfOrigin = countryOfOrigin;
        this.price = price;
        this.isReserved = isReserved;
    }
public void printInfo() {
        System.out.println("Название: " + name);
        System.out.println("Дата производства: " + productionDate);
        System.out.println("Производитель: " + manufacturer);
        System.out.println("Страна происхождения: " + countryOfOrigin);
        System.out.println("Цена: " + price + " руб.");
        System.out.println("Забронирован: " + (isReserved ? "Да" : "Нет"));
    }

    public static void main(String[] args) {
        Product product = new Product(
                "Смартфон XYZ",
                LocalDate.of(2023, 10, 15),
                "TechCorp",
                "Китай",
                59999.99,
                false
        );

        product.printInfo();
    }
}
