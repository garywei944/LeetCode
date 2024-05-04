class Solution {
   public:
    string simplifyPath(string path) {
        vector<string> tokens;
        string token;
        istringstream tokenStream(path);

        while (getline(tokenStream, token, '/')) {
            // cout << token << endl;
            if (token == "")
                continue;
            else if (token == "..") {
                if (!tokens.empty()) tokens.pop_back();
            } else if (token == ".")
                ;
            else
                tokens.push_back(token);
        }

        if (tokens.size() == 0) return "/";

        string ans;
        for (auto e : tokens) {
            ans += '/' + e;
        }
        return ans;
    }
};
