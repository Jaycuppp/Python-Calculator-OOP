import datetime
from datetime import date


class Sales_Tasks_Data():
    def Total_Prospective_Clients_Outreached():
        # User Input For Some Common Outcomes After Outreaching A Prospective Client
        Rejection = int(input("Total Clients That Gave A Rejection From The Sales Pitch: "))
        No_Respopnse = int(input("Total Clients That Did Not Respond To Outreach: "))
        Hung_Up_Phone = int(input("Total Clients That Hung Up The Phone Before Sale: "))
        Potential_Client = int(input("Total Clients That Are Potential Clients: "))

        # Sum Calculation from all Inputed Data
        Total = Rejection + No_Respopnse + Hung_Up_Phone + Potential_Client

        # First Part Of Progress Calculation
        Total_Clients_From_Weekly_List = int(input("What is the total number of Prospective Clients fro Weekly List? "))
        Remaining_Calls = Total_Clients_From_Weekly_List - Total

        # Final Message Result To Give Progress
        print(f"As of {date.today()}")
        print(f"Prospective Clients Outreached So Far: {Total}")
        print(f"Remaining Prospective Clients To Outreach: {Remaining_Calls}")

    def Total_Inactive_Clients_Outreached():
        # User Input For Some Common Outcomes After Outreaching An Inactive Client
        Close_Account = int(input("Total Clients That Want To Close Their Account: "))
        No_Respopnse = int(input("Total Clients That Did Not Respond To Outreach: "))
        Keep_Account = int(input("Total Clients That Want To Keep Their Account: "))
        Potential_Client = int(input("Total Clients That Are Potential Clients: "))
        Business_Closed = int(input("Total Clients That Have Closed Their Business: "))

        # Sum Calculation from all Inputed Data
        Total = Close_Account + No_Respopnse + Keep_Account + Potential_Client + Business_Closed

        # First Part Of Progress Calculation
        Total_Clients_From_Weekly_List = int(input("What is the total number of Inactive Clients from Weekly List? "))
        Remaining_Calls = Total_Clients_From_Weekly_List - Total

        # Final Message Result To Give Progress
        print(f"As of {date.today()}")
        print(f"Inactive Clients Outreached So Far: {Total}")
        print(f"Remaining Inactive Clients To Outreach: {Remaining_Calls}")

    def Total_Sales_Made():
        Total_Leads_Closed = int(input("How many clients have you made a sale for today? "))
        List = []

        for i in range(0, Total_Leads_Closed):
            Sale_Made = int(input("Record your sale made: "))
            List.append(Sale_Made)
            i += 1

        print(f"Here is a wide look of all the Sales You Made {List}")

        for index in range(0, len(List)):
            if index <= len(List):
                Total = sum(List)
                index += 1

        print(f"The Total Amount of Sales You Made Today is {Total}")


Sales_Tasks_Data.Total_Prospective_Clients_Outreached()
Sales_Tasks_Data.Total_Inactive_Clients_Outreached()
Sales_Tasks_Data.Total_Sales_Made()
