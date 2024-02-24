bkt_seq = input()

bkt_dict = {']':'[', ')':'(', '}':'{'}
stack = []

def define_seq(bkt_seq):
    for bkt in bkt_seq:
        if bkt not in bkt_dict:
            stack.append(bkt)
        else:
            if len(stack)==0 or stack.pop()!=bkt_dict[bkt]:
                return 'no'
           
    return 'yes' if len(stack)==0 else 'no'
   
print(define_seq(bkt_seq))