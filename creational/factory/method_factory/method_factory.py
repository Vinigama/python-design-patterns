from abc import ABCMeta, abstractclassmethod

class Section(metaclass = ABCMeta):
    @abstractclassmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


# Implementação da Fábrica
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractclassmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)
    

class linkedin(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())


class facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())

if __name__ == "__main__":
    profile_type = input("Qual perfil você gostaria de criar?")
    profile = eval(profile_type.lower())()
    print("Criando um perfil:", type(profile).__name__)
    print("Perfil tem as seguintes sessões:", profile.get_sections())