from EMP import EMP
from EMPService import EMPService

emp = EMP(123, 'Steven', 'King', 'SKING', '1234567', '2003-06-17', 'AD_PRES', 24000, '', '', 90)
print(emp)

emp = EMPService.readEmp()
print(emp)

EMPService.computeDuty(emp)