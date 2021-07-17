teamCsr = {'Busola': 'Inbound', 'Tosin': 'Inbound', 'Tobi': 'Inbound', 'Samuel': 'Livechat', 'Jethro': 'Inbound'}
print(type(teamCsr))
newTeam = 'email'
teamCsr['Biola'] = newTeam
print(teamCsr)
teamLeads = {'Lukman': {'Team':'Livechat', 'pay':46632},
             'Biola': {'Team':'Inbound', 'pay':77362}}
print(teamLeads)
print(type(teamLeads))
print(teamLeads['Lukman']['pay'])


csrpay = {'Samuel':{'team': 'livechat', 'pay': 67000},
          'Ayobami':{'team':'livechat', 'pay': 68000},
          'Shakira': {'team': 'livechat', 'pay': 70000},
          'Sandra': {'team': 'livechat', 'pay': 70000}}


print(csrpay)
print(csrpay['Samuel']['pay'])
newupdate = {'team': 'Easybuy', 'pay': 76000}
csrpay['Sophie'] = newupdate
print(csrpay)
anotheragent = {'team': 'inbound', 'pay': 58000}
csrpay['Precious'] = anotheragent
print(csrpay)
print(csrpay['Precious']['pay'])
csrHead = {'position': 'Department head'}
csrpay['Tolu'] = csrHead
print(csrpay)
print(csrpay['Tolu']['position'])
