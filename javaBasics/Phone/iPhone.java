public class iPhone extends phone implements Ringable {
    public iPhone(String versionNumber, int batteryPercentage, String carrier, String ringTone) {
        super(versionNumber, batteryPercentage, carrier, ringTone);
    }
    @Override
    public String ring() {
    	return "iPhone" + this.getVersionNumber() + "ring!"+ this.getRingTone();
        
    }
    @Override
    public String unlock() {
    	return "finger print" + this.getCarrier();
        
    }
    @Override
    public void displayInfo() {
       System.out.println("iPhone X" + getCarrier() + getBatteryPercentage());     
    }
}