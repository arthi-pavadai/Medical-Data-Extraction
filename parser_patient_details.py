from backend.src.Parsergeneric import MedicalDocParser
import re


class Patientdetail_Parser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_patient_name(),
            'patient_phone_no': self.get_phone_number(),
            'Hep_B_status': self.get_hep_b_status(),
            'Medical_problems': self.get_medical_prob()
        }

    def get_patient_name(self):
        pattern='Patient Information(.*?)\(\d{3}\)'
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        name = ''
        if match:
            name = self.remove_noise_from_name(match[0])
        return name

    def remove_noise_from_name(self, name):
        name = name.replace('Birth Date', '').strip()
        date_pattern='((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_match = re.findall(date_pattern, name)
        if date_match:
            date = date_match[0][0]
            name= name.replace(date, '').strip()
        return name

    def get_phone_number(self):
        pattern = 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        match = re.findall(pattern,self.text, flags=re.DOTALL)
        if match:
            return match[0][1]

    def get_hep_b_status(self):
        pattern = 'vaccination\?.*(Yes|No)'
        match = re.findall(pattern,self.text, flags=re.DOTALL)
        if match:
            return match[0].strip()

    def get_medical_prob(self):
        pattern = 'head.*?:(.*)'
        match = re.findall(pattern,self.text, flags=re.DOTALL)
        if match:
            return match[0].strip()

if __name__ == "__main__":
    document_text = '''
                   17/12/2020

Patient Medical Record . : :

Patient Information

 

 

Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight:
9264 Ash Dr 95
New York City, 10005 a
United States Height:
190
In Case of Emergency
ee oe
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
I i
Chicken Pox (Varicella): Measies:
IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches):

Migraine
'''
    pp = Patientdetail_Parser(document_text)
    print(pp.parse())