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
        ListNode* i = head;
        ListNode* j = head;
        int tnode=1;
        while(i->next!=nullptr){
            i=i->next;
            tnode++;
        }
        if(n==tnode){
            ListNode *newhead = head->next;
            return newhead;
        }
        if(!head){
            return nullptr;
        }
        for(int k=0;k<tnode-n-1;k++){
            j=j->next;
        }

        ListNode *deltnode = j->next;
        j->next = deltnode->next;
        return head;

    }
};