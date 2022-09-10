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
    ListNode* middleNode(ListNode* head) {
        if(not head or not head->next){
            return head;
        }
        int size=1;
        ListNode *head1=head;
        while(head1->next){
            head1=head1->next;
            size+=1;
        }
        int value=0;
        value=int(size/2);
        while (value>0){
            value--;
            head=head->next;
        }
        return head;
    }
};