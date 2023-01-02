def solution(score,index,mem,tabs=""):
    print(f"{tabs}Index {index}")

    if(index > len(score)-1):
        # print(f"{tabs}Out of bounds")
        return 0
    # if(index == len(score)-1):
    #     return 
    if(mem[index]!=-1):
        # print(f"{tabs}Memoized")
        return mem[index]

    pick = score[index] + solution(score,(index+1)+(index+1)+1,mem,tabs+'\t')
    print(f"When song {index} is picked: {pick}")
    notpicked = 0 + solution(score,index+1,mem,tabs+'\t')
    print(f"When song {index} is not picked: {notpicked}")

    # print(f"{tabs}index {index} ,pick {pick}, notpicked {notpicked}")

    if(max(pick,notpicked) == pick):
        print(f"{tabs}Song {score[index]} is chosen")
    else:
        print(f"{tabs}Song {score[index]} is not chosen")

    mem[index] = max(pick,notpicked)

    return max(pick,notpicked)

def main():
    score = [1,28,31,166,5]
    mem = [-1 for i in range(len(score))]
    print ("\nThe max score is: ",solution(score,0,mem))

if __name__ == '__main__':
    main()