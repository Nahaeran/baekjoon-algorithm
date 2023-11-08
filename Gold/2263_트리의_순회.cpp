#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> inorder, postorder, idx_list_in;

void make_preorder(int in_f, int in_e, int post_f, int post_e) {
    if (in_f > in_e || post_f > post_e) {
        return;
    }

    int root = postorder[post_e];
    int root_in_idx = idx_list_in[root];

    cout << root << " ";
    make_preorder(in_f, root_in_idx - 1, post_f, post_f + (root_in_idx - 1 - in_f));
    make_preorder(root_in_idx + 1, in_e, post_f + (root_in_idx - 1 - in_f) + 1, post_e - 1);
}

int main(){
    cin >> n;
    inorder.resize(n);
    postorder.resize(n);
    idx_list_in.resize(n + 1);
    
    for (int i = 0; i < n; i++) {
        cin >> inorder[i];
        idx_list_in[inorder[i]] = i;
    }
    for (int i = 0; i < n; i++) {
        cin >> postorder[i];
    }

    make_preorder(0, n - 1, 0, n - 1);

    return 0;
}