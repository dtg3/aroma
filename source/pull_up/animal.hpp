#ifndef ANIMAL_HPP
#define ANIMAL_HPP

// abstract base class
class Animal
{
  protected:
  double weight;

  public:
    // pure virtual method
    virtual void speak() = 0;
};
#endif
