def generate_hashtag(s):
    #your code here
    hashtag='#'
    if s=="" or len(s)>140:
        return False
    else:
        capitalizer=True
        for i in range(0,len(s)):
            if s[i]==' ':
                capitalizer=True
            else:
                if capitalizer:
                    hashtag+=s[i].upper()
                    capitalizer=False
                else:
                    hashtag+=s[i].lower()
                
        return hashtag
print(generate_hashtag('c i n'))