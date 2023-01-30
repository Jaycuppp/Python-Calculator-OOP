import datetime
from datetime import date

Reused_Exception_Quote = 'Invalid Number. Please Enter A Valid Amount Of Clients'


class Sales_Tasks_Data():
    def Total_Prospective_Clients_Outreached():
        # User Input For Some Common Outcomes After Outreaching A Prospective Client
        try:
            Rejection = int(input("Total Clients That Gave A Rejection From The Sales Pitch: "))

        except:
            Rejection = int(input(f"{Reused_Exception_Quote} That Give A Rejection: "))

        try:
            No_Resopnse = int(input("Total Clients That Did Not Respond To Outreach: "))

        except:
            No_Resopnse = int(input(f"{Reused_Exception_Quote} That Did Not Respond"))

        try:
            Hung_Up_Phone = int(input("Total Clients That Hung Up The Phone Before Sale: "))

        except:
            Hung_Up_Phone = int(input(f"{Reused_Exception_Quote} That Hung Up The Phone Before Sale: "))

        try:
            Potential_Client = int(input("Total Clients That Are Potential Clients: "))

        except:
            Potential_Client = int(input(f"{Reused_Exception_Quote} That Are Potential Clients: "))


        # Sum Calculation from all Inputed Data
        Total = Rejection + No_Resopnse + Hung_Up_Phone + Potential_Client

        # First Part Of Progress Calculation
        Total_Clients_From_Weekly_List = int(input("What is the total number of Prospective Clients from Weekly List? "))
        Remaining_Calls = Total_Clients_From_Weekly_List - Total

        # Final Message Result To Give Progress
        print(f"As of {date.today()}")
        print(f"Prospective Clients Outreached So Far: {Total}")
        print(f"Remaining Prospective Clients To Outreach: {Remaining_Calls}")

    def Total_Inactive_Clients_Outreached():
        # User Input For Some Common Outcomes After Outreaching An Inactive Client
        try:
            Close_Account = int(input("Total Clients That Want To Close Their Account: "))

        except:
            Close_Account = int(input(f"{Reused_Exception_Quote} That Want To Close Their Account: "))

        try:
            No_Respopnse = int(input("Total Clients That Did Not Respond To Outreach: "))

        except:
            No_Respopnse = int(input(f"{Reused_Exception_Quote} That Did Not Respond To Outreach: "))

        try:
            Keep_Account = int(input("Total Clients That Want To Keep Their Account: "))

        except:
            Keep_Account = int(input(f"{Reused_Exception_Quote} That Want To Keep Their Account: "))

        try:
            Potential_Client = int(input("Total Clients That Are Potential Clients: "))

        except:
            Potential_Client = int(input(f"{Reused_Exception_Quote} That Are Potential Clients: "))

        try:
            Business_Closed = int(input("Total Clients That Have Closed Their Business: "))

        except:
            Business_Closed = int(input(f"{Reused_Exception_Quote} That Have Closed Their Business: "))

        # Sum Calculation from all Inputed Data
        Total = Close_Account + No_Respopnse + Keep_Account + Potential_Client + Business_Closed

        # First Part Of Progress Calculation
        Total_Clients_From_Weekly_List = int(input("What is the total number of Inactive Clients from Weekly List?"))
        Remaining_Calls = Total_Clients_From_Weekly_List - Total

        # Final Message Result To Give Progress
        print(f"As of {date.today()}")
        print(f"Inactive Clients Outreached So Far: {Total}")
        print(f"Remaining Inactive Clients To Outreach: {Remaining_Calls}")

    def Total_Sales_Made():
        Total_Leads_Closed = int(input("How many clients have you made a sale for today? "))
        List = list()

        for i in range(0, Total_Leads_Closed):
            try:
                Sale_Made = float(input("Record your sale made: "))
                List.append(Sale_Made)
                i += 1
            except:
                print("Sorry only enter a value without any other characters like $")
                Sale_Made = float(input("Record your sale made: "))
                List.append(Sale_Made)
                i += 1

        print(f"Here is a wide look of all the Sales You Made {List}")

        for index in range(0, len(List)):
            if index <= len(List):
                Total = sum(List)
                index += 1

        print(f"The Total Amount of Sales You Made Today is ${Total}")


Sales_Tasks_Data.Total_Prospective_Clients_Outreached()
Sales_Tasks_Data.Total_Inactive_Clients_Outreached()
Sales_Tasks_Data.Total_Sales_Made()