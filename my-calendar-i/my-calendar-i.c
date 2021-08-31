
struct bst{
    struct bst* left, *right;
    int start;
    int end;
};

bool insert(struct bst* root, struct bst* node){
    if (root->end <= node->start){
        if(!root->right){
            root->right = node;
            return true;
        }
        return insert(root->right, node);
    }else if (root->start >= node->end){
        if(!root->left){
            root->left = node;
            return true;
        }
        return insert(root->left, node);
    }
    return false;
}

void freebst(struct bst* node){
    if(!node)
        return;
    freebst(node->left);
    freebst(node->right);
    free(node);
}

struct bst* newbst(int start, int end){
    struct bst* node = (struct bst*)malloc(sizeof(struct bst));
    memset(node, 0, sizeof(struct bst));
    node->start = start;
    node->end = end;
    return node;
}

typedef struct {
    struct bst* root;
} MyCalendar;


MyCalendar* myCalendarCreate() {
    MyCalendar* ret = malloc(sizeof(MyCalendar));
    ret->root = NULL;
    return ret;
}

bool myCalendarBook(MyCalendar* obj, int start, int end) {
    struct bst* node;
    bool ret;
    if(!obj->root){
        obj->root = newbst(start, end);
        return obj->root;
    }
    node = newbst(start, end);
    ret = insert(obj->root, node);
    if(!ret){
        free(node);
    }
    return ret;
}

void myCalendarFree(MyCalendar* obj) {
    freebst(obj->root);
    free(obj);
}

/**
 * Your MyCalendar struct will be instantiated and called as such:
 * MyCalendar* obj = myCalendarCreate();
 * bool param_1 = myCalendarBook(obj, start, end);
 
 * myCalendarFree(obj);
*/