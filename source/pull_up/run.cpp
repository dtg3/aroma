#include "cat.hpp"
#include "dog.hpp"
#include <iostream>

int main( int argc, char* args[] ) {

  Animal* a = new Dog();
  Animal* b = new Cat();

  // invoke the speak method of the first Animal in the container
  a->speak();
  b->speak();

  Dog d;
  d.setWeight(10.0);
  std::cout << d.getWeight() << "\n";

  return 0;
}