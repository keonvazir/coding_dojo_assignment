public class FizzBuzz {
    public String fizzBuzz(int number) {
        // int divideThree;
        // int divideFive;
        if(number%3==0 && number%5==0){
            return "Fizz Buzz";
        }
        else if(number%3 == 0){
            return "Fizz";
        }
        else if(number%5 == 0){
            return "Buzz";
        }
        else {
            return String.valueOf(number);
            // return Integer.toString(number)
        }
    }
}