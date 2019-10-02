public class Samurai extends Human{
	private static int numInstances = 0;
	public int health;
	public Samurai() {
		this.health = 200;
	
		
	}
	public void deathBlow(Samurai other) {
		other.health = 0;
		this.health -= (this.health/2);
		System.out.println("death blow" + Integer.toString(other.health));
	}
	public void meditate() {
		health += (this.health/2);
		System.out.println("meditate" + Integer.toString(this.health));
	}
	public static int howMany() {
		return numInstances;
		
	}

}
