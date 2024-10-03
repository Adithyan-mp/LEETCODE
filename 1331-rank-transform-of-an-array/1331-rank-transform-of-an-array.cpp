class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        set<int> array(arr.begin(),arr.end());
        map<int,int> rankMap;
        int rank =1;
        
        for(int elem:array){
            rankMap[elem]= rank++;
        }
        
        vector<int> ans;
        for(int elem:arr){
            ans.push_back(rankMap[elem]);
        }
        
        return ans;
    }
};