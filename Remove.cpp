class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL  ||  head->next==NULL) return head;

        ListNode*prev=NULL;
        ListNode*temp=NULL;
        ListNode*curr=head;

        while(curr!=NULL){
            if(prev==NULL){
                prev=curr;
                temp=prev;
                curr=curr->next;
                continue;
            }
            if(curr->val == prev->val){
                curr=curr->next;
                if(curr==NULL) prev->next=NULL;
            }
            else{
                prev->next=curr;
                prev=curr;
                curr=curr->next;
            }
        }
        return temp;
    }
};