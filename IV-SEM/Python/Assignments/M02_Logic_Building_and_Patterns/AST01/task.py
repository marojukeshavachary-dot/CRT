def count_digits(n: int) -> int:
    count_digits=0
    n=abs(n)
    if n==0:
        return 1
    while n>0:
        n//=10
        count_digits+=1
    return count_digits     

if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))