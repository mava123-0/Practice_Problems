class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
        for x in sentence:
            if(x in alpha_list):
                alpha_list.pop(alpha_list.index(x))
        if(len(alpha_list)==0):
            return True
        return False