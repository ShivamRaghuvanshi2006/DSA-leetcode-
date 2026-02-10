class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        backtrack(s, 0, 0, "", res);
        return res;
    }

    void backtrack(const string& s, int idx, int parts, string curr, vector<string>& res) {
        if (parts == 4 && idx == s.size()) {
            curr.pop_back(); // remove last '.'
            res.push_back(curr);
            return;
        }
        if (parts == 4 || idx == s.size()) return;

        for (int len = 1; len <= 3 && idx + len <= s.size(); len++) {
            string part = s.substr(idx, len);
            if ((part[0] == '0' && part.size() > 1) || stoi(part) > 255) continue;
            backtrack(s, idx + len, parts + 1, curr + part + ".", res);
        }
    }
};
