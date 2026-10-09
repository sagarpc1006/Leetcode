class Solution:
    def defangIPaddr(self, address: str) -> str:
        """address=list(address)
        for i in range(len(address)):
            if ( address[i] == '.') :
                address[i] = '[.]'
        return str(address)"""
        #return address.replace('.','[.]')
        ans=""
        for i in address :
            if ( i == '.'):
                ans=ans+'[.]'
            else :
                ans+=i
        return ans