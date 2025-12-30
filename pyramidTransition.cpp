class Solution {
public:
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        // pair "AB" -> list of possible tops {'C','D',...}
        unordered_map<string, vector<char>> tops;
        for (const string& a : allowed) {
            tops[a.substr(0, 2)].push_back(a[2]);
        }

        // memo[row] = Can this row lead to the top?
        unordered_map<string, bool> memo;

        function<bool(const string&)> canBuild = [&](const string& row) -> bool {
            if (row.size() == 1) return true;
            auto itMemo = memo.find(row);
            if (itMemo != memo.end()) return itMemo->second;

            // Early prune: if any adjacent pair has no possible top, impossible
            for (int i = 0; i + 1 < (int)row.size(); i++) {
                string key = row.substr(i, 2);
                if (!tops.count(key)) return memo[row] = false;
            }

            string next;
            next.reserve(row.size() - 1);

            function<bool(int)> buildNext = [&](int idx) -> bool {
                if (idx == (int)row.size() - 1) {
                    return canBuild(next);
                }

                string key = row.substr(idx, 2);
                auto it = tops.find(key);
                if (it == tops.end()) return false;

                for (char c : it->second) {
                    next.push_back(c);
                    if (buildNext(idx + 1)) return true;
                    next.pop_back();
                }
                return false;
            };

            return memo[row] = buildNext(0);
        };

        return canBuild(bottom);
    }
};
