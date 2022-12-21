#include <iostream>

extern "C" int add(int a, int b) {
    return a + b;
}

extern "C" int subtract(int a, int b) {
    return a - b;
}