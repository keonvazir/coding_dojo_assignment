public class Ninja extends Human{
	public int stealth;
	public Ninja() {
		this.stealth = 10;
		this.health = 100;
	}
	public void steal(Ninja other) {
		int add=(this.stealth -= other.health);
		int newAdd = ((add) + (this.health));
		System.out.println("g"+ Integer.toString(newAdd));
		
	}
	public void runAway() {
		health -= 10;
		System.out.println("new health" + Integer.toString(health));
	}
	
}
