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
    ListNode* removeNodes(ListNode* head) {
        stack<int> st;

        while(head){
            while(!st.empty() && head->val > st.top()){
                st.pop();
            }
            st.push(head->val);
            head = head->next;
        }

        ListNode* node = nullptr;
        while(!st.empty()){
            ListNode* new_node = new ListNode(st.top(), node);
            node = new_node;
            st.pop();
        }
        
        return node;
    }
};