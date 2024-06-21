#include <iostream>
#include <stdexcept>

struct X {
    X() {};
    X(int x)
    : x(x) {
        std::cout << "X ctor" << std::endl;
    }

    X(const X& other) {
        x = other.x;
        std::cout << "X copy ctor" << std::endl;
    }

    int x;
};

struct Y {
    Y(X x) {
        std::cout << "Y ctor" << std::endl;
        x = x;
    }
    X x;
};

int getX(X x) {
    Y y(x);
    return y.x.x;
}

int main() {
    X x1(5);
    std::cout << getX(x1) << std::endl;
    return 0;
}
