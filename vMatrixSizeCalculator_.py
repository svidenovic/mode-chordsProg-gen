
def is_prime_(n):
    if n == 2:
        return True;
    if n % 2 == 0 or n <= 1:
        return False;
    sqr = int(n**0.5) +1;
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False;
    return True;

def get_factors_(n):
	factors = set();
	for x in range(2, int(n**0.5) + 1):
		if n % x == 0:
			factors.add(x)
			factors.add(n//x)
	return sorted(factors);

def gen_MatrixSize( ilen ):
	cols = 0; rows = 0;
	min_diff = ilen;
	if is_prime_(ilen):
		ilen += 1;
	factors = get_factors_(ilen);
	for fac1 in factors:
		for fac2 in factors:
			if fac1*fac2 == ilen:
				if abs(fac1-fac2) < min_diff:
					min_diff = abs(fac1-fac2);
					cols = fac2; rows = fac1;
	return [cols,rows];

