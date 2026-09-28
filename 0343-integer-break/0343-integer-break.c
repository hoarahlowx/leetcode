int power(int base, int exp) {
    int res = 1;
    for (int i = 0; i < exp; i++) {
        res *= base;
    }
    return res;
}

int integerBreak(int n) {
    if (n == 2) return 1;
    if (n == 3) return 2;

    if (n % 3 == 0) {
        return power(3, n / 3);
    }
    
    if (n % 3 == 1) {
        return power(3, (n / 3) - 1) * 4;
    }
    
    return power(3, n / 3) * 2;
}