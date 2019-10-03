//package com.codingdojo;
import java.util.Random;
public class BankAccount {
	public String accountNumber;
	private double checkingBalance;
	private double savingsBalance;
	public static int numberOfAccounts;
	public static double totalMoney;
	private String randomString() {
		String randomNumber = "";
		for(int i=0; i<10; i++) {
			Random r = new Random();
			randomNumber += String.valueOf(r.nextInt(9));
			
		}
		System.out.println(randomNumber);
		return randomNumber;
	}
	public BankAccount() {
		this.accountNumber = randomString();
		numberOfAccounts ++;
	}
	
	public double getCheckingBalance() {
		return this.checkingBalance;
	}
	public double getSavingsBalance() {
		return this.savingsBalance;
	}
	public void depositMoney(String accountType, double amount) {
		if(accountType == "Checking") {
			this.checkingBalance += amount;
			System.out.println("deposit into checking!");
		} else if(accountType == "Savings") {
			this.savingsBalance += amount;
			totalMoney += amount;
			System.out.println("Deposit into Savings!");
		} else {
			System.out.println("Invlaid account type :(");
		}
	}
	public void withdraw(String accountType, double amount) {
		if(amount > this.savingsBalance) {
			System.out.println("error!");
		}else {
			this.savingsBalance -= amount;
			totalMoney -= amount;
		}
		
	}
	public double getTotalBalances() {
		return this.checkingBalance + this.savingsBalance;
	}
	
}

