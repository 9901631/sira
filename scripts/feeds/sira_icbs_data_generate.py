from faker import Faker
import random, string
import datetime
from datetime import datetime

fake = Faker("en_GB")

current_date = datetime.now().strftime("%Y%m%d")

def sira_icbs_src_data(i, sira_icbs_data):

    sira_icbs_data[i] = {}

    sira_icbs_data[i]['MAAPPCODE'] = fake.postcode()
    sira_icbs_data[i]['MAAPPNUM'] = random.randint(100, 999)
    sira_icbs_data[i]['MACUADDFLNUM'] = "Flat " + str(random.randint(10, 99))
    sira_icbs_data[i]['MACUADDHSNAME'] = fake.secondary_address()
    sira_icbs_data[i]['MACUADDHSNUM'] = fake.building_number()
    sira_icbs_data[i]['MACUADDSRTEET'] = fake.street_address()
    sira_icbs_data[i]['MACUADDDIST'] = fake.county()
    sira_icbs_data[i]['MACUADDTOWN'] = fake.city()
    sira_icbs_data[i]['MACUADDCOUNTY'] = fake.county()
    sira_icbs_data[i]['MACUADDPCODE'] = fake.postcode()
    sira_icbs_data[i]['MACUADDTIMEINYRS'] = random.choices(['100', '1908', '1107', '1012'])[0]
    sira_icbs_data[i]['MACUADDTYPE'] = random.choices(['RESIDENTIAL', 'COMMERCIAL', 'UNKNOWN'])[0]
    sira_icbs_data[i]['MAPRADDFLNUM'] = "Flat " + str(random.randint(10, 99))
    sira_icbs_data[i]['MAPRADDHSNAME'] = fake.secondary_address()
    sira_icbs_data[i]['MAPRADDHSNUM'] = fake.building_number()
    sira_icbs_data[i]['MAPRADDSRTEET'] = fake.street_address()
    sira_icbs_data[i]['MAPRADDDIST'] = fake.county()
    sira_icbs_data[i]['MAPRADDTOWN'] = fake.city
    sira_icbs_data[i]['MAPRADDCOUNTY'] = fake.county()
    sira_icbs_data[i]['MAPRADDPCODE'] = fake.postcode()
    sira_icbs_data[i]['MAPRADDTIMEINYRS'] = random.choices(['100', '1908', '1107', '1012'])[0]
    sira_icbs_data[i]['MAPRADDTYPE'] = random.choices(['RESIDENTIAL', 'COMMERCIAL', 'UNKNOWN'])[0]
    sira_icbs_data[i]['MAAPPID'] = random.randint(100000, 999999)
    sira_icbs_data[i]['MAAPPDATE'] = fake.date #TO BE UPDATED
    sira_icbs_data[i]['MAAPPTIME'] = datetime.utcnow().strftime('%H.%M.%S')
    sira_icbs_data[i]['MAAPPVALUE'] = random.choices(['100', '1908', '1107', '10000000','0'])[0]
    sira_icbs_data[i]['MALOANPURPOSE'] = random.choices(['9', '8', '13'])[0]
    sira_icbs_data[i]['MACHANNELID'] = random.choices(['INTERNET', 'POST', 'UNSPECIFIED'])[0]
    sira_icbs_data[i]['MABRAND'] = 'LTB'
    sira_icbs_data[i]['MAPRODUCT'] = random.choices(['CURRENT ACCOUNT', 'CREDIT CARD', 'UNSECURED LOAD'])[0]
    sira_icbs_data[i]['MASUBPRDCT'] = random.choices(['LLOYDS', 'Lloyds Bank Current Account', 'Single Tier Products'])[0]
    sira_icbs_data[i]['MACLASSFICN'] = random.choices(['Accept', 'Decline'])[0]
    sira_icbs_data[i]['MABALTRNFRREQ'] = random.choices(['N', ''])[0]
    sira_icbs_data[i]['MABALTRNFRAMT'] =  random.choices(['10004005', '1107', '11000000','0'])[0]
    sira_icbs_data[i]['MAIDREFTYPE1'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['MAIDREFTYPE2'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['MAIDREFTYPE3'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['MAIDREFNUM'] = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    sira_icbs_data[i]['MADDACCNTNUM'] = random.randint(10000000, 99999999)
    sira_icbs_data[i]['MADDSORTCODE'] = random.randint(100000, 999999)
    sira_icbs_data[i]['MAEID'] = random.randint(10000000, 99999999)
    sira_icbs_data[i]['MASELLBRNCH'] = sira_icbs_data[i]['MAPRADDTOWN']
    sira_icbs_data[i]['MASELLCOLLID'] = random.randint(100000, 999999)
    sira_icbs_data[i]['MAHOMEPHNE'] = fake.phone_number()
    sira_icbs_data[i]['MAMOBILEPHNE'] = fake.phone_number()
    sira_icbs_data[i]['MAEMAILADDR'] = fake.street_address()
    sira_icbs_data[i]['MAIPADDR'] = fake.ipv4()
    sira_icbs_data[i]['MADEVIDSUMMSCRE'] = ''
    sira_icbs_data[i]['MADEVICEID'] = random.randint(100000, 999999)
    sira_icbs_data[i]['MAFUZZYDEVICEID'] = random.randint(100000, 999999)
    sira_icbs_data[i]['MAOS'] = ''
    sira_icbs_data[i]['MAIPCOUNTRY'] = 'United Kingdom'
    sira_icbs_data[i]['MAIPCITY'] = fake.city()
    sira_icbs_data[i]['MAEMTRADENAME'] = ''.join(random.choices(string.ascii_letters, k=10))
    sira_icbs_data[i]['MAEMADDFLNUM'] = "Flat " + str(random.randint(10, 99))
    sira_icbs_data[i]['MAEMADDHSNAME'] = ''.join(random.choices(string.ascii_letters, k=10))
    sira_icbs_data[i]['MAEMADDHSNUM'] = fake.building_number()
    sira_icbs_data[i]['MAEMADDSTREET'] = fake.street_address()
    sira_icbs_data[i]['MAEMADDDIST'] = fake.city()
    sira_icbs_data[i]['MAEMADDTOWN'] = fake.city()
    sira_icbs_data[i]['MAEMCOUNTY'] = fake.city()
    sira_icbs_data[i]['MAEMCOUNTRY'] = 'United Kingdom'
    sira_icbs_data[i]['MAEMPHONENUM'] = sira_icbs_data[i]['MAHOMEPHNE']
    sira_icbs_data[i]['MATITLE'] = sira_icbs_data[i]['MAHOMEPHNE']
    sira_icbs_data[i]['MAINITIALS'] = random.choice(string.ascii_letters).upper()
    gender = random.choices(['001', '002'])[0]
    sira_icbs_data[i]['MAFIRSTNAME'] = fake.first_name_male() if gender == '001' else fake.first_name_female()
    sira_icbs_data[i]['MASURNAME'] = fake.last_name()
    sira_icbs_data[i]['MADOB'] = fake.date_of_birth().strftime('%Y-%m-%d')
    sira_icbs_data[i]['MAGENDER'] = gender
    sira_icbs_data[i]['MAMARITALST'] = random.choices(['002', '008','001','99'])[0]
    sira_icbs_data[i]['MARESSTATUS'] = random.choices(['001', '002'])[0]
    sira_icbs_data[i]['MAEMPSTATUS'] = random.choices(['001', '002', '123', '004'])[0]
    sira_icbs_data[i]['MAOCCTYPE'] = random.choices(['013', '321', '', '3'])[0]
    sira_icbs_data[i]['MAJOBTITLE'] = fake.job()
    sira_icbs_data[i]['MANATIONALITY'] = 'British'
    sira_icbs_data[i]['MACUSTTYPE'] = random.choices(['013', '321', '', '3'])[0]
    sira_icbs_data[i]['MASWITCHIND'] = ''
    sira_icbs_data[i]['MASALANUAL'] = str(random.randint(10000, 99999)).rjust(15, '0') + '.000'
    sira_icbs_data[i]['MASALMNTH'] = str(random.randint(1000, 9999)).rjust(15, '0') + '.000'
    sira_icbs_data[i]['MADAY1REF1'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['MADAY1REF2'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['MADAY1REF3'] = 'N'
    sira_icbs_data[i]['MADAY1FRDREF1'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['MADAY1FRDREF2'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['MADAY1FRDREF3'] = 'N'
    sira_icbs_data[i]['MADAY1CIFASREF1'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['MADAY1CIFASREF2'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['MADAY1CIFASREF3'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['MADAY1FRDREFID'] = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    sira_icbs_data[i]['JACUADDFLNUM'] = "Flat " + str(random.randint(10, 99))
    sira_icbs_data[i]['JACUADDHSNAME'] = fake.secondary_address()
    sira_icbs_data[i]['JACUADDHSNUM'] = fake.building_number()
    sira_icbs_data[i]['JACUADDSRTEET'] = fake.street_address()
    sira_icbs_data[i]['JACUADDDIST'] = fake.county()
    sira_icbs_data[i]['JACUADDTOWN'] = fake.city()
    sira_icbs_data[i]['JACUADDCOUNTY'] = fake.county()
    sira_icbs_data[i]['JACUADDPCODE'] = fake.postcode()
    sira_icbs_data[i]['JACUADDTIMEINYRS'] = random.choices(['100', '1908', '1107', '1012'])[0]
    sira_icbs_data[i]['JACUADDTYPE'] = random.choices(['RESIDENTIAL', 'COMMERCIAL', 'UNKNOWN'])[0]
    sira_icbs_data[i]['JAPRADDFLNUM'] = "Flat " + str(random.randint(10, 99))
    sira_icbs_data[i]['JAPRADDHSNAME'] = fake.secondary_address()
    sira_icbs_data[i]['JAPRADDHSNUM'] = fake.building_number()
    sira_icbs_data[i]['JAPRADDSRTEET'] = fake.street_address()
    sira_icbs_data[i]['JAPRADDDIST'] = fake.county()
    sira_icbs_data[i]['JAPRADDTOWN'] = fake.city()
    sira_icbs_data[i]['JAPRADDCOUNTY'] = fake.county()
    sira_icbs_data[i]['JAPRADDPCODE'] = fake.postcode()
    sira_icbs_data[i]['JAPRADDTIMEINYRS'] = random.choices(['100', '1908', '1107', '1012'])[0]
    sira_icbs_data[i]['JAPRADDTYPE'] = random.choices(['RESIDENTIAL', 'COMMERCIAL', 'UNKNOWN'])[0]
    sira_icbs_data[i]['JAIDREFTYPE1'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['JAIDREFTYPE2'] = ''.rjust(6, ' ')
    sira_icbs_data[i]['JAIDREFTYPE3'] = 'N'
    sira_icbs_data[i]['JAIDREFNUM'] = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    sira_icbs_data[i]['JAEID'] = random.randint(10000000, 99999999)
    sira_icbs_data[i]['JAHOMEPHNE'] = fake.phone_number()
    sira_icbs_data[i]['JAMOBILEPHNE'] = fake.phone_number()
    sira_icbs_data[i]['JAEMAILADDR'] = fake.street_address()
    sira_icbs_data[i]['JAEMTRADENAME'] = ''.join(random.choices(string.ascii_letters, k=10))
    sira_icbs_data[i]['JAEMADDFLNUM'] = sira_icbs_data[i]['JAPRADDFLNUM']
    sira_icbs_data[i]['JAEMADDHSNAME'] = fake.secondary_address()
    sira_icbs_data[i]['JAEMADDHSNUM'] = ''
    sira_icbs_data[i]['JAEMADDSRTEET'] = fake.street_address()
    sira_icbs_data[i]['JAEMADDDIST'] = fake.county()
    sira_icbs_data[i]['JAEMADDTOWN'] = fake.city
    sira_icbs_data[i]['JAEMADDCOUNTY'] = fake.county()
    sira_icbs_data[i]['JAEMADDCOUNTRY'] = 'United Kingdom'
    sira_icbs_data[i]['JAEMPHONENUM'] = fake.phone_number()
    sira_icbs_data[i]['JATITLE'] = sira_icbs_data[i]['JAHOMEPHNE']
    sira_icbs_data[i]['JAINITIALS'] = sira_icbs_data[i]['MAINITIALS']
    sira_icbs_data[i]['JAFIRSTNAME'] = sira_icbs_data[i]['MAFIRSTNAME']
    sira_icbs_data[i]['JASURNAME'] = sira_icbs_data[i]['MASURNAME']
    sira_icbs_data[i]['JADOB'] = fake.date_of_birth().strftime('%Y-%m-%d')
    sira_icbs_data[i]['JAGENDER'] = gender
    sira_icbs_data[i]['JAMARITALST'] = random.choices(['002', '008','001','99'])[0]
    sira_icbs_data[i]['JARESSTATUS'] = random.choices(['001', '002'])[0]
    sira_icbs_data[i]['JAEMPSTATUS'] = random.choices(['001', '002', '123', '004'])[0]
    sira_icbs_data[i]['JAOCCTYPE'] = random.choices(['013', '321', '', '3'])[0]
    sira_icbs_data[i]['JAJOBTITLE'] = fake.job()
    sira_icbs_data[i]['JANATIONALITY'] = 'British'
    sira_icbs_data[i]['JACUSTTYPE'] = random.choices(['013', '321', '', '3'])[0]
    sira_icbs_data[i]['JASALANUAL'] = str(random.randint(10000, 99999)).rjust(15, '0') + '.000'
    sira_icbs_data[i]['JASALMNTH'] = str(random.randint(1000, 9999)).rjust(15, '0') + '.000'