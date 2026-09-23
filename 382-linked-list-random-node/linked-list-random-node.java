import java.util.*;

class Solution {

    private ListNode head;
    private Random random;

    public Solution(ListNode head) {
        this.head = head;
        this.random = new Random();
    }
    
    public int getRandom() {
        int length = 0;
        ListNode current = head;

        // Find length
        while (current != null) {
            length++;
            current = current.next;
        }

        // Pick random index [0, length - 1]
        int randomIndex = random.nextInt(length);

        // Move to that index
        current = head;

        for (int i = 0; i < randomIndex; i++) {
            current = current.next;
        }

        return current.val;
    }
}