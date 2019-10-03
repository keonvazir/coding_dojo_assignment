//package com.codingdojo;
public class BankAccountTest {

	public static void main(String[] args) {
		BankAccount user = new BankAccount();
		System.out.println(user.accountNumber);
		user.depositMoney("Checking", 300);
		user.depositMoney("Savings", 300);
		user.withdraw("Savings", 50);
		System.out.println(user.getCheckingBalance());
		System.out.println(user.getSavingsBalance());
		System.out.println(BankAccount.totalMoney);
		System.out.println(user.getTotalBalances());

	}

}
