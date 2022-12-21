#include <iostream>
#include <stdexcept>

struct BadRequest : public std::runtime_error {
    BadRequest(const std::string& msg) : std::runtime_error(msg) {}
};

int main() {
    try {
        throw BadRequest("hellobello");
    } catch (BadRequest& e) {
        std::cout << "BadRequest caught: " << e.what() << std::endl;
    } catch (std::exception& e) {
        std::cout << "Exception caught: " << e.what() << std::endl;
    }
    return 0;
}
