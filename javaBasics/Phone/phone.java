
public abstract class phone {
	    private String versionNumber;
	    private int batteryPercentage;
	    private String carrier;
	    private String ringTone;
	    public phone(String versionNumber, int batteryPercentage, String carrier, String ringTone){
	        this.versionNumber = versionNumber;
	        this.batteryPercentage = batteryPercentage;
	        this.carrier = carrier;
	        this.ringTone = ringTone;
	    }
	    // abstract method. This method will be implemented by the subclasses
	    public abstract void displayInfo();
	    public String getVersionNumber() {
	    	return versionNumber;
	}
	    public int getBatteryPercentage() {
	    	return batteryPercentage;
	    }
	    public void setBatteryPercentage(int number) {
	    	batteryPercentage= number;
	    }
	    public String getCarrier() {
	    	return carrier;
	    }
	    public void setCarrier(String carrier) {
	    	this.carrier = carrier;
	    }
	    public String getRingTone() {
	    	return ringTone;
	    }
	    public void setRingTone(String ringTone) {
	    	this.ringTone = ringTone;
	    }
}
