#include <stdio.h>


int binary_search(int target, int *array, int left, int right) {
    int middle = left + ((right-left)/2);
    int ret;

    if (right - left == 2) {
        if (array[left] == target) {
            return left;
        } else if (array[left+1] == target) {
            return left+1;
        } else {
            return -1;
        }
    }

    if (array[middle] == target) {
        return middle;
    } else if (array[middle] < target) {
        left = middle;
        ret = binary_search(target, array, left, right);
    } else {
        right = middle;
        ret = binary_search(target, array, left, right);
    }
    return ret;
}

int binary_search_w(int target, int *array, int n) {
    int left = 0;
//    int right = sizeof array / sizeof array[0];
    int right = n;
    int result = binary_search(target, array, left, right);
    return result;
}

int main() {

    int t[11] = {3,4,7,24,18,11,1,2,5,8,111,-1};

    for (int i=0; i < 11; i++) {
//        printf("%d", t[i]);
    }
    int result = binary_search_w(111, t, 12);
    printf("%d", result);
    return 1;
}
