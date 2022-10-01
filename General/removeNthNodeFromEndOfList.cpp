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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* front = head;
        ListNode* end = head;
        ListNode* size = head;
        int int_size=0;
        while(size->next!=NULL){
            int_size++;
            size = size->next;
        }
        if(n > int_size){
            head = head->next;
            return head;
        }
        for (int i=0; i<n; i++){
            if(front->next != NULL){
                front = front->next;
            }
            else{return head;}
        }
        if(front==NULL){
            return head->next;
        }
        while(front->next!=NULL){
            front = front->next;
            end = end->next;
        }
        // if(end->next->next!=NULL){
        end->next = end->next->next;
        // }
        return head;
    }
};