total_seats = 40
available_seats = total_seats
tickets_sold = 0

print(f"Available seats: {available_seats}")

while available_seats > 0:
    tickets = int(input("Enter number of tickets to book (0 to exit): "))

    if tickets == 0:
        print("Exiting booking system.")
        break
    elif tickets <= available_seats:
        available_seats -= tickets
        tickets_sold += tickets
        print(f"Booking confirmed. Seats left: {available_seats}")
    else:
        print(f"Cannot book {tickets} ticket(s). Only {available_seats} seat(s) left.")

if available_seats == 0:
    print("Bus Full. No more bookings can be made.")

print(f"\nTotal tickets sold: {tickets_sold}")
print(f"Total seats remaining: {available_seats}")
