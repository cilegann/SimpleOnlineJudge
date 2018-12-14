def judgeCpp(question,fn):
    import os
    cpp='./submitted/'+fn+'.cpp'
    data='./data/'+question+"_data.txt"
    ans='./data/'+question+"_ans.txt"
    out='./tmp/'+fn+'.out'
    result='./tmp/'+fn+"_result.txt"
    cmd1="g++ "+cpp+" -o "+out
    cmd2=out+" <"+data+" >"+result
    os.system(cmd1)
    os.system(cmd2)
    with open(ans,'r') as right:
        with open(result,'r') as judge:
            right_lines=right.readlines()
            judge_lines=judge.readlines()
    if len(right_lines)!=len(judge_lines):
        ok=False
    else:
        ok=True
        for i,l in enumerate(right_lines):
            if l !=judge_lines[i]:
                print("Line NO."+str(i+1))
                print("Ans: "+l)
                print("Your ans: "+judge_lines[i])
                ok=False
                break
    os.system("rm "+out)
    os.system("rm "+result)
    if ok:
        print(fn+" AC")
        return "AC"
    else:
        print(fn+" WA")
        return "WA"