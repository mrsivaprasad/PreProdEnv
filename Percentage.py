import os
#This file generates the test percentage ratio of TEST_CASES.
def functionName( percentage ):
    if percentage < 40.0:
        raise Exception("BUILD FAILED :" +str(percentage))

text_file=open("TEST-TestEnvTestCases.txt","r")
text_file.readline();
data= text_file.readline();
arr= data.split(" ");
indexs=[2,4];
tests_data=[];
for i in indexs:
    f=list(arr[i]);
    f.pop();
    s=''.join(f);
    tests_data.append(int(s));
tests_run=int(tests_data[0]);
tests_fail=int(tests_data[1]);
tests_success=tests_run-tests_fail;
tests_data.append(tests_success);
tests_perc=(float(tests_success)/(tests_run))*100.00;
tests_data.append(tests_perc);
functionName(tests_data[-1]);
text_file.close()
