class Patient:
    def __init__(self, sender, subject, date):
        '''
        Initlizes the first name, lastname, age and illness, severity, and arival order.
        '''
        self.sender = sender
        self.subject = subject
        self.date = date


    def __lt__(self, other):
        '''
        Magic method that compares severity then age then arrival order based on what is greater or eqaul to.
        '''
        if self.severity == other.severity:
            if self.age == other.age:
                return self.arrival_order > other.arrival_order
        return self.severity < other.severity 

    def __repr__(self):
        '''
        Printable representation of the patient.
        '''
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Illness: {self.illness}, Severity: {self.severity}"