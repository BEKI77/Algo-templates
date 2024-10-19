class ModularArithmetic:
    def add(self, a, b, p):
        return ((a % p) + (b % p)) % p
    def subtract(self, a, b, p):
        return ((a % p) - (b % p)) % p
    def multiply(self, a, b, p):
        return ((a % p) * (b % p)) % p

    def binary_exponentiation(self, base, exponent, p):
        result = 1
        while exponent > 0:
            if exponent & 1:
                result = self.multiply(base, result, p)
            base = self.multiply(base, base, p)
            exponent >>= 1
        
        return result

    def inverse(self, a, p):
        return self.binary_exponentiation(a, p - 2, p)

    def division(self, a, b, p):
        return self.multiply(a, self.inverse(b, p), p)
