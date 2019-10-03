public class CalculatorTest {

	public static void main(String[] args) {
		Calculator b1 = new Calculator(10.5, "+", 5.2);
		b1.performOperation();
		System.out.println(b1.results());

	}

}
