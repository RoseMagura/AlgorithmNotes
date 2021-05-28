// Start of function Node
function Node(data) {
    this.data = data;
    this.left = null;
    this.right = null;
}; // End of function Node

// Start of function BinarySearchTree
function BinarySearchTree() {
    this.insert = function(root, data) {
        if (root === null) {
            this.root = new Node(data);
            
            return this.root;
        }
        
        if (data <= root.data) {
            if (root.left) {
                this.insert(root.left, data);
            } else {
                root.left = new Node(data);
            }
        } else {
            if (root.right) {
                this.insert(root.right, data);
            } else {
                root.right = new Node(data);
            }
        }
        
        return this.root;
    };
    
    // Start of function getHeight
    this.getHeight = function(root) {
        // Add your code here
        let max = 0;
        let count = 0;
        const traverse = (currNode, count) => {
            if(currNode){
                count++;
                if(currNode.left === null && currNode.right === null){
                    if(count - 1 > max){
                        max = count - 1;
                    }
                    count = 0;
                    return max;
                }
                traverse(currNode.left, count);
                traverse(currNode.right, count);
            }
        }

        traverse(root, count);
        return max;
    }; // End of function getHeight
}; // End of function BinarySearchTree

const tree = new BinarySearchTree();
let root = null;

// const values = _input.split('\n').map(Number);

const values = [7, 3, 5, 2, 1, 4, 6, 7];
for (var i = 1; i < values.length; i++) {
    root = tree.insert(root, values[i]);
}

console.log(tree.getHeight(root));