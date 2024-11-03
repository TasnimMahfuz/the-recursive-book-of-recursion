#include <bits/stdc++.h>
using namespace std;

#define START 0
#define IN_THE_CALL 1

int ans = -1;

int main()
{

    int lookupNum; cin >> lookupNum;


    stack< map<string, int>> callStack;


    map<string, int> initialFrame;
    initialFrame["returnAddr"] = START;
    initialFrame["number"] = lookupNum;

    callStack.push(initialFrame);

    while(callStack.empty() == false)
    {
        int top_num = callStack.top().at("number");
        int top_return_addr = callStack.top().at("returnAddr");

        if(top_return_addr == START)
        {

            //nije processing e dhuke geche, eta janiye rakhi
            callStack.top()["returnAddr"] = IN_THE_CALL;

            //is it the base case?
            if(top_num == 1){
                //then return, not adding any new function-call to the call Stack.
                ans = 1;
                callStack.pop();
                continue;

            }else{

                //arekta call mane arekta frame add kora ar ki!
                map<string, int> function_call_frame;
                function_call_frame["returnAddr"] = START;
                function_call_frame["number"] = top_num - 1;

                callStack.push(function_call_frame);

            }


        }else if(top_return_addr == IN_THE_CALL)
        {
            ans *= top_num;
            callStack.pop();
        }

    }

    cout<< ans <<endl;

}
