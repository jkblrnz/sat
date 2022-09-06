#!/usr/bin/env python3
import z3

def main():
   s = Solver()
   x = Real('x')
   s.add(x > 5)
   s.add(x < 10)
   s.check()
   s.model()

if __name__ == '__main__':
    main()
