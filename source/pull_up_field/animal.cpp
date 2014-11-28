#include <iostream>
#include <vector>
using namespace std;

// abstract base class
class Animal
{
public:
    // pure virtual method
    virtual void speak() = 0;

    void die() { 
      cout << "I died\n";
    }

    // virtual destructor
    virtual ~Animal() {}
};

// derived class
class Dog : public Animal
{
public:
    // polymorphic implementation of speak
    virtual void speak() { cout << "Ruff!"; }
};

int main( int argc, char* args[] ) {

    Animal* a = new Dog();

    // invoke the speak method of the first Animal in the container
    a->speak();
    a->die();

    return 0;
}
