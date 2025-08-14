import java.util.ArrayList;

class Animal {
private static int animalCount = 0;
private String name;

public Animal(String name) {
this.name = name;
animalCount++;
}

public void run(int distance) {
System.out.println(name + " пробежал " + distance + " м.");
}

public void swim(int distance) {
System.out.println(name + " проплыл " + distance + " м.");
}

public String getName() {


return name;
}

public
static
int
getAnimalCount()
{
return animalCount;
}
}


class Dog extends Animal {
private static int dogCount = 0;
private final int maxRunDistance = 500;
private final int maxSwimDistance = 10;

public Dog(String name) {
super(name);
dogCount++;
}

@ Override
public void run(int distance) {
if (distance <= maxRunDistance) {
super.run(distance);
} else {
System.out.println(getName() + " не может пробежать больше " + maxRunDistance + " м.");
}
}

@ Override
public void swim(int distance) {
if (distance <= maxSwimDistance) {
super.swim(distance);
} else {
System.out.println(getName() + " не может проплыть больше " + maxSwimDistance + " м.");
}
}

public static int getDogCount() {


return dogCount;
}
}


class Cat extends Animal {
private static int catCount = 0;
private final int maxRunDistance = 200;
private boolean isFull = false;

public Cat(String name) {
super(name);
catCount++;
}

@ Override
public void run(int distance) {
if (distance <= maxRunDistance) {
super.run(distance);
} else {
System.out.println(getName() + " не может пробежать больше " + maxRunDistance + " м.");
}
}

@ Override
public void swim(int distance) {
System.out.println(getName() + " не умеет плавать.");
}

public void eat(Bowl bowl, int amount) {
if (bowl.decreaseFood(amount)) {
isFull = true;
System.out.println(getName() + " поел из миски и теперь сыт.");
} else {
System.out.println(getName() + " не смог поесть из миски. Недостаточно еды.");
}
}

public boolean isFull() {


return isFull;
}

public
static
int
getCatCount()
{
return catCount;
}
}

class Bowl {
private int foodAmount;

public Bowl(int initialFood) {
this.foodAmount = Math.max(initialFood, 0); // Гарантируем, что не будет отрицательного значения
}

public boolean decreaseFood(int amount) {
if (amount <= 0) {
System.out.println("Количество еды должно быть положительным.");


return false;
}
if (foodAmount >= amount) {
foodAmount -= amount;
return true;
}
return false;
}

public
void
addFood(int
amount) {
if (amount > 0) {
foodAmount += amount;
System.out.println("В миску добавлено " + amount + " еды. Теперь в миске " + foodAmount + " еды.");
} else {
System.out.println("Можно добавлять только положительное количество еды.");
}
}

public
int
getFoodAmount()
{
return foodAmount;
}
}

public


class Main {
public static void main(String[] args) {

Dog dog = new Dog("Бобик");
Cat cat = new Cat("Мурзик");

dog.run(150);
dog.run(600);
dog.swim(5);
dog.swim(15);

cat.run(100);
cat.run(250);
cat.swim(10);

Bowl bowl = new Bowl(30);
System.out.println("\nСоздаем котов и кормим их:");

ArrayList < Cat > cats = new ArrayList <> ();
cats.add(new Cat("Барсик"));
cats.add(new Cat("Васька"));
cats.add(new Cat("Рыжик"));
cats.add(new Cat("Черныш"));

for (Cat c: cats

) {
    c.eat(bowl, 10);
}

System.out.println("\nСостояние котов:");
for (Cat c: cats)
{
    System.out.println(c.getName() + ": " + (c.isFull() ? "сыт": "голоден"));
}

bowl.addFood(20);

System.out.println("\nКормим оставшихся голодных котов:");
for (Cat c: cats)
{
if (!c.isFull()) {
    c.eat(bowl, 10);
}
}

System.out.println("\nФинальное состояние котов:");
for (Cat c: cats)
{
    System.out.println(c.getName() + ": " + (c.isFull() ? "сыт": "голоден"));
}

System.out.println("\nВсего животных: " + Animal.getAnimalCount());
System.out.println("Всего собак: " + Dog.getDogCount());
System.out.println("Всего котов: " + Cat.getCatCount());
}
}
