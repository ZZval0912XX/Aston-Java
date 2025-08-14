import java.util.ArrayList;
import java.util.List;

class Park {
    private String parkName;
    private List<Attraction> attractions;

    public Park(String parkName) {
        this.parkName = parkName;
        this.attractions = new ArrayList<>();
    }

    public class Attraction {
        private String attractionName;
        private String workingHours;
        private double price;

        public Attraction(String attractionName, String workingHours, double price) {
            this.attractionName = attractionName;
            this.workingHours = workingHours;
            this.price = price;
        }

        public String getAttractionName() {
            return attractionName;
        }

        public void setAttractionName(String attractionName) {
            this.attractionName = attractionName;
        }

        public String getWorkingHours() {
            return workingHours;
        }

        public void setWorkingHours(String workingHours) {
            this.workingHours = workingHours;
        }

        public double getPrice() {
            return price;
        }

        public void setPrice(double price) {
            this.price = price;
        }

        @Override
        public String toString() {
            return "Аттракцион: " + attractionName +
                   ", Время работы: " + workingHours +
                   ", Стоимость: " + price + " руб.";
        }
    }

    public void addAttraction(String name, String hours, double price) {
        Attraction attraction = new Attraction(name, hours, price);
        attractions.add(attraction);
    }

    public void displayAttractions() {
        System.out.println("Парк: " + parkName);
        System.out.println("Аттракционы:");
        for (Attraction attraction : attractions) {
            System.out.println(attraction);
        }
    }

    public String getParkName() {
        return parkName;
    }

    public void setParkName(String parkName) {
        this.parkName = parkName;
    }

    public List<Attraction> getAttractions() {
        return attractions;
    }

    public static void main(String[] args) {
        Park disneyland = new Park("Disneyland");

        disneyland.addAttraction("Колесо обозрения", "10:00 - 20:00", 500);
        disneyland.addAttraction("Американские горки", "09:00 - 19:00", 750);
        disneyland.addAttraction("Дом с привидениями", "12:00 - 22:00", 600);

        disneyland.displayAttractions();
    }
}
