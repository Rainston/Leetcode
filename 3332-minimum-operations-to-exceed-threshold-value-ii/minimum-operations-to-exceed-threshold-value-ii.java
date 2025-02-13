import java.util.PriorityQueue;
class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> minheap = new PriorityQueue<>();
        for(int i:nums){
           minheap.add((long) i);
        }
        int count=0;
        while(!minheap.isEmpty()){
            long min1 =minheap.poll();
            if (min1>=k){
                break;
            }
            long min2 =minheap.poll();
            minheap.add(2*Math.min(min1,min2)+Math.max(min1,min2));
            count++;
        }
        return count;
    }
}