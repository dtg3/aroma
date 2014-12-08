#ifndef DOG_HPP
#define DOG_HPP

#include "animal.hpp"
#include <iostream>

// derived class
class Dog : public Animal
{
  private:

  public:
    // polymorphic implementation of speak
    virtual void speak() {
      std::cout << "WOOF!\n";
    }

    void setWeight(double w);
    double getWeight();
};
#endif
