'''
Script for testing whilst under development
'''

import transact2 as tr

ld = tr.Ledger()
ld.add_transactions('data/Santander123 1.txt', 'santander')
ld.add_transactions('data/Santander123 2.txt', 'santander')
#for row in ld.ledger:
    #print (row)
print (ld.ledger)
print ('Start date: %s' % ld.date_from)
print ('End date: %s' % ld.date_to)
print ('%s transactions' % len(ld.ledger))

#ld.add_transactions('data/Santander123 2.txt', 'text')
#print ('Start date: %s' % ld.date_from)
#print ('End date: %s' % ld.date_to)
#print ('%s transactions' % len(ld.ledger))
#filepath = 'data/Santander123 1.txt'
#print (filepath.split(' ')[0].split('/')[1])
#.split('/')[1]

#for key in list(values.keys()):
    #print ('%s: has %s elements' % (key, len(values[key])))