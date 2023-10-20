import numpy as np
def newton(f, fp, ini, tol=1e-8, max_iter=20):
    """
    Return an approximate root of a function using Newton's method.

    INPUT
        f: function whose zero is sought.
        fp: derivative of f (name from 'f prime')
        ini: initial guess
        tol: tolerance for stopping criterion. If consecutive iterates differ by less than this, it is considered convergenct.
        max_iter: maximum number of iterations
    OUTPU
        approximated zero and the number of iterations. When the maximum number of iterations is reached, the last iterate with a warning message.
    """
    x = ini
    for i in range(max_iter):
        x_pre = x
        x = x - f(x)/fp(x)

        if np.abs(x - x_pre) < tol: 
            break
    
    if i == max_iter - 1:
        print("   Warning (newton): maximum number of iteration reached.\n     --> The output may not be close enough to the zero.")
    return x, i + 1

# find the square root
f = lambda x: x*x - 2.
fp = lambda x: 2*x

x0 = 10.

appr, iter = newton(f, fp, x0, max_iter=7)
sol = np.sqrt(2.)

print("Newton's method : ", appr, f"   ({iter} iterations taken)")
print("True solution   : ", sol)
print("Error           : ", appr - sol)
#3
A = np.array([[0,5,10,15],[20,25,30,35],[40,45,50,55],[60,65,70,75]])
B = np.array([[1],[4],[9],[16]])
C = np.array([0,1,2,3])
result1 = A + B
print(result1)
result2 = A * C
print(result2)
#4
#Have to change C shape as I only define it as a 4x1 so 1D while A is 2D and still remain to be 2D after the cut. 
split_C = C[[0,3]]
result3 = A[:, [0, 3]] - split_C
print(result3)
mask = (A >=30) & (A <50)
A_mask  = A.copy()
A_mask[mask] *= -1
print(A_mask)
even_mask = A % 2 == 0
odd_mask = A % 2 != 0
A_even_or_odd = np.where(even_mask, A**2, A**3)
print(A_even_or_odd)
#5
random_array = np.random.randint(-1000000, 1000000, size=(1000, 2000))
min_entry = np.min(random_array)
min_index = np.unravel_index(np.argmin(random_array), random_array.shape)
print("Minimum Entry:", min_entry)
print("Index of Minimum Entry:", min_index)
#6
import numpy as np 
X = np.random.uniform(3, 3.5, size=(100, 20))
Y = np.random.uniform(3, 3.5, size=(100, 20))
print(X)
print(Y)
result4 = np.abs(X-Y)
print(result4)
result5 = np.max(result4)
print("Maximum error",result5)
#7
Random_array = np.random.uniform(1,21, size = 20)
print(Random_array)
Random_array[-3:] = np.nan
def filter_nan(array):
    return array[~np.isnan(array)]
filtered_array = filter_nan(Random_array)
print("Original Array:",Random_array)
print("\nFiltered Array (without nan):",filtered_array)

