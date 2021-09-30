#include <iostream>

#include "library.hpp"

// Pet
Pet::Pet(const std::string &name): name(name) {}

void Pet::setName(const std::string &name) {
    this->name = name;
}

const std::string &Pet::getName() const {
    return name;
}

void Pet::die(int kek, float lol) const {
    std::cout << "kek";
}

// Dog
Dog::Dog(const std::string &name): Pet(name) {}

std::string Dog::bark() const {
    return "woof!";
}
