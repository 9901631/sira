
from faker import Faker
import random, string
import datetime
from datetime import datetime

fake = Faker("en_GB")

current_date = datetime.now().strftime("%Y%m%d")

def asm_src_data(i, sira_asm_data, maptyid, japtyid):

    maptyid_1 = str(random.randint(1000, 9999)).rjust(10, '0')
    japtyid_1 = str(random.randint(1000, 9999)).rjust(10, '0')

    sira_asm_data[i] = {}

    sira_asm_data[i]['MACUADDFLTNO'] = "Flat " + str(random.randint(10, 99))
    sira_asm_data[i]['MACUADDHSNAME'] = fake.secondary_address()
    sira_asm_data[i]['MACUADDHSNUM'] = fake.building_number()
    sira_asm_data[i]['MACUADDSTREET'] = fake.street_address()
    sira_asm_data[i]['MACUADDDIST'] = fake.county()
    sira_asm_data[i]['MACUADDTOWN'] = fake.city()
    sira_asm_data[i]['MACUADDCOUNTY'] = fake.county()
    sira_asm_data[i]['MACUADDPCODE'] = fake.postcode()
    sira_asm_data[i]['MACUADDTIMEINYRS'] = random.choices(['100', '1908', '1107', '1012'])[0]
    sira_asm_data[i]['MAPRADDFLTNO'] = sira_asm_data[i]['MACUADDFLTNO']
    sira_asm_data[i]['MAPRADDHSNAME'] = sira_asm_data[i]['MACUADDHSNAME']
    sira_asm_data[i]['MAPRADDHSNUM'] = sira_asm_data[i]['MACUADDHSNUM']
    sira_asm_data[i]['MAPRADDSTREET'] = sira_asm_data[i]['MACUADDSTREET']
    sira_asm_data[i]['MAPRADDDIST'] = sira_asm_data[i]['MACUADDDIST']
    sira_asm_data[i]['MAPRADDTOWN'] = sira_asm_data[i]['MACUADDTOWN']
    sira_asm_data[i]['MAPRADDCOUNTY'] = sira_asm_data[i]['MACUADDCOUNTY']
    sira_asm_data[i]['MAPRADDPCODE'] = sira_asm_data[i]['MACUADDPCODE']
    sira_asm_data[i]['MAPRADDTIMEINYRS'] = sira_asm_data[i]['MACUADDTIMEINYRS']
    sira_asm_data[i]['MAAPPID'] = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    sira_asm_data[i]['MAAPPDATE'] = fake.date #to be updated
    sira_asm_data[i]['MAAPPTIME'] = datetime.utcnow().strftime('%H.%M.%S')
    sira_asm_data[i]['MACARDAPPVALUE'] = random.choices(['100', '1908', '1107', '10000000','0'])[0]
    sira_asm_data[i]['MALOANAPPVALUE'] = random.choices(['100', '1908', '1107', '10000000','0'])[0]
    sira_asm_data[i]['MAODAPPVALUE'] = '0'
    sira_asm_data[i]['MALOANPURPOSE'] = random.choices(['9', '8', '13'])[0]
    sira_asm_data[i]['MACHANNELID'] = random.choices(['INTERNET', 'POST', 'UNSPECIFIED'])[0]
    sira_asm_data[i]['MABRAND'] = 'LTB'
    sira_asm_data[i]['MAPRODUCT'] = random.choices(['CURRENT ACCOUNT', 'CREDIT CARD', 'UNSECURED LOAD'])[0]
    sira_asm_data[i]['MASUBPRODUCT'] = random.choices(['LLOYDS', 'Lloyds Bank Current Account', 'Single Tier Products'])[0]
    sira_asm_data[i]['MACLASSFICN'] = random.choices(['Accept', 'Decline'])[0]
    sira_asm_data[i]['MABALTRNFRREQ'] = random.choices(['N', ''])[0]
    sira_asm_data[i]['MABALTRNFRAMT'] = random.choices(['10004005', '1107', '11000000','0'])[0]
    sira_asm_data[i]['MADDACCNTNUM'] = sira_asm_data[i]['MABALTRNFRAMT']
    sira_asm_data[i]['MADDSORTCODE'] = random.randint(10000, 999999)
    sira_asm_data[i]['MASELLBRNCH'] = random.randint(10000, 999999)
    sira_asm_data[i]['MASELLCOLLID'] = random.randint(10000, 999999)
    sira_asm_data[i]['MAHOMEPHNECD'] = random.choices(['12345', ''])[0]
    sira_asm_data[i]['MAHOMEPHNENO'] = sira_asm_data[i]['MAHOMEPHNECD']
    sira_asm_data[i]['MAEMPHONENUMCD'] = sira_asm_data[i]['MAHOMEPHNECD']
    sira_asm_data[i]['MAEMPHONENUM'] = sira_asm_data[i]['MAHOMEPHNECD']
    sira_asm_data[i]['MATITLE'] = random.choices(['Mr', 'Mrs'])[0]
    sira_asm_data[i]['MAINITIALS'] = random.choice(string.ascii_letters).upper()
    gender = random.choices(['001', '002'])[0]
    sira_asm_data[i]['MAFIRSTNAME'] = fake.first_name_male() if gender == '001' else fake.first_name_female()
    sira_asm_data[i]['MASURNAME'] = fake.last_name()
    sira_asm_data[i]['MADOB'] = fake.date_of_birth().strftime('%Y-%m-%d')
    sira_asm_data[i]['MAGENDER'] = gender
    sira_asm_data[i]['MAMARITALST'] = random.choices(['002', '008','001','99'])[0]
    sira_asm_data[i]['MARESSTATUS'] = random.choices(['001', '002'])[0]
    sira_asm_data[i]['MAEMPSTATUS'] = random.choices(['001', '002', '123', '004'])[0]
    sira_asm_data[i]['MAOCCTYPE'] = random.choices(['013', '321', '', '3'])[0]
    sira_asm_data[i]['MACUSTTYPE'] = random.choices(['3', '1'])[0]
    sira_asm_data[i]['MASWITCHIND'] = ''
    sira_asm_data[i]['MASALANUAL'] = str(random.randint(10000, 99999)).rjust(15, '0') + '.000'
    sira_asm_data[i]['MASALMNTH'] = str(random.randint(1000, 9999)).rjust(15, '0') + '.000'
    sira_asm_data[i]['MADAY1DETREF1'] = ''.rjust(6, ' ')
    sira_asm_data[i]['MADAY1DETREF2'] = ''.rjust(6, ' ')
    sira_asm_data[i]['MADAY1DETREF3'] = 'N'
    sira_asm_data[i]['MADAY1FRDREF1'] = ''.rjust(6, ' ')
    sira_asm_data[i]['MADAY1FRDREF2'] = ''.rjust(6, ' ')
    sira_asm_data[i]['MADAY1FRDREF3'] = 'N'
    sira_asm_data[i]['MADAY1FRDREFID'] = 'N'
    sira_asm_data[i]['MADAY1CIFASREF1'] = ''.rjust(6, ' ')
    sira_asm_data[i]['MADAY1CIFASREF2'] = ''.rjust(6, ' ')
    sira_asm_data[i]['MADAY1CIFASREF3'] = 'N'
    sira_asm_data[i]['MAPTYID'] = random.choices([maptyid, maptyid_1, maptyid])[0]
    sira_asm_data[i]['MALOANTERM'] = str(random.randint(10, 30)).rjust(5, '0')
    sira_asm_data[i]['MATIMEATBANK'] = random.choices(['01608', '00001', '02609', '00000'])[0]
    sira_asm_data[i]['MATIMEATEMP'] = random.choices(['09999','00000'])[0]
    sira_asm_data[i]['JACUADDFLTNO'] = "Flat " + str(random.randint(10, 99))
    sira_asm_data[i]['JACUADDHSNAME'] = fake.secondary_address()
    sira_asm_data[i]['JACUADDHSNUM'] = fake.building_number()
    sira_asm_data[i]['JACUADDSTREET'] = fake.street_address()
    sira_asm_data[i]['JACUADDDIST'] = fake.county()
    sira_asm_data[i]['JACUADDTOWN'] = fake.city()
    sira_asm_data[i]['JACUADDCOUNTY'] = fake.county()
    sira_asm_data[i]['JACUADDPCODE'] = fake.postcode()
    sira_asm_data[i]['JACUADDTIMEINYRS'] = random.choices(['100', '1908', '1107', '1012'])[0]
    sira_asm_data[i]['JAPRADDFLTNO'] = "Flat " + str(random.randint(10, 99))
    sira_asm_data[i]['JAPRADDHSNAME'] = fake.secondary_address()
    sira_asm_data[i]['JAPRADDHSNUM'] = fake.building_number()
    sira_asm_data[i]['JAPRADDSTREET'] = fake.street_address()
    sira_asm_data[i]['JAPRADDDIST'] = fake.county()
    sira_asm_data[i]['JAPRADDTOWN'] = fake.city()
    sira_asm_data[i]['JAPRADDCOUNTY'] = fake.county()
    sira_asm_data[i]['JAPRADDPCODE'] = fake.postcode()
    sira_asm_data[i]['JAPRADDTIMEINYRS'] = random.choices(['100', '1908', '1107', '1012'])[0]
    sira_asm_data[i]['JAHOMEPHNECD'] = random.choices(['12345', ''])[0]
    sira_asm_data[i]['JAHOMEPHNENO'] = sira_asm_data[i]['JAHOMEPHNECD']
    sira_asm_data[i]['JAEMPHONENUMCD'] = sira_asm_data[i]['JAHOMEPHNECD']
    sira_asm_data[i]['JAEMPHONENUM'] = sira_asm_data[i]['JAHOMEPHNECD']
    sira_asm_data[i]['JATITLE'] = random.choices(['Mr', 'Mrs'])[0]
    sira_asm_data[i]['JAINITIALS'] = random.choice(string.ascii_letters).upper()
    sira_asm_data[i]['JAFIRSTNAME'] = sira_asm_data[i]['MAFIRSTNAME']
    sira_asm_data[i]['JASURNAME'] = fake.last_name()
    sira_asm_data[i]['JADOB'] = fake.date_of_birth().strftime('%Y-%m-%d')
    sira_asm_data[i]['JAGENDER'] = gender
    sira_asm_data[i]['JAJARITALST'] = random.choices(['002', '008','001','99'])[0]
    sira_asm_data[i]['JARESSTATUS'] = random.choices(['001', '002'])[0]
    sira_asm_data[i]['JAEMPSTATUS'] = random.choices(['001', '002', '123', '004'])[0]
    sira_asm_data[i]['JAOCCTYPE'] = random.choices(['013', '321', '', '3'])[0]
    sira_asm_data[i]['JACUSTTYPE'] = random.choices(['3', '1'])[0]
    sira_asm_data[i]['JASWITCHIND'] = ''
    sira_asm_data[i]['JASALANUAL'] = sira_asm_data[i]['MASALANUAL']
    sira_asm_data[i]['JASALMNTH'] = sira_asm_data[i]['MASALMNTH']
    sira_asm_data[i]['JAPTYID'] = random.choices([japtyid, japtyid_1, japtyid])[0]
    sira_asm_data[i]['JATIMEATBANK'] = sira_asm_data[i]['MATIMEATBANK']
    sira_asm_data[i]['JATIMEATEMP'] = sira_asm_data[i]['MATIMEATEMP']



