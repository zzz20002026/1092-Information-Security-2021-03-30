
import random as rand
class RSA:
    def __init__(self):
        print(self.r())
        self.p, self.q = map(int,input().split()) 
        self.N = self.p * self.q                   
        print(self.N)
        self.N1 = (self.p-1) * (self.q-1)           
        print(self.N1)
        print(self.genEList(self.N1))
        self.e = int(input("請輸入e: "))                         
        print(self.genDList(self.e,self.N1))
        self.d = int(input("請輸入d: "))
    def encrypt(self):
        msg = int(input("請輸入明文: "))
        self.C = msg**self.e % self.N
        print(self.C)
    def decrypt(self):
        emsg = int(input("請輸入密文: "))
        self.M = emsg**self.d % self.N
        print(self.M)
    def r(self):
        data = []
        while len(data)<5:
            y = rand.randint(2,50)
            if self.isPrime(y):
                data.append(y)
        return data
    def isPrime(self,x):
        n = 2 
        bln = True 
        while n<(x//2):
            if (x%n==0):
                bln = False
                break        
            else:
                bln = True
                break
        n = n + 1
        return bln
    def gcd(self,N1,e):
        maxVal = max(N1,e)
        minVal = min(N1,e)
        if maxVal%minVal==0:
            return minVal
        else:
            return self.gcd(minVal,maxVal%minVal)
    def genEList(self,N1):
        data2 = []
        while len(data2)<5:
            y2 = rand.randint(2,50)
            if self.isPrime2(N1,y2):
                data2.append(y2)
        return data2
    def isPrime2(self,N1,y2):
        maxVal = max(N1,y2)
        minVal = min(N1,y2)
        if maxVal%minVal==0:
            return minVal
        else:
            return self.gcd(minVal,maxVal%minVal)

    def genDList(self,e,N1):
        
        datalist = []
        while len(datalist)<5:
            d = rand.randint(2, 10000)
            if(e*d%N1==1):
                datalist.append(d)
        return datalist

        
if __name__ == '__main__':
    rsa = RSA()
    rsa.encrypt()
    rsa.decrypt()