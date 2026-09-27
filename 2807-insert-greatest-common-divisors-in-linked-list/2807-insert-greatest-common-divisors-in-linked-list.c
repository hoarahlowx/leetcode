int gcd(int a, int b){
    int c = 1;
    int ans = 1;
    while (c <= a && c <= b){
        if (a % c == 0 && b % c == 0){
            ans = c;
        }
        c++;
    }
    return ans;
}


struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) {
    struct ListNode* curr = head;

    while (curr != NULL && curr->next != NULL) {
        int a = curr->val;
        int b = curr->next->val;
        int gcdValue = gcd(a, b);
        
        struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = gcdValue;
        newNode->next = curr->next;
        curr->next = newNode;
        
        curr = newNode->next;
    }
    
    return head;
}