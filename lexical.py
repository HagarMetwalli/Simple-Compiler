import string
with open('lexical_file.txt','r') as f_open:
    data = f_open.read()
a=[]
a=data.split()
i=0
while i< len(a) :
      if a[i] == '/*':
          a.remove(a[i])

          while a[i] != '*/':
              a.remove(a[i])
          a.remove(a[i])

      i = i + 1
print(a)




white_spaces=['\t','\n',' ','endl']
operators=['+','-','*','/','%','^','++','--','+=','-=','*=','/=','%=',"="]
Relational_Operators=['<','>','==','!=','<=','>=']
conditional_Logical_Operators=['&&','||']
Logical_Operators=['&','|','!','<<','>>']
delim=[';',',','(',')','[',']','{','}','<','>','#','"',":"]
predirect=["include","define",'iostream']
keywords=['const','true','false','string','break','continue','bool',
          'void',"main","struct","for","if","else","return","while","do",'using','namespace',
          'std','int','float','long','double','char','bool','short','cout','cin']
Num=['0','1','2','3','4','5','6','8','7','8','9']
identefire=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



y=[]
flag_keywords=0
flag_operators=0
flag_Num=0
flag_Relational_Operators=0
flag_identefire=0
flag_predirect=0
flag_delim=0
flag_Logical_Operators=0
flag_conditional_Logical_Operators=0
flag_Relational_Operators=0
flag_white_spaces=0

for i in range (0,len(a)):
    flag_keywords = 0
    flag_operators = 0
    flag_Num = 0
    flag_Relational_Operators = 0
    flag_identefire = 0
    flag_predirect = 0
    flag_delim = 0
    flag_Logical_Operators = 0
    flag_conditional_Logical_Operators = 0
    flag_Relational_Operators = 0
    flag_white_spaces = 0

    for j in range (0, len(keywords)):
       if( a[i]==keywords[j]):
           flag_keywords=1
           y.append("keyword")
           break



    if(flag_keywords!=1):
       for k in range(0, len(operators)):
          if (a[i]==operators[k]):
             flag_operators=1
             y.append("operator")
             break

    if (flag_keywords != 1 and flag_operators!=1):
       for u in range(0, len(Num)):
             if (a[i].isdigit()):
                flag_Num=1
                y.append("Number")
                break

    for r in range(0, len(white_spaces)):
        if (a[i] == white_spaces[r]):
            flag_white_spaces = 1
            y.append("white_spaces")
            break

    for o in range(0, len(Relational_Operators)):
        if (a[i] == Relational_Operators[o]):
            flag_Relational_Operators = 1
            y.append("Relational_Operators")
            break

    for t in range(0, len(conditional_Logical_Operators)):
        if (a[i] == conditional_Logical_Operators[t]):
            flag_conditional_Logical_Operators = 1
            y.append("conditional_Logical_Operators")
            break

    for p in range(0, len(Logical_Operators)):
        if (a[i] == Logical_Operators[p]):
            flag_Logical_Operators = 1
            y.append("Logical_Operators")
            break

    for w in range(0, len(delim)):
         if (a[i] == delim[w]):
                flag_delim = 1
                y.append("delim")
                break

    for z in range(0, len(predirect)):
        if (a[i] == predirect[z]):
            flag_predirect = 1
            y.append("predirect")
            break

    for s in range(0, len(identefire)):
        tok=list(a[i])
        length=len(tok)-1

        if (tok[0]=='_' or tok[0] in string.ascii_letters and flag_keywords != 1 and flag_keywords != 1
            and flag_operators != 1 and flag_Num != 1 and flag_Relational_Operators != 1
            and flag_predirect != 1 and flag_delim != 1 and flag_Logical_Operators != 1
            and flag_conditional_Logical_Operators != 1
            and flag_Relational_Operators != 1 and flag_white_spaces != 1 ):
            flag_identefire = 1
            for i in range (1,len(tok)):
                if (tok[i] in string.ascii_letters or tok[i].isdigit() or tok[i]=='_'):
                    length=length-1

                else:
                    a.append(tok[i])
                    y.append("error")

                    break
            if length==0 :

                y.append("identefire")
            break

    if (flag_keywords != 1 and flag_keywords != 1 and flag_operators != 1 and flag_Num != 1 and flag_Relational_Operators != 1 and flag_identefire != 1
    and flag_predirect != 1 and flag_delim != 1 and flag_Logical_Operators != 1 and flag_conditional_Logical_Operators != 1
    and flag_Relational_Operators != 1 and flag_white_spaces != 1 ):

            y.append("Error")




for i in range (0,len(y)):

    print("<",a[i],",",y[i],">" )


