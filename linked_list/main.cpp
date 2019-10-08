// g++ -std=c++17 reverse_linked_list.cpp
/*
Given the head of a singly linked list, reverse it in-place.
*/

#include <iostream>    // std::cout, std::endl
#include <vector>      // std::vector


struct Node {
    // Forward declarations can only be defined as pointers
    int val;
    Node* next_;
};


Node* newNode(int val) {
    Node* node = new Node;
    node->val = val;
    node->next_ = NULL;
    return node;
}


Node* build_linked_list(std::vector<int> vals) {
    // Build in reverse; insert to the front
    Node* head  = NULL;
    Node* curr_ = NULL;
    for (auto& val : vals) {
        curr_ = newNode(val);
        curr_->next_ = head;
        head = curr_;
    }
    return head;
}


void print_linked_list(Node* head) {
    std::cout << "[";
    while (head != NULL) {
        std::cout << head->val;
        head = head->next_;
        if (head != NULL)
            std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}


Node* reverse_linked_list(Node* head) {
    Node* prev_ = NULL;
    Node* curr_ = head;
    Node* next_ = NULL;
    while (curr_ != NULL) {
        next_ = curr_->next_;    // move next
        curr_->next_ = prev_;    // reverse curr
        prev_ = curr_;           // move prev
        curr_ = next_;           // move curr
    }
    head = prev_;
    return head;
}


int main() {
    std::vector<int> vals;
    Node* head;

    vals = {4, 3, 2, 1};
    head = build_linked_list(vals);
    print_linked_list(head);
    head = reverse_linked_list(head);
    print_linked_list(head);
    head = reverse_linked_list(head);
    print_linked_list(head);
    std::cout << std::endl;

    vals = {1};
    head = build_linked_list(vals);
    print_linked_list(head);
    head = reverse_linked_list(head);
    print_linked_list(head);
    std::cout << std::endl;
}
