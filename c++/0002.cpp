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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        auto head = new ListNode(0);
        auto tail = head;
        int carry = 0;

        while (l1 || l2 || carry) {
            carry += ((l1 ? l1->val : 0) + (l2 ? l2->val : 0));
            tail->next = new ListNode(carry % 10);
            carry /= 10;
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
            tail = tail->next;
        }

        return head->next;
    }
};
