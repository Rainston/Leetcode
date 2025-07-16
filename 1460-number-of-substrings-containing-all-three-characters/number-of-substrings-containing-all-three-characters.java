class Solution {
    public int numberOfSubstrings(String s) {
        int n = s.length();
        int[] lastseen = new int[3];
        // Initialize to -1
        lastseen[0] = -1;
        lastseen[1] = -1;
        lastseen[2] = -1;
        int count = 0;

        for (int i = 0; i < n; i++) {
            lastseen[s.charAt(i) - 'a'] = i;
            if (lastseen[0] != -1 && lastseen[1] != -1 && lastseen[2] != -1) {
                int minLast = Math.min(lastseen[0], Math.min(lastseen[1], lastseen[2]));
                count += minLast + 1;
            }
        }
        return count;
    }
}
