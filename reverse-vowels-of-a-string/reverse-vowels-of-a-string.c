#define isvowel(c)  ((c == 'a') || (c == 'e') || (c == 'i') || (c == 'o') \
    || (c == 'u') || (c == 'A') || (c == 'E') || (c == 'I') || (c == 'O') || (c == 'U'))

char * reverseVowels(char * s){
    int n = strlen(s);
    int left = 0, right = n - 1, tmp;
    while (left <= right){
        while (left < n && !isvowel(s[left]))
            left++;
        while (right >= 0 && !isvowel(s[right]))
            right--;
        if (left > right)
            break;
        tmp = s[left];
        s[left] = s[right];
        s[right] = tmp;
        left++;
        right--;
    }
    return s;
}