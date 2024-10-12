
# number using Fast Doubling Method 
MOD = 1000000007


def FastDoubling(n, res): 
	
	# Base Condition 
	if (n == 0): 
		res[0] = 0
		res[1] = 1
		return
		
	FastDoubling((n // 2), res) 

	# Here a = F(n) 
	a = res[0] 

	# Here b = F(n+1) 
	b = res[1] 

	c = 2 * b - a 

	if (c < 0): 
		c += MOD 

	# As F(2n) = F(n)[2F(n+1) – F(n)] 
	# Here c = F(2n) 
	c = (a * c) % MOD 

	# As F(2n + 1) = F(n)^2 + F(n+1)^2 
	# Here d = F(2n + 1) 
	d = (a * a + b * b) % MOD 

	# Check if N is odd or even
	
	if (n % 2 == 0): 
		res[0] = c 
		res[1] = d 
	else : 
		res[0] = d 
		res[1] = c + d 
	
# Driver code 
N = 6
res = [0] * 2

FastDoubling(N, res) 

print(res[0]) 
	
# This code is contributed by Pratham Jain
