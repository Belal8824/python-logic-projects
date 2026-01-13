import numpy as np 
rng = np.random.default_rng(seed= 42)
X = rng.integers(low= 1, high= 1000, size= (200,1))
#print(X)
noise = rng.standard_normal(size=(200, 1))
#print(noise)
y = 2*X + 1 + noise
#print(y)
X_b = np.c_[np.ones((200,1)),X]
weights = np.linalg.inv(X_b.T@X_b)@X_b.T@y
#print(weights)
user_input = int(input('enter a number'))
X_new = np.array([1, user_input])
print(f'the output is: {X_new@weights}')
