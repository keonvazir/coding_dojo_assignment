public class PythagoreanTest {
    public static void main(String[] args) {
        Pythagorean hyp = new Pythagorean();
        Double hypotenuse = hyp.calculateHypotenuse(3, 4);
        System.out.println(hypotenuse);
    }
}