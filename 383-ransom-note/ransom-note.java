class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

        int[] count = new int[26];

        // Count characters in magazine
        for (char c : magazine.toCharArray()) {
            count[c - 'a']++;
        }

        // Use characters to construct ransomNote
        for (char c : ransomNote.toCharArray()) {
            count[c - 'a']--;

            // Not enough of this character
            if (count[c - 'a'] < 0) {
                return false;
            }
        }

        return true;
    }
}