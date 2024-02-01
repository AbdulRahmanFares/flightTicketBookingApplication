# Flight Ticket Booking Application - ZOHO Advanced Programming Question

flightList = [1, 2]
flight1TicketsCount = 50
flight1TicketsRate = 5000
flight2TicketsCount = 50
flight2TicketsRate = 5000
passengerIdGenerate = 0
passengerListForFlight1 = {}
passengerListForFlight2 = {}
passengerId = 0

# Function to book, cancel, or print tickets
def bookFlight():
    global flightList, flight1TicketsCount, flight1TicketsRate, flight2TicketsCount, flight2TicketsRate
    global passengerIdGenerate, passengerListForFlight1, passengerListForFlight2, passengerId

    option = int(input("1. Book 2. Cancel 3. Print\n"))

    # Booking Tickets
    if (option == 1):
        flightId = int(input("Enter flight Id\n"))
        if (flightId in flightList):
            if (flightId == 1):
                # Booking for Flight 1
                print("Flight Id 1 -- Remaining tickets " + str(flight1TicketsCount) + " -- Current ticket price " + str(flight1TicketsRate))
                numberOfTickets = int(input("Enter number of tickets\n"))
                if (flight1TicketsCount - numberOfTickets >= 0):
                    # Successful booking
                    costOfBookedTickets = numberOfTickets * flight1TicketsRate
                    flight1TicketsCount -= numberOfTickets
                    flight1TicketsRate = (numberOfTickets * 200) + flight1TicketsRate
                    print("Booked successfully!")
                    print("Flight Id 1 -- Remaining tickets " + str(flight1TicketsCount) + " -- Current ticket price " + str(flight1TicketsRate))
                    passengerIdGenerate += 1
                    passengerListForFlight1[passengerIdGenerate] = [numberOfTickets, costOfBookedTickets]
                    print("Flight Id 1 ->\nPassenger Id " + str(passengerIdGenerate) + " -- Number of tickets booked " + str(numberOfTickets) + " -- Total cost " + str(costOfBookedTickets))
                    bookFlight()
            else:
                # Booking for Flight 2
                print("Flight Id 2 -- Remaining tickets " + str(flight2TicketsCount) + " -- Current ticket price " + str(flight2TicketsRate))
                numberOfTickets = int(input("Enter number of tickets\n"))
                if (flight2TicketsCount - numberOfTickets >= 0):
                    # Successful booking
                    costOfBookedTickets = numberOfTickets * flight2TicketsRate
                    flight2TicketsCount -= numberOfTickets
                    flight2TicketsRate = (numberOfTickets * 200) + flight2TicketsRate
                    print("Booked successfully!")
                    print("Flight Id 2 -- Remaining tickets " + str(flight2TicketsCount) + " -- Current ticket price " + str(flight2TicketsRate))
                    passengerIdGenerate += 1
                    passengerListForFlight2[passengerIdGenerate] = [numberOfTickets, costOfBookedTickets]
                    print("Flight Id 2 ->\nPassenger Id " + str(passengerIdGenerate) + " -- Number of tickets booked " + str(numberOfTickets) + " -- Total cost " + str(costOfBookedTickets))
                    bookFlight()
        else:
            print("Invalid flight Id!")
            bookFlight()
    
    # Printing Tickets
    if (option == 3):
        # Printing booked tickets for Flight 1
        print("Flight Id 1 ->")
        for key, value in passengerListForFlight1.items():
            print("Passenger Id " + str(key) + " -- Number of tickets booked " + str(value[0]) + " -- Total cost " + str(value[1]))
        
        # Printing booked tickets for Flight 2
        print("Flight Id 2 ->")
        for key, value in passengerListForFlight2.items():
            print("Passenger Id " + str(key) + " -- Number of tickets booked " + str(value[0]) + " -- Total cost " + str(value[1]))
        
        bookFlight()

    # Cancel
    if (option == 2):
        cancelInput = input("Enter flight Id and passenger Id to cancel booking\n")
        cancelInput = cancelInput.split()

        flightId = int(cancelInput[0])
        passengerId = int(cancelInput[1])

        if (flightId not in flightList):
            print("Invalid flight Id!")
            bookFlight()
        elif (flightId == 1):
            # Cancelling booking for Flight 1
            if (passengerId not in passengerListForFlight1):
                print("Passenger Id not found!")
                print("Flight Id 1 -- Remaining tickets " + str(flight1TicketsCount) + " -- Current ticket price " + str(flight1TicketsRate))
                print("Flight Id 1 ->")
                for key, value in passengerListForFlight1.items():
                    print("Passenger Id " + str(key) + " -- Number of tickets booked " + str(value[0]) + " -- Total cost " + str(value[1]))
                bookFlight()
            else:
                # Refund and cancellation for Flight 1
                print("Refund amount after cancel : " + str(passengerListForFlight1[passengerId][1]))
                print("Cancelled booked tickets successfully!")
                flight1TicketsCount += passengerListForFlight1[passengerId][0]
                flight1TicketsRate -= passengerListForFlight1[passengerId][0] * 200
                print("Flight Id 1 -- Remaining tickets " + str(flight1TicketsCount) + " -- Current ticket price " + str(flight1TicketsRate))
                print("Flight Id 1 ->")
                passengerListForFlight1.pop(passengerId)
                for key, value in passengerListForFlight1.items():
                    print("Passenger Id " + str(key) + " -- Number of tickets booked " + str(value[0]) + " -- Total cost " + str(value[1]))
                bookFlight()
        elif(flightId == 2):
            # Cancelling booking for Flight 2
            if (passengerId not in passengerListForFlight2):
                print("Passenger Id not found!")
                print("Flight Id 2 -- Remaining tickets " + str(flight2TicketsCount) + " -- Current ticket price " + str(flight2TicketsRate))
                print("Flight Id 2 ->")
                for key, value in passengerListForFlight2.items():
                    print("Passenger Id " + str(key) + " -- Number of tickets booked " + str(value[0]) + " -- Total cost " + str(value[1]))
                bookFlight()
            else:
                # Refund and cancellation for Flight 2
                print("Refund amount after cancel : " + str(passengerListForFlight2[passengerId][1]))
                print("Cancelled booked tickets successfully!")
                flight2TicketsCount += passengerListForFlight2[passengerId][0]
                flight2TicketsRate -= passengerListForFlight2[passengerId][0] * 200
                print("Flight Id 2 -- Remaining tickets " + str(flight2TicketsCount) + " -- Current ticket price " + str(flight2TicketsRate))
                print("Flight Id 2 ->")
                passengerListForFlight2.pop(passengerId)
                for key, value in passengerListForFlight2.items():
                    print("Passenger Id " + str(key) + " -- Number of tickets booked " + str(value[0]) + " -- Total cost " + str(value[1]))
                bookFlight()

# Initial call to the function
bookFlight()

