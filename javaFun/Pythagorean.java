public class Pythagorean {
    public double calculateHypotenuse(int legA, int legB) {
        double c = Math.sqrt(Math.pow(legA, 2)+ Math.pow(legB, 2));
        return c;
        // the hypotenuse is the side across the right angle. 
        // calculate the value of c given legA and legB
    }
}
    