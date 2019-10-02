public class Wizard extends Human{
	public int health, intelligence;
	public Wizard() {
		this.health = 50;
		this.intelligence = 8;
	}
	public void heal(Samurai other) {
		other.health += this.intelligence;
		System.out.println("heal" + Integer.toString(other.health));
	}
	public void fireball(Samurai other) {
		other.health -= this.intelligence *3;
		System.out.println("fireball" + Integer.toString(other.health));
	}
	
}
