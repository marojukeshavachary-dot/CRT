def even_odd(n: int) -> str:
   n = int(input())
   if n % 2 == 1:
      print("weird")
   else:
      if 2 <= n <= 5:
         print("not weird")
      elif 6 <= n <= 20:
         print("weird")
      else:
         print("not weird")
   return "" 


if __name__ == '__main__':
    n = int(input())
    print(even_odd(n))
