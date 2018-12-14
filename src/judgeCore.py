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
        errorType="NA"
        errorMsg="你共輸出 "+str(len(judge_lines))+" 行"
    else:
        ok=True
        errorMsg=""
        for i,l in enumerate(right_lines):
            if l !=judge_lines[i]:
                errorMsg+=("第 "+str(i+1)+" 行<br>")
                errorMsg+=("正確答案: "+l+"<br>")
                errorMsg+=("你的答案: "+judge_lines[i]+"<br>")
                ok=False
                errorType="WA"
                break
    os.system("rm "+out)
    os.system("rm "+result)
    if ok:
        return "AC"
    else:
        return errorType+" (Msg below)<br>"+errorMsg