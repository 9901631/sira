
from faker import Faker
import random, string
import datetime
from datetime import datetime

fake = Faker("en_GB")

current_date = datetime.now().strftime("%Y%m%d")

def asm_src_data(i, ocismi_phone_data, pty_id):

    pty_id_1 = str(random.randint(1000, 9999)).rjust(10, '0')

    ocismi_phone_data[i] = {}

    ocismi_phone_data[i]['PTY_ID'] = random.choices([pty_id_1, pty_id])[0]
    ocismi_phone_data[i]['HOME_ARA_CD'] = fake.secondary_address()
    ocismi_phone_data[i]['HOME_PHONE'] = fake.building_number()
    ocismi_phone_data[i]['EMP_ARA_CD'] = fake.street_address()
    ocismi_phone_data[i]['EMP_PHONE'] = fake.county()
    ocismi_phone_data[i]['MOBILE_ARA_CD'] = fake.city()
    ocismi_phone_data[i]['MOBILE_PHONE'] = fake.county()


