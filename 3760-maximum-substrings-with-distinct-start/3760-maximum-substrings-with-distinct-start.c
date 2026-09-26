int maxDistinct(char* s) {
    int size = 1;
    int *set = (int*)malloc(size * sizeof(int));
    set[0] = s[0];
    for (int i = 1; s[i] != '\0'; i++) {
        int f = 0;
        for (int j = 0; j < size; j++) {
            if (s[i] == set[j]) {
                f = 1;
                break;
            }
        }
        if (f == 0) {
            size++;
            set = (int*)realloc(set, size * sizeof(int));
            set[size - 1] = s[i];
        }
    }
    free(set);
    return size;
}