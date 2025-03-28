from abc import ABC, abstractmethod

class Ticket:
    def __init__(self, ticket_id, ticket_type, price):
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.price = price
    
    @staticmethod
    def validate_ticket_id(ticket_id):
        if not ticket_id[:3].isupper() or not ticket_id[3:].isdigit() or len(ticket_id) != 8:
            return False
        else:
            return True

    @property
    def ticket_id(self):
        return self.__ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        if not self.validate_ticket_id(value):
            raise ValueError("This has gyatt to be a string in the right formnyatt <:")
        else:
            self.__ticket_id = value
    
    @property
    def ticket_type(self):
        return self.__ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        if not isinstance(value, str):
            raise ValueError("This has gyatt to be a string")
        else:
            self.__ticket_type = value
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("This has gyatt to be a float")
        else:
            self.__price = value
    
    def __str__(self):
        return(f"Ticket ID: {self.ticket_id}, Ticket Type: {self.ticket_type}, Ticket Price: {self.price}")

class Event(ABC):
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.__dict = dict()
    
    def add_ticket(self, ticket):
        if self.total_tickets >= self.max_capacity:
            raise ValueError("full")
        self.__dict[ticket.ticket_id] = ticket
    
    def remove_ticket(self, ticket_id):
        if ticket_id not in self.__dict:
            raise ValueError("No balls!")
        del self.__tickets[ticket_id]
    
    @property
    def total_tickets(self):
        return len(self.__dict)
    
    @abstractmethod
    def generate_event_summary(self):
        pass

class Concert(Event):
    def __init__(self, name, max_capacity, artists):
        super().__init__(name, max_capacity)
        self.artists = artists
    
    def generate_event_summary(self):
        final_string = f"Name: {self.name}\nTotal Tickets: {self.total_tickets}\nArtists:"
        for artist in self.artists:
            final_string += f"\n- {artist}"
        return final_string

class PrivateEvent(Event):
    def __init__(self, name, artists):
        super().__init__(name, 50)
        self.artists = artists
    
    def generate_event_summary(self):
        final_string = f"Name: {self.name}\nTotal Tickets: {self.total_tickets}\nArtists: {self.artists}"
        return final_string

# print(validate_ticket_id("VIP12345"))
# print(validate_ticket_id("VIp12345"))
# print(validate_ticket_id("vIP12345"))
# print(validate_ticket_id("VIP1234V"))
# print(validate_ticket_id("VIPV2345"))
Pukkelpop = Concert("Pukkelpop", 1000, ["Shakira", "David", "Tupac"])
print(Pukkelpop.generate_event_summary())