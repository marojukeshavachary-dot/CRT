def number_triangle(n: int) -> str:
    rows=[]
    for i in range(1,n+1):
        row_string="".join(str(j) for j in range(1,i+1))
        rows.append(row_string)
    return "\n".join(rows)    


if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))