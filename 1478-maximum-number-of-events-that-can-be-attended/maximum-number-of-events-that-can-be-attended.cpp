class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(),events.end());
        int pos=0;
        int time=1;
        int attended =0;
        int n=events.size();
        priority_queue<int,vector<int>,greater<int>> minheap;
        while(pos<n or !minheap.empty()){
            //To skip time
            if(minheap.empty())
                time=max(time,events[pos][0]);
            
            //To add events 
            while(pos<n and events[pos][0]==time){
                minheap.push(events[pos][1]);
                pos++;
            }
            //To pop unattended events
            while(!minheap.empty() and minheap.top()<time){
                minheap.pop();
            }
            if(!minheap.empty()){
                minheap.pop();
                attended++;
            }
            time++;
        }
        return attended;
    }
};