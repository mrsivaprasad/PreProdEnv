import index
from exceptions import Exception
def functionName( percentage ):
    if percentage < index.test_percent :
        raise Exception("BUILD FAILED :"+str(str(percentage)+"%")+" => Required "+index.s+ "Percentage : "+str(str(index.test_percent) +"%"))
    else:
        print "BUILD SUCCESS :"+str(str(percentage)+"%")+" => Required "+index.s+" Percentage :"+str(str(index.test_percent)+"%")
        print "Tests RUN :",tests_run,"\nTests Success :",tests_success,"\nTests_Fail :",tests_fail
text_file=open("TEST-PreProdEnvTestCases.txt","r")
text_file.readline();
data= text_file.readline();
arr= data.split(" ");
indexs=[2,4];
global tests_run,test_fail,tests_success;
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
