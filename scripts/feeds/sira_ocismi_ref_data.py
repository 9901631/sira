
from faker import Faker
import random
from datetime import datetime

fake = Faker("en_GB")

current_date = datetime.now().strftime("%Y%m%d")

def asm_src_data(i, ocismi_ref_data, pty_id):

    pty_id_1 = str(random.randint(10000000, 99999999))

    ocismi_ref_data[i] = {}

    ocismi_ref_data[i]['PTY_ID'] = random.choices([pty_id_1, pty_id])[0]
    ocismi_ref_data[i]['NI_NO'] = fake.secondary_address()
    ocismi_ref_data[i]['EMAIL_ID'] = fake.building_number()
    ocismi_ref_data[i]['DRIVE_LIC'] = fake.street_address()
    ocismi_ref_data[i]['PASSPORT_NO'] = fake.county()
    ocismi_ref_data[i]['COUNTRY'] = fake.city()



