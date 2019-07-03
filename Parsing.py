import string

#Production Rules
E=["T+E","T"]
T=["int*T","int"]


#follows
Follow_E=['$']
Follow_T=['$','+']
print ("Follow_E",Follow_E)
print("Follow_T",Follow_T)
####possible tokens

token1="| int $"
token2="| int * int $"
token3="| int + int $"
token4="| int * int + int $"
token5="| int * int * int $"
token6="| int + int + int $"
token7="| int + int * int $"
token8="| int + int + int + int $"
token9="| int * int * int * int $"
token10="| int + int + int * int $"
token11="| int + int * int + int $"
token12="| int * int + int + int $"
token13="| int * int + int * int $"
token14="| int * int + int * int $"
token15="| int + int * int * int $"
token16="| int * int * int + int $"
token17="| int * int * int * int + int + int + int * int + int * int + int + int * int * int $"
token18="| str * str $" #refused


def SLR(token):
    token=token.split()
    print(" token is : ",''.join(token))

    i=0
    j=0

    while i<len(token):

        flag_t=0
        flag_e=0

        if(token[i]=='|' and i==0):
            print("the first step : shift ")
            token[i],token[i+1]=token[i+1],token[i]
            i+=1
            print(''.join(token))


        if(token[i]=='|' and i!=0):
            j=0
            while j < i:

                if(''.join(token[j:i] )in T ):

                    print(" there is shift reduce conflict ")
                    if (token[i+1] in Follow_T):
                        if(i-j == 1):
                            print('"',token[i+1] ,'" is in follow set of T so we will (Reduce) : T ==> int ' )
                            token[i-1]="T"
                            print(''.join(token))
                            flag_t+=1
                            j=0
                            break
                        else:
                            print('"',token[i+1] ,'" is in follow set of T so we will (Reduce) : T ==> int * T' )
                            token[i-1]="T"
                            del token[j:i-1]
                            print(''.join(token))
                            flag_t+=1
                            i=i-(i-j-1) #i=i-2
                            j=0
                            break

                    else:
                        print('"',token[i+1] ,'" is not in follow set of T so we will (Shift) :' )
                        token[i],token[i+1]=token[i+1],token[i]
                        print(''.join(token))
                        i+=1
                        flag_t+=1
                        j=0
                        break
                j+=1

            if(flag_t==0):

                j=0
                while j < i:

                    if(''.join(token[j:i] )in E ):

                        print(" there is shift reduce conflict ")
                        if (token[i+1] in Follow_E):
                            if(i-j == 1):
                                print('"',token[i+1] ,'" is in follow set of E so we will (Reduce) : E ==> T ' )
                                token[i-1]="E"
                                print(''.join(token))
                                flag_e+=1

                                break
                            else:
                                print('"',token[i+1] ,'" is in follow set of E so we will (Reduce) : E ==> T + E' )
                                token[i-1]="E"
                                del token[j:i-1]
                                print(''.join(token))
                                flag_e+=1
                                i=i-(i-j-1)

                        else:
                            print('"',token[i+1] ,'" is not in follow set of E so we will (Shift) :' )
                            token[i],token[i+1]=token[i+1],token[i]
                            print(''.join(token))
                            i+=1
                            flag_e+=1
                            break
                    j+=1
            else:continue

            if(flag_e==0 and flag_t ==0 ):#and i!= len(token)-1):

                print(" there is no shift reduce conflict so we will shif :")
                token[i],token[i+1]=token[i+1],token[i]
                i+=1
                print(''.join(token))

          #  if(token[i-1]=="$"):
          #      print("******REFUSED******")
          #      break
   
        if(''.join(token) == 'E|$'):
            break

    if(''.join(token) == 'E|$'):
        print("*********** ACCEPTED ***************")

SLR(token4)
