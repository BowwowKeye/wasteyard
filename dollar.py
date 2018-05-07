total=raw_input('input your money')
total=float(total)
if total<1:
    total*=100
(quarter,total)=divmod(total,25)
(dime,total)=divmod(total,10)
(nickel,total)=divmod(total,5)
(cent,total)=divmod(total,1)

print 'quarter:%d,dime:%d,nickel:%d,cent:%d' % (quarter,dime,nickel,cent)
