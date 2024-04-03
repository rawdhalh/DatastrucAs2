from classes import Ticket, VisitorCategory, EventType, Event

def test_ticket_purchase():
    # Create an event
    musical_concert = Event("Musical Concert", EventType.MUSICAL_CONCERTS, "Concert Hall")

    # Purchase tickets for individuals
    adult_ticket = Ticket("T001", 63.0, "2024-04-02", 0)  # Adult ticket price is 63 AED
    child_ticket = Ticket("T002", 0, "2024-04-02", 0)     # Child ticket is free
    student_ticket = Ticket("T003", 0, "2024-04-02", 0)   # Student ticket is free
    senior_ticket = Ticket("T004", 0, "2024-04-02", 0)    # Senior citizen ticket is free

    # Calculate prices for individual tickets
    adult_ticket_price = adult_ticket.calculate_price()
    child_ticket_price = child_ticket.calculate_price()
    student_ticket_price = student_ticket.calculate_price()
    senior_ticket_price = senior_ticket.calculate_price()

    # Print prices for individual tickets
    print("Adult Ticket Price:", adult_ticket_price)
    print("Child Ticket Price:", child_ticket_price)
    print("Student Ticket Price:", student_ticket_price)
    print("Senior Citizen Ticket Price:", senior_ticket_price)

    # Purchase tickets for a tour group (10 members)
    group_ticket = Ticket("T005", 63.0, "2024-04-02", 50)  # Group ticket price with 50% discount

    # Calculate price for the group ticket
    group_ticket_price = group_ticket.calculate_price()

    # Print price for the group ticket
    print("Group Ticket Price:", group_ticket_price)

if __name__ == "__main__":
    test_ticket_purchase()
