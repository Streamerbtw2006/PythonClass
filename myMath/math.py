from myMath import Geometric
from myMath import Arithmatic

class Mathematic:

    def __init__(self, arithmatic = Arithmatic(), geometric = Geometric()):
        self._arithmatic = arithmatic
        self._geometrics = geometric

    @property
    def arithmatic(self):
        return self._arithmatic

    @property
    def geometric(self):
        return self._geometrics

    def Add(self, x, y):
        result = self.arithmatic.Addition(x, y)
        print('Sum of two numbers: ' + str(result))
           
    def Multiply(self, x, y):
        result = self.geometric.Multiplication(x, y)
        print('Multiplication of two numbers: ' + str(result))
        
    def Subtraction(self, x, y):
        result = self.arithmatic.Subtraction(x, y)
        print('Difference of two numbers: ' + str(result))
        
    def Division(self, x, y):
        result = self.geometric.Division(x, y)
        print('Quotient of two numbers: ' + str(result))

   
