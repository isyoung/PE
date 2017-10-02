#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iterator>


using namespace std;


//simplify and get trid of templates.
template<typename S>
void split(string &line, char delimiter, S func){
    stringstream stream;
    stream.str(line);
    string insert;
    while(getline(stream, insert, delimiter)){
        for(int i = 0; i < insert.length(); i++){
            if(ispunct(insert[i])){
                insert.erase(insert.find(insert[i]));
            }
        }
        *(func++) = insert;
    }
}

set<string> set_split(string &line, char delimiter){
    vector<string> dic;
    split(line, delimiter, back_inserter(dic));
    set<string> l_set(dic.begin(), dic.end());
    return l_set;
}
vector<string> v_split(string &line, char delimiter){
    vector<string> dic;
    split(line, delimiter, back_inserter(dic));
    return dic;
}


int main(int argc, char *argv[]) {

    string command = "1Nephi";
    string line = "";
    string hold = "";

    fstream inFile;
    ofstream outFile, v_outFile, mFile;

    inFile.open(command + ".txt");
    outFile.open(command + "_set.txt");
    v_outFile.open(command + "_vec.txt");
    mFile.open(command + "_1_1.txt");

    vector<string> lang, lang2;
    set<string> s1, s2;


    cout << "Enter argument: ";

    while (!inFile.eof() && inFile) {
        getline(inFile, line);
        lang2 = v_split(line, ' ');
        lang.insert(lang.end(), lang2.begin(), lang2.end());
        transform(line.begin(), line.end(), line.begin(), ::tolower);
        s2 = set_split(line, ' ');
        s1.insert(s2.begin(), s2.end());
    }

    copy(lang.begin(), lang.end(), ostream_iterator<string>(v_outFile, "\n"));

    copy(s1.rbegin(), s1.rend(), ostream_iterator<string>(outFile, "\n"));

    ostream &flush();

    map<string, string> wMap;
    string last = "";
    vector<string>::const_iterator it;
    for (it = lang.begin(); it != lang.end(); it++) {
        wMap[last] = *it;
        last = *it;
    }

    for (auto &wr: wMap) { mFile << wr.first << ", " << wr.second << "\n"; }

    outFile.close();
    v_outFile.close();
    mFile.close();

    string state = "";

    for (int i = 0; i < 100; i++) {
        cout << wMap[state] << " ";
        state = wMap[state];
    }
    cout << endl << endl;
    map<string, vector<string> > vMap;
    state = "";
    srand(time(NULL));

    for (auto iter = lang.begin(); iter != lang.end(); iter++) {
        vMap[state].push_back(*iter);
        state = *iter;
    }
    state = "";
    for (int i = 0; i < 100; i++) {
        int seed = rand() % vMap[state].size();
        cout << vMap[state][seed] << " ";
        state = vMap[state][seed];
    }
    cout << endl;

    int M = 2;
    map<vector<string>, vector<string>> v_Map;
    vector<string> vState;
    for (int i = 0; i < M; i++){
        vState.push_back("");
    }
    for(vector<string>::iterator iter = lang.begin(); iter != lang.end(); iter++){
        v_Map[vState].push_back(*iter);
        vState.push_back(*iter);
        vState.erase(vState.begin() + 1);
    }
    for(int i = 0; i < 100 ; i++){
        int seed = rand() % v_Map[vState].size();
        cout << v_Map[vState][seed] << " ";
        vState.push_back(v_Map[vState][seed]);
        vState.erase(vState.begin() + 1);
    }
    return 0;
}