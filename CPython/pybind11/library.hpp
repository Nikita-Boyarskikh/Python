#pragma once

#include <string>

class Pet {
    private:
        std::string name;

    public:
        Pet(const std::string &name);
        void setName(const std::string &name);
        const std::string &getName() const;
        virtual void die(int kek, float lol) const;
};

class Dog: public Pet {
    public:
        Dog(const std::string &name);
        std::string bark() const;

        std::string type;
};
