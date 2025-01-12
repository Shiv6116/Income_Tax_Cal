package Variables;

import java.util.Scanner;

public class IncomeTax_cal {

    public static void main(String[] args) {
        // Create scanner object to take input
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter their income
        System.out.println("Enter your Income:");
        int income = input.nextInt();

        // Variable to store the calculated tax
        int tax = 0;

        // Income tax slabs
        if (income <= 250000) {
            tax = 0; // No tax for income up to 2.5 lakh
        }
        else if (income >= 250001 && income <= 500000) {
            tax = (int) (income * 0.05); // 5% tax for income between 2.5 lakh to 5 lakh
        }
        else if (income >= 500001 && income <= 1000000) {
            tax = (int) (income * 0.20); // 20% tax for income between 5 lakh to 10 lakh
        }
        else {
            tax = (int) (income * 0.30); // 30% tax for income above 10 lakh
        }

        // Output the calculated tax
        System.out.println("Tax is: " + tax);
    }
}
