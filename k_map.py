# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:46:22 2017

@author: Lucky
"""
import itertools

def expression(l_):
    hex_={(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15):"1"}
    oct_={(0, 1, 2, 3, 4, 5, 6, 7):"A'", (4, 5, 6, 7, 12, 13, 14, 15):"B", (8, 9, 10, 11, 12, 13, 14, 15):"A", (0, 1, 4, 5, 8, 9, 12, 13):"C'", (1, 3, 5, 7, 9, 11, 13, 15):"D", (2, 3, 6, 7, 10, 11, 14, 15):"C", (0, 2, 4, 6, 8, 10, 12, 14):"D'", (0, 1, 2, 3, 8, 9, 10, 11):"B'"}
    quad_={(0, 1, 2, 3):"A'B'", (4, 5, 6, 7):"A'B", (12, 13, 14, 15):"AB", (8, 9, 10, 11):"AB'", (0, 4, 8, 12):"C'D'", (1, 5, 9, 13):"C'D", (3, 7, 11, 15):"CD", (2, 6, 10, 14):"CD'", (0, 1, 4, 5):"A'C'", (1, 3, 5, 7):"A'D", (2, 3, 6, 7):"A'C", (4, 5, 12, 13):"BC'", (5, 7, 13, 15):"BD", (6, 7, 14, 15):"BC", (8, 9, 12, 13):"AC'", (9, 11, 13, 15):"AD",(10, 11, 14, 15):"AC", (0, 1, 8, 9):"B'C'", (1, 3, 9, 11):"B'D", (2, 3, 10, 11):"B'C", (0, 2, 8, 10):"B'D'", (0, 2, 4, 6):"A'D'", (8, 10, 12, 14):"AD'", (4, 6, 12, 14):"BD'"}
    pair_={(0, 1):"A'B'C'", (1, 3):"A'B'D", (2, 3):"A'B'C", (0, 2):"A'B'D'", (4, 5):"A'BC'", (5, 7):"A'BD", (6, 7):"A'BC", (4, 6):"A'BD'", (12, 13):"ABC'", (13, 15):"ABD", (14, 15):"ABC", (12, 14):"ABD'", (8, 9):"AB'C'", (9, 11):"AB'D", (10, 11):"AB'C", (8, 10):"AB'D'", (0, 4):"C'D'A'", (4, 12):"C'D'B", (8, 12):"C'D'A", (0, 8):"C'D'B'", (1, 5):"C'DA'", (5, 13):"C'DB", (9, 13):"C'DA", (1, 9):"C'DB'", (3, 7):"CDA'", (7, 15):"CDB", (11, 15):"CDA",(3, 11):"CDB'", (2, 6):"CD'A'", (6, 14):"CD'B", (10, 14):"CD'A", (2, 10):"CD'B'"}
    singl_={(0,):"A'B'C'D'",(1,):"A'B'C'D",(2,):"A'B'CD'",(3,):"A'B'CD",(4,):"A'BC'D'",(5,):"A'BC'D",(6,):"A'BCD'",(7,):"A'BCD",(8,):"AB'C'D'",(9,):"AB'C'D",(10,):"AB'CD'",(11,):"AB'CD",(12,):"ABC'D'",(13,):"ABC'D",(14,):"ABCD'",(15,):"ABCD"}

    exp=''
    #print l_
    for i in l_:
       for j in hex_:
           if(j==tuple(i)):
                exp=exp + "+" + hex_[j]
       for j in oct_:
           if(j==tuple(i)):
                exp=exp + "+" + oct_[j]
       for j in quad_:
           if(j==tuple(i)):
                exp=exp + "+" + quad_[j]
       for j in pair_:
           if(j==tuple(i)):
                exp=exp + "+" + pair_[j]
       for j in singl_:
           if(j==tuple(i)):
                exp=exp + "+" + singl_[j]
    
    return exp
    
                        
                        
def prime(m_):
    
    prime_=[]
    o_=[]
    q_=[]
    p_=[]
    s_=[]
    
    for i in m_:
        if(len(i)==8):
            o_.append(i)
        if(len(i)==4):
            q_.append(i)
        if(len(i)==2):
            p_.append(i)
        if(len(i)==1):
            s_.append(i)

    if(o_!=[]):
        prime_.extend(o_)
        for i in q_:
            flag=0
            for j in o_:
                if((set(j)>set(i))):
                    flag=1
                    break;
            if(flag==0):
                prime_.append(i)
        for i in p_:
            flag=0
            for j in q_:
                if((set(j)>set(i))):
                    flag=1
                    break;
            if(flag==0):
                prime_.append(i)
        for i in s_:
            flag=0
            for j in p_:
                if((set(j)>set(i))):
                    flag=1
                    break;
            if(flag==0):
                prime_.append(i)

    if(o_==[] and q_!=[]):
        prime_.extend(q_)
        for i in p_:
            flag=0
            for j in q_:
                if((set(j)>set(i))):
                    flag=1
                    break;
            if(flag==0):
                prime_.append(i)
        for i in s_:
            flag=0
            for j in p_:
                if((set(j)>set(i))):
                    flag=1
                    break;
            if(flag==0):
                prime_.append(i)
    if(q_==[] and p_!=[]):
         prime_.extend(p_)
         for i in s_:
             flag=0
             for j in p_:
                 if((set(j)>set(i))):
                     flag=1
                     break;
             if(flag==0):
                prime_.append(i) 
    if(p_==[]):
        return m_
        
    return prime_

def check(h_,o_,q_,p_,s_):
    
    match_found=[]    
    
    hex_=[[0,1,3,2,4,5,7,6,12,13,15,14,8,9,11,10]]
    hex_=[sorted(i) for i in hex_]
    #print hex_
    
    oct_=[[0,1,3,2,4,5,7,6],[4,5,7,6,12,13,15,14],[12,13,15,14,8,9,11,10],[0,4,12,8,1,5,13,9],[1,5,13,9,3,7,15,11],[3,7,15,11,2,6,14,10],[0,4,12,8,2,6,14,10],[0,1,3,2,8,9,11,10]]
    oct_=[sorted(i) for i in oct_]
    #print oct_
    
    quad_=[[0,1,3,2],[4,5,7,6],[12,13,15,14],[8,9,11,10],[0,4,12,8],[1,5,13,9],[3,7,15,11],[2,6,14,10],[0,1,5,4],[1,3,7,5],[3,2,6,7],[4,5,13,12],[5,7,15,13],[7,6,14,15],[12,13,9,8],[13,15,11,9],[15,14,10,11],[8,9,1,0],[9,11,3,1],[11,10,2,3],[0,2,10,8],[0,2,6,4],[12,14,10,8],[4,6,14,12]]
    quad_=[sorted(i) for i in quad_]
    #print quad_
    
    pair_=[[0,1],[1,3],[3,2],[0,2],[4,5],[5,7],[7,6],[4,6],[12,13],[13,15],[15,14],[12,14],[8,9],[9,11],[11,10],[8,10],[0,4],[4,12],[12,8],[0,8],[1,5],[5,13],[13,9],[1,9],[3,7],[7,15],[15,11],[3,11],[2,6],[6,14],[14,10],[2,10]]
    pair_=[sorted(i) for i in pair_]
    #print  pair_
    
    singl_=[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]]

    for i in h_:
        for j in hex_:
            if(i==j):
                match_found.append(j)

    for i in o_:
        for j in oct_:
            if(i==j):
                match_found.append(j)
    for i in q_:
        for j in quad_:
            if(i==j):
                match_found.append(j)
    for i in p_:
        for j in pair_:
            if(i==j):
                match_found.append(j)                
    for i in s_:
        for j in singl_:
            if(i==j):
                match_found.append(j)
   # print match_found
           
    return match_found

def oct_(min_):
    b=[list(x) for x in itertools.combinations(min_, 8)]
    b=[sorted(i) for i in b]
    return b;    
def quad(min_):
    b=[list(x) for x in itertools.combinations(min_, 4)]
    b=[sorted(i) for i in b]    
    return b;
def pair(min_):
    b=[list(x) for x in itertools.combinations(min_, 2)]
    b=[sorted(i) for i in b]    
    return b;    
def single(min_):
    b=[list(x) for x in itertools.combinations(min_, 1)]
    b=[sorted(i) for i in b]    
    return b;    

def create_comb(min_t,n_terms):
    if(n_terms>=1 and n_terms<2):
        s=single(min_t)
        #print s
        match_=check([['16']],[['16']],[['16']],[['16']],s)
        p_=prime(match_)
    
    
    if(n_terms>=2 and n_terms<4):
        p=pair(min_t)
        s=single(min_t)
        #print s
        #print p
        match_=check([['16']],[['16']],[['16']],p,s)
        p_=prime(match_)
        
    if(n_terms>=4 and n_terms<8):
        p=pair(min_t)
        s=single(min_t)
        q=quad(min_t)
        #print s
        #print p
        #print q
        match_=check([['16']],[['16']],q,p,s)
        p_=prime(match_)
        
    if(n_terms>=8 and n_terms<16):
        p=pair(min_t)
        s=single(min_t)
        q=quad(min_t)
        o=oct_(min_t)
        #print s
        #print p
        #print q
        #print o
        match_=check([['16']],o,q,p,s)
        p_=prime(match_)
        
    if(n_terms==16):
        h=[0,1,3,2,4,5,7,6,12,13,15,14,8,9,11,10]        
        #print h       
    
        match_=h
        p_=match_
        
    return p_
    
def filter_(li_):
    for i in li_:
        re=[]
        for k in i:
             for j in li_:                
                if(i!=j):    
                    if(k in j):
                        re.append(k)        
        try:
            li_.remove(re)
        except:
            re=[]            
            
    return li_ 
                
                
        
n_terms=input("ENTER THE NUMBER OF TERMS:  ")
min_terms=[]
print "ENTER MIN TERMS:  "
for i in range(n_terms):
    x=input()
    min_terms.append(x)  
    
list_=create_comb(min_terms,n_terms)
list_n=filter_(list_)
print '\n'
print "prime: "
print list_n
exp_=expression(list_n)
print "\n"

print "output:",exp_[1:len(exp_)]