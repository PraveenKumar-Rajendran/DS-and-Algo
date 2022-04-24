int reverse(int x){
    int reverse = 0;
    long temp = 0;
    int last_digit = 0;

    
    while(x != 0){
        last_digit = x % 10;
        temp = temp*10 + last_digit;
        x /= 10;
    }
    
    return (((int)temp) == temp) ? temp : 0;

}