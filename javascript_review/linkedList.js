class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

function Solution(){

	this.insert=function(head,data){
        //complete this method
        const newNode = new Node(data);
        let currNode = head;
        if(currNode !== null){
            while(currNode.next !== null){
                currNode = currNode.next;
            }
            currNode.next = newNode;
        } else {
            head = newNode;
        }
        return head;
    };

	this.display=function(head){
        var start=head;
            while(start){
                process.stdout.write(start.data+" ");
                start=start.next;
            }
    };
}

const linkedList = Solution();
linkedList.insert(4);
linkedList.insert(2);
linkedList.insert(3);
linkedList.insert(4);
linkedList.insert(1);
linkedList.display();