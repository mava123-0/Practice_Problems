/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        int size = 0;
        ListNode* temp = head;
        while(temp!=NULL){
            size++;
            temp = temp->next;
        }
        
        if(size<2){
            head = head->next;
            return head;
        }
        
        int n = (size/2)-1;
        
        ListNode* index = head;
        while(n>0){
            index = index->next;
            n--;
        }
        
        index->next = index->next->next;
        
        return head;
    }
};