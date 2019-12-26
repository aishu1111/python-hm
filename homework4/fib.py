def fib_rabbits(n,k):
    rabbits = [0,1]
    for i in xrange(n-1):
        rabbits[i % 2] = rabbits[(i-1) % 2] + k*rabbits[i % 2]

    return rabbits[n % 2]


with open('rosalind_fib.txt') as input_data:
    n, k = map(int, input_data.read().strip().split())

rabbits = str(fib_rabbits(n,k))

print rabbits
with open('result.txt', 'w') as output_data:
    output_data.write(rabbits)