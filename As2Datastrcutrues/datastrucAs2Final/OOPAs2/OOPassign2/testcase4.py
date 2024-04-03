from classes import Ticket, VisitorCategory, EventType, Event

def display_payment_receipt(tickets):
    total_price = 0
    print("Payment Receipt:")
    for ticket in tickets:
        print(f"Ticket ID: {ticket.get_ticket_id()}")
        print(f"Price: {ticket.get_price()} AED")
        print("------------------------------")
        total_price += ticket.get_price()
    print(f"Total Price: {total_price} AED")

def test_payment_receipt_display():
    # Purchase tickets for individuals
    adult_ticket = Ticket("T001", 63.0, "2024-04-02", 0)  # Adult ticket price is 63 AED
    child_ticket = Ticket("T002", 0, "2024-04-02", 0)     # Child ticket is free

    # Display payment receipt for individual tickets
    display_payment_receipt([adult_ticket, child_ticket])

    # Purchase tickets for a tour group (10 members)
    group_tickets = [Ticket(f"T00{i}", 63.0, "2024-04-02", 50) for i in range(3, 13)]  # Group ticket price with 50% discount

    # Display payment receipt for group tickets
    display_payment_receipt(group_tickets)

if __name__ == "__main__":
    test_payment_receipt_display()
