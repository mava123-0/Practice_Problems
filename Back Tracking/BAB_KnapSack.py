def branch_and_bound(weights,benefits,values,index,total_weight,curr_benefit,best_sol,tabs=""):
    curr_ub = (curr_benefit + (values[index]*total_weight))
    print(f"{tabs}Upper Bound = {curr_ub}")

    print(f"{tabs}Index {index}")
    if curr_ub < best_sol:
        return best_sol

    if(index == len(weights)-1):
        if(weights[index]<=total_weight):
            benn = curr_benefit+benefits[index]
            print(f"{tabs}Final Index can be included: {benn}")
            return max(curr_benefit+benefits[index],best_sol)
        print(f"{tabs}Final index cannot be included: {curr_benefit}")
        return max(curr_benefit,best_sol)

    # benefit with current index
    picked = 0
    if(weights[index] <= total_weight):
        best_sol = branch_and_bound(weights,benefits,values,index+1,total_weight-weights[index],curr_benefit+benefits[index],best_sol,tabs+'\t')

    # benefit without current index
    best_sol = branch_and_bound(weights,benefits,values,index+1,total_weight,curr_benefit,best_sol,tabs+'\t')

    return best_sol

def call_branch_b(weights,benefits,n):
    values = []

    for i in range(len(weights)):
        values.append(benefits[i]/weights[i])
    
    temp = values
    new_benefits = [x for _,x in sorted(zip(values,benefits))]
    new_weights = [x for _,x in sorted(zip(temp,weights))]

    return (branch_and_bound(new_weights,new_benefits,values,0,n,0,0))


def main():
    benefits = [60, 100, 120]
    weights = [10, 20, 30]
    n=50
    print("Maximum Benefit: ",call_branch_b(weights,benefits,n))

main()