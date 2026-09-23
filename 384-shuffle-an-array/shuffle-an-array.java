import java.util.*;

class Solution {

    private int[] original;
    private Random random;

    public Solution(int[] nums) {
        original = nums.clone();
        random = new Random();
    }
    
    public int[] reset() {
        return original.clone();
    }
    
    public int[] shuffle() {
        int[] arr = original.clone();

        // Fisher-Yates Shuffle
        for (int i = arr.length - 1; i > 0; i--) {
            int j = random.nextInt(i + 1);

            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }

        return arr;
    }
}