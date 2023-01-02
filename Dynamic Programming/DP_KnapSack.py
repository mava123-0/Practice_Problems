def solution(weights,benefits,index,n,tabs,mem):
    print(f"{tabs}Index {index}")

    if(index<0 or n==0):
        return 0
    if(weights[index]>n):
        return 0
    if(mem[index]!=-1):
        return mem[index]

    k_included = benefits[index] + solution(weights,benefits,index-1,n-weights[index],tabs+'\t',mem)
    print(f"{tabs}Index {index} included, total benefit is {k_included}")
    k_excluded = solution(weights,benefits,index-1,n,tabs+'\t',mem)
    print(f"{tabs}Index {index} not included, total benefit is {k_excluded}")

    if(max(k_excluded,k_included) == k_included):
        print(f"{tabs}Index {index} is chosen")
    if(max(k_excluded,k_included) == k_excluded):
        print(f"{tabs}Index {index} is not chosen")

    mem[index] = max(k_included,k_excluded)
    return max(k_included,k_excluded)

def main():
    benefits = [60, 100, 120]
    weights = [10, 20, 30]
    n = 50

    mem = [-1 for i in range(len(weights))]
    print("\nMaximum Benefit is:",solution(weights,benefits,len(weights)-1,n,"",mem))

if __name__ == '__main__':
    main()