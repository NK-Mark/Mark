def encrypt_cis(msg,key): #암호화
    ans = ''
    dic = 'abcdefghijklmnopqrstuvwxyz'
    
    for m in msg:
        index = dic.find(m) #dic에서 해당 문자가 몇번째 문자인지 찾아준다.
        if(index ==  -1):	#공백일 경우 ( =띄어쓰기 )
            ans = ans + m
        else:
            index = index + key  # key만큼 뒤로 이동
            index = index % len(dic) # index길이를 초과하지 않도록 방지한다.
            ans = ans + dic[index]
            
    return ans
              
        

def decrypt_cis(enc_msg,key): #복호화
    ans = ''
    dic = 'abcdefghijklmnopqrstuvwxyz'
    
    for m in enc_msg:
        index = dic.find(m)
        if(index ==  -1):
            ans = ans + m
        else:
            index = index - key # key만큼 앞으로 이동
            index = index % len(dic)
            ans = ans + dic[index]
            
    return ans


def main():
    msg = 'Saved World'
    key = 1
    
    enc_msg = encrypt_cis(msg, key)
    print(enc_msg)
    
    dec_msg = decrypt_cis(enc_msg, key)
    print(dec_msg)

main()
