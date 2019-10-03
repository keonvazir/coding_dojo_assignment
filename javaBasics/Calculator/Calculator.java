
class Calculator implements java.io.Serializable{
	/**
	 * 
	 */
	private static final long serialVersionUID = -4475413204294187573L;
	private double operandOne;
	private String operation;
	private double operandTwo;
	private double results;
	
	public Calculator(double operandOne, String operation, double operandTwo) {
		this.operandOne = operandOne;
		this.operandTwo = operandTwo; 
		this.operation = operation;//all private classes
	}
	public double getOperandOne(){
		return operandOne;
	}
	public void setOperandOne(double value) {
		this.operandOne = value;
	}
	public double getOperandTwo() {
		return operandTwo;
	}
	public void setOperandTwo(double value) {
		this.operandTwo = value;
	}
	public void setOperation(String value) {
		this.operation = value;
	}
	public void performOperation() {
		if(operation.equals("+")) {
			results = operandOne + operandTwo;
		}else if(operation.equals("-")) {
			results = operandOne - operandTwo;
		}
	}
	public double results() {
		return results;
	}
	
	
}