import random


class Subject:
    """
    Subject class to generate subject objects
    """

    @staticmethod
    def supported_subjects():
        return [
            Subject.science, 
            Subject.commerce,
            Subject.arts,
            Subject.computer_science,
            Subject.engineering,
            Subject.medical,
            Subject.law
        ]

    @staticmethod
    def get_subject(category:str):
        """
        Get a subject based on the category
        """

        _sub_dict = {
            "science": Subject.science,
            "commerce": Subject.commerce,
            "arts": Subject.arts,
            "computer_science": Subject.computer_science,
            "cs": Subject.computer_science,
            "engineering": Subject.engineering,
            "medical": Subject.medical,
            "law": Subject.law,
            "leagal": Subject.law,
            "any": random.choice(Subject.supported_subjects())
        }
        return _sub_dict.get(category, Subject.computer_science)()

    @staticmethod
    def science():
        """
        Generate a science subject
        """
        return random.choice(["Physics", "Chemistry", "Biology", "Mathematics", "Computer Science", "Statistics", "Geology", "Astronomy", "Zoology", "Botany", "Microbiology", "Biochemistry", "Biotechnology", "Genetics", "Environmental Science", "Oceanography", "Physics", "Chemistry", "Biology", "Mathematics", "Computer Science", "Statistics", "Geology", "Astronomy", "Zoology", "Botany", "Microbiology", "Biochemistry", "Biotechnology", "Genetics", "Environmental Science", "Oceanography"])
    
    @staticmethod
    def commerce():
        """
        Generate a commerce subject
        """
        return random.choice(["Accountancy", "Business Studies", "Economics", "Mathematics", "Statistics", "Business Mathematics", "Business Economics", "Business Law", "Business Communication", "Business Environment", "Business Finance", "Business Management", "Business Administration", "Business Accounting", "Business Statistics", "Business Mathematics", "Business Economics", "Business Law", "Business Communication", "Business Environment", "Business Finance", "Business Management", "Business Administration", "Business Accounting", "Business Statistics"])
    
    @staticmethod
    def arts():
        """
        Generate an arts subject
        """
        return random.choice(["History", "Geography", "Political Science", "Sociology", "Psychology", "Philosophy", "English", "Hindi", "Sanskrit", "Urdu", "French", "German", "Spanish", "Chinese", "Japanese", "Korean", "Arabic", "History", "Geography", "Political Science", "Sociology", "Psychology", "Philosophy", "English", "Hindi", "Sanskrit", "Urdu", "French", "German", "Spanish", "Chinese", "Japanese", "Korean", "Arabic"])
    
    @staticmethod
    def computer_science():
        """
        Generate a computer subject
        """
        return random.choice(["Computer Science", "Computer Applications", "Information Technology", "Software Engineering", "Computer Engineering", "Computer Programming", "Computer Graphics", "Computer Networks", "Computer Security", "Computer Hardware", "Computer Software", "Computer Science", "Computer Applications", "Information Technology", "Software Engineering", "Computer Engineering", "Computer Programming", "Computer Graphics", "Computer Networks", "Computer Security", "Computer Hardware", "Computer Software", "Full Stack Development", "Frontend Development", "Backend Development", "Mobile App Development", "Web Development", "Game Development", "Data Science", "Machine Learning", "Artificial Intelligence", "Cyber Security", "Cloud Computing", "Internet of Things", "Blockchain Technology", "Big Data", "DevOps"])

    @staticmethod
    def engineering():
        """
        Generate an engineering subject
        """
        return random.choice(["Mechanical Engineering", "Civil Engineering", "Electrical Engineering", 
                            "Electronics Engineering", "Chemical Engineering", "Aerospace Engineering",
                            "Biomedical Engineering", "Industrial Engineering", "Robotics Engineering",
                            "Environmental Engineering", "Marine Engineering", "Mining Engineering",
                            "Petroleum Engineering", "Agricultural Engineering", "Materials Engineering"])

    @staticmethod
    def medical():
        """
        Generate a medical subject
        """
        return random.choice(["Medicine", "Surgery", "Pediatrics", "Gynecology", "Cardiology", 
                            "Neurology", "Psychiatry", "Dermatology", "Ophthalmology", "Dentistry",
                            "Pharmacy", "Nursing", "Physiotherapy", "Nutrition", "Public Health"])

    @staticmethod
    def law():
        """
        Generate a law subject
        """
        return random.choice(["Constitutional Law", "Criminal Law", "Civil Law", "Corporate Law", 
                            "International Law", "Human Rights Law", "Environmental Law", "Cyber Law",
                            "Intellectual Property Law", "Family Law", "Labor Law", "Tax Law"])
    

