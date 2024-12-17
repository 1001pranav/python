class Film:
    allowed_languages = ['Kannada', 'Hindi', 'English', 'Tamil', 'Telugu', 'Malayalam']

    def __init__(self, title: str, year: int, language:str):
        
        assert language in Film.allowed_languages, f"Language {language} is not supported"
        assert year >= 1900, f"Please select movies released after 1900 {year} "

        self.title = title
        self.year = year
        self.language = language

    def __repr__(self):
        return f"Film({self.title}, {self.year}, {self.language})"
    
    def __str__(self):
        return f"title: {self.title}, year: {self.year}, language: {self.language}"
    
drishyam = Film('Drishyam', 2013, 'Malayalam')
all_the_best = Film('All the best', 1900, 'Hindi')

# repr() is mainly intended for developers and debugging purposes. 
print(" Printed using __repr__() ", drishyam.__repr__())
# str() aims to produce a human-readable representation, suitable for end users.
print('Printing using __str__()', all_the_best.__str__())
