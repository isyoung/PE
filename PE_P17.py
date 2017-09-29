words = {
	0	:'',
	1	:'one',
	2	:'two',
	3	:'three',
	4	:'four',
	5	:'five',
	6	:'six',
	7	:'seven',
	8	:'eight',
	9	:'nine',
	10	:'ten',
	11	:'eleven',
	12	:'twelve',
	13	:'thirteen',
	14	:'fourteen',
	15	:'fifteen',
	16	:'sixteen',
	17	:'seventeen',
	18	:'eighteen',
	19	:'nineteen',
	20	:'twenty',
	30	:'thirty',
	40	:'forty',
	50	:'fifty',
	60	:'sixty',
	70	:'seventy',
	80	:'eighty',
	90	:'ninety'
}

def toword(n):
	#not built for n>999 or <1
	d = digits(n);
	dg = [];
	for i in range(1,d+1):
		dg += [mthdigit(i,n)]
	s='';
	if n<21:
		s+= words[n];
	elif n<100:
		s+= words[dg[1]*10]+words[dg[0]];
	elif n<1000:
		s+= words[dg[2]]+'hundred'
		if not (dg[1]==0 and dg[0]==0):
			if(dg[1]<2):
				s+= 'and'+words[dg[1]*10+dg[0]];
			else: s+='and'+words[dg[1]*10]+words[dg[0]];
	return s;

def digits(n):
	#return number of digits in number (base10)
	c=0;
	while n>0:
		n/=10; #python 2.x
		c+=1;
	return c;

def mthdigit(m,x):
	#return mth digit of x (right2left <--)
	if(m<0):print 'oops'; return 0;
	i=0;
	while True:
		i+=1;
		if i>=m : return x%10;
		x/=10;

s='';
s = 'onethousand';
for i in range(1,1000):
	s+=toword(i);
print len(s)