from abc import ABC, abstractmethod
import yaml 

class Band:
    instance_of_a_class = []

    # This is a constructor
    #### self.instance_of_a_class works but not recommended ####
    def __init__(self, name , members = []):
        self.name = name
        self.members = members
        Band.instance_of_a_class.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"The band instance with name = {self.name}, members = {self.members}"        

    @staticmethod
    def create_from_data(yaml_file_path):
        with open(yaml_file_path) as f:
            file = yaml.safe_load(f)

            for band_name,band_details in file.items():
                members_list = []
                
                for _,musician in band_details.items(): 
                    # print(musician)
                    member_name = musician.get('Name')
                    member_speciality = musician.get('Speciality')
                    object_name = band_name + member_speciality

                    # Assign members to musician object
                    if member_speciality == 'Guitarist':
                        object_name = Guitarist(member_name)
                    elif member_speciality == 'Bassist':
                        object_name = Bassist(member_name)
                    elif member_speciality == 'Drummer':
                        object_name = Drummer(member_name)
                    else:
                        raise Exception(f"We are not taking {member_speciality} now. Please check YAML file")
                    members_list.insert(0,object_name)

                # Create Band
                band_name_object = Band(band_name,members_list)  

            print("************************************Bands Object*******************************************")
            for band in band_name_object.to_list():
                print(repr(band))
            print("*******************************************************************************************")


    @classmethod
    def to_list(cls):
        return cls.instance_of_a_class

    def play_solos(self):
        solo = []
        for member in self.members:
            solo.append(member.play_solo())

        return solo

class Musician(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(f"I am a musician named {self.name}")

    def __repr__(self):
        return str(f"Musician instance. Name: {self.name}")
    
    def get_instrument(self):
         return self.instrument

    def play_solo(self):
         return self.instrument_solo

class Guitarist(Musician):
    def __init__(self,name):
        self.name = name
        self.instrument = "Guitar"
        self.instrument_solo = f"{self.name} Playing solo guitar"

    def __str__(self):
        return str(f"I am a guitarist named {self.name}")

    def __repr__(self):
        return str(f"Guitarist instance. Name: {self.name}")


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "Bass"
        self.instrument_solo = f"{self.name} Playing solo bass"

    def __str__(self):
        return str(f"I am a bassist named {self.name}")

    def __repr__(self):
        return str(f"Bassist instance. Name: {self.name}")


class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "Drum"
        self.instrument_solo = f"{self.name} Playing solo drum"

    def __str__(self):
        return str(f"I am a Drummer named {self.name}")

    def __repr__(self):
        return str(f"drummer instance. Name: {self.name}")

if __name__ == "__main__":
    Band.create_from_data('pythonic_garage_band\\assets\\bands.yaml')