#ifndef CAT_HPP
#define CAT_HPP

#include "animal.hpp"
#include <iostream>

// derived class
class Cat : public Animal
{

  private:

  public:
    // polymorphic implementation of speak
    virtual void speak() {
      std::cout << "MEOW!\n";
    }

    void setWeight(double w);
    double getWeight();
};
#endif
