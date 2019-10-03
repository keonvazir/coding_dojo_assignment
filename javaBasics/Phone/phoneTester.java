
public class phoneTester {

	public static void main(String[] args) {
		
		iPhone X = new iPhone("X", 99, "Verizon", "ring ring");

        X.displayInfo();
        System.out.println(X.ring());
        System.out.println(X.unlock());  

	}

}
