# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.


def simple_interest(p, t, r):
    print ('The principal is', p)
    print ('The time period is', t)
    print ('The rate of interest is', r)

    si = (p * t * r) / 100

    print ('The Simple Interest is', si)
    return si


# Driver code
p = float(input("Please Enter the Principal Amount :"))
r = float(input("Please Enter the rate of interest:"))
t = float(input("Please Enter the time period in years :"))

simple_interest (p, t, r)