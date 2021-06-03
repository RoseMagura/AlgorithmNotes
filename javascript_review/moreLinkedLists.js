class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class Solution {
    constructor() {

        this.removeDuplicates = function (head) {
            let currNode = head;
            let prevNode = head;
            const alreadyUsed = new Set([head.data]);

            while (currNode) {
                if (alreadyUsed.has(currNode.data)) {
                    while (currNode.next && currNode.data === currNode.next.data) {
                        currNode = currNode.next;
                    }
                    prevNode.next = currNode.next; // skip current node
                } else {
                    prevNode.next = currNode;
                    alreadyUsed.add(currNode.data);
                }
                prevNode = currNode;
                currNode = currNode.next;
            }
            return head;
        };

        this.insert = function (head, data) {
            const p = new Node(data);
            if (head == null) {
                head = p;
            }
            else if (head.next == null) {
                head.next = p;
            }
            else {
                let start = head;
                while (start.next != null) {
                    start = start.next;
                }
                start.next = p;
            }
            return head;

        };

        this.display = function (head) {
            let start = head;
            while (start) {
                process.stdout.write(start.data + " ");
                start = start.next;
            }
        };
    }
}

// const values = [1, 2, 2, 3, 3, 4];
const values = [1, 1, 1, 1, 1, 1, 1];
let head = null;
const myList = new Solution();

for (let i = 0; i < values.length; i++) {
    head = myList.insert(head, values[i]);
}

head = myList.removeDuplicates(head);
myList.display(head);
