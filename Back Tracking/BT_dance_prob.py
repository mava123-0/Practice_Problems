def solution(score,index,tabs):
    # print(f"{tabs}index {index}")

    if(index > len(score)-1):
        # print(f"{tabs}Out of bounds")
        return 0

    # new condition

    pick = score[index] + solution(score,(index+1)+(index+1)+1,tabs+'\t',)
    print(f"{tabs}When the song {index} is picked:",pick)
    notpicked = 0 + solution(score,index+1,tabs+'\t')
    print(f"{tabs}When the song {index} is not picked:",notpicked)

    if(max(pick,notpicked) == pick):
        print(f"{tabs}{score[index]} is chosen")
    else:
        print(f"{tabs}{score[index]} is not chosen")

    return max(pick,notpicked)

def main():
    score = [1,28,31,166,5]
    # ans 167
    print ("\nThe max score is: ",solution(score,0,""))

if __name__ == '__main__':
    main()