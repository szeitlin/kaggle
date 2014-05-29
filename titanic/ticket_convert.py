test = "A/C 34567"
numbers = "0123456789"

ticket = ""

for d in test:
  if d in numbers:
	ticket = ticket + d

if int(ticket)%2 > 0:
	print ticket
