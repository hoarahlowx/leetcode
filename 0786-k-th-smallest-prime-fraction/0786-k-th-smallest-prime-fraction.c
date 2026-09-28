#include <stdlib.h>

int* kthSmallestPrimeFraction(int* arr, int arrSize, int k, int* returnSize) {
    double left = 0.0;
    double right = 1.0;
    
    *returnSize = 2;
    int* ans = (int*)malloc(2 * sizeof(int));
    
    while (left < right) {
        double mid = (left + right) / 2.0;
        
        int total = 0;
        int best_p = 0, best_q = 1;
        int j = 1;
        
        for (int i = 0; i < arrSize - 1; i++) {
            while (j < arrSize && arr[i] > mid * arr[j]) {
                j++;
            }
            
            if (j == arrSize) {
                break;
            }
            
            total += (arrSize - j);
            if (best_p * arr[j] < arr[i] * best_q) {
                best_p = arr[i];
                best_q = arr[j];
            }
        }
        if (total == k) {
            ans[0] = best_p;
            ans[1] = best_q;
            return ans;
        } else if (total < k) {
            left = mid;
        } else {
            right = mid;
        }
    }
    
    return ans;
}