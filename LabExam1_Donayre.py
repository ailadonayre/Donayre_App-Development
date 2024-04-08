from datetime import datetime
import string
import random

ref_no = ""
date_time = ""
cond_name = ""
orig_dest = ""
orig_pt = 0
dest_pt = 0
baraco_tix = 0
baraco_disc = 0
baraco_tix_disc = 0

baraco_stations = {"1": "Batangas City",
                   "2": "Ibaan",
                   "3": "Rosario",
                   "4": "San Juan",
                   "5": "Lobo"}

routes_km = {"1-2": 16.3, "1-3": 23.6, "1-4": 35.3, "1-5": 39.9,
             "2-1": 16.3, "2-3": 14.5, "2-4": 23.5, "2-5": 42.6,
             "3-1": 23.6, "3-2": 14.5, "3-4": 27.7, "3-5": 41.8,
             "4-1": 35.3, "4-2": 23.5, "4-3": 27.7, "4-5": 38.6,
             "5-1": 39.9, "5-2": 42.6, "5-3": 41.8, "5-4": 38.6}

routes_qty = {"1-2": 0, "1-3": 0, "1-4": 0, "1-5": 0,
            "2-1": 0, "2-3": 0, "2-4": 0, "2-5": 0,
            "3-1": 0, "3-2": 0, "3-4": 0, "3-5": 0,
            "4-1": 0, "4-2": 0, "4-3": 0, "4-5": 0,
            "5-1": 0, "5-2": 0, "5-3": 0, "5-4": 0}

baraco_rcp = {}

total_routes = []

total_sales = []

def view_stations(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc):
    print("_" * 150, "\n")
    stations_title = "BARACO Stations"
    print(stations_title.center(150), "\n")

    i = 1
    for stations in baraco_stations.values():
        print(f"{i}. {stations}")
        i += 1

    while True:
        try:
            choice = str(input("\n> Would you like to go back to the main menu? (Y/N) "))
            if choice == 'Y' or choice == 'y':
                main_menu(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                break
            elif choice == 'N' or choice == 'n':
                view_stations(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                break
            else:
                print("\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\t>> [ValueError] Invalid input. Please try again.")
            view_stations(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)

def select_route(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc):
    baraco_tix = 0
    baraco_disc = 0
    baraco_tix_disc = 0

    print("_" * 150, "\n")
    route_title = "Select BARACO Route"
    print(route_title.center(150), "\n")

    i = 1
    for stations in baraco_stations.values():
        print(f"{i}. {stations}")
        i += 1

    try:
        cond_name = str(input("\n> Kindly enter your name: ")).upper().title()
    except ValueError:
            print("\t>> [ValueError] Invalid input. Please try again.")
            view_stations(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)

    while True:
        try:
            orig_pt = str(input("\n> Kindly select the numerical input corresponding to your origin point: "))
            dest_pt = str(input("> Kindly select the numerical input corresponding to your destination point: "))
            orig_dest = orig_pt + "-" + dest_pt
            
            if orig_dest in routes_km.keys():
                baraco_tix = (5*abs(routes_km[f"{orig_dest}"] - 7))
                baraco_tix = int(baraco_tix) + bool(baraco_tix % 1)
                total_routes.append(routes_km[f'{orig_dest}'])
                routes_qty[f'{orig_dest}'] += 1

                print(f"\t>> The calculated distance from {baraco_stations[f'{orig_pt}']} to {baraco_stations[f'{dest_pt}']} is {routes_km[f'{orig_dest}']} kilometers.")
                
                while True:
                    try:
                        elig_disc = str(input("> Are you a senior citizen, PWD, or a student? (Y/N) "))
                        if elig_disc == 'Y' or elig_disc == 'y':
                            baraco_disc = (baraco_tix * 0.2)
                            baraco_tix_disc = baraco_tix - baraco_disc
                            total_sales.append(baraco_tix_disc)
                            print(f"\t>> Thank you for riding with BARACO. Your total ticketing fare with the 20% discount applied is Php {baraco_tix_disc:.2f}.")
                            
                            n = 10
                            ref_no = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
                            now = datetime.now()
                            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
                            
                            baraco_rcp[ref_no] = {"rcp_datetime": date_time, "rcp_cond": cond_name, "rcp_orig": orig_pt, "rcp_dest": dest_pt, "rcp_tix": baraco_tix, 
                                                  "rcp_disc": baraco_disc, "rcp_tix_disc": baraco_tix_disc}
                            
                            print("_" * 75, "\n")
                            receipt_title = "BARACO Official Receipt"
                            print(receipt_title.center(75))
                            rline1 = "Batangas Railway Corporation"
                            print(rline1.center(75))
                            rline2 = f"Reference No.: {str(ref_no)}"
                            print(rline2.center(75))
                            rline3 = f"Date and Time: {date_time}"
                            print(rline3.center(75))
                            rline4 = f"Conductor: {cond_name}"
                            print(rline4.center(75))
                            rline5 = f"From: {baraco_stations[f'{orig_pt}']}"
                            print(rline5.center(75))
                            rline6 = f"To: {baraco_stations[f'{dest_pt}']}"
                            print(rline6.center(75))
                            rline7 = f"Regular: Php {baraco_tix:.2f}"
                            print(rline7.center(75))
                            rline8 = f"Discount: Php {baraco_disc:.2f}"
                            print(rline8.center(75))
                            rline9 = f"Total Amount: Php {baraco_tix_disc:.2f}"
                            print(rline9.center(75))
                            print("_" * 75)

                            break
                        elif elig_disc == 'N' or elig_disc == 'n':
                            total_sales.append(baraco_tix)
                            print(f"\t>> Thank you for riding with BARACO. Your total ticketing fare is Php {baraco_tix:.2f}.")
                            
                            n = 10
                            ref_no = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
                            now = datetime.now()
                            date_time = now.strftime("%d/%m/%Y %H:%M:%S")

                            baraco_rcp[ref_no] = {"rcp_datetime": date_time, "rcp_cond": cond_name, "rcp_orig": orig_pt, "rcp_dest": dest_pt, "rcp_tix": baraco_tix, 
                                                  "rcp_disc": baraco_disc}

                            print("_" * 75, "\n")
                            receipt_title = "BARACO Official Receipt"
                            print(receipt_title.center(75))
                            rline1 = "Batangas Railway Corporation"
                            print(rline1.center(75))
                            rline2 = f"Reference No.: {str(ref_no)}"
                            print(rline2.center(75))
                            rline3 = f"Date and Time: {date_time}"
                            print(rline3.center(75))
                            rline4 = f"Conductor: {cond_name}"
                            print(rline4.center(75))
                            rline5 = f"From: {baraco_stations[f'{orig_pt}']}"
                            print(rline5.center(75))
                            rline6 = f"To: {baraco_stations[f'{dest_pt}']}"
                            print(rline6.center(75))
                            rline7 = f"Regular: Php {baraco_tix:.2f}"
                            print(rline7.center(75))
                            rline8 = f"Discount: Php {baraco_disc:.2f}"
                            print(rline8.center(75))
                            rline9 = f"Total Amount: Php {baraco_tix:.2f}"
                            print(rline9.center(75))
                            print("_" * 75)

                            break
                        else:
                            print("\t>> Invalid input. Please try again.")
                            continue
                    except ValueError:
                        print("\t>> [ValueError] Invalid input. Please try again.")
                        select_route(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
            else:
                print("\t>> Invalid input. Please try again.")
                continue
    
        except ValueError:
            print("\t>> [ValueError] Invalid input. Please try again.")
            select_route(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
        except KeyError:
            print("\t>> [KeyError] Invalid input. Please try again.")
            select_route(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
        
        break
    
    while True:
        try:
            choice = str(input("\n> Would you like to (a) book another ticket or (b) go back to the main menu? "))
            if choice == 'a' or choice == 'A':
                select_route(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                break
            elif choice == 'b' or choice == 'B':
                main_menu(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                break
            else:
                print("\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\t>> [ValueError] Invalid input. Please try again.")
            select_route(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)

def calc_dist(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc):
    print("_" * 150, "\n")
    dist_title = "Calculate Distance"
    print(dist_title.center(150))

    while True:
        print("\n1. Batangas City")
        print("2. Ibaan")
        print("3. Rosario")
        print("4. San Juan")
        print("5. Lobo")

        try:
            orig_pt = str(input("\n> Kindly select the numerical input corresponding to your origin point: "))
            dest_pt = str(input("> Kindly select the numerical input corresponding to your destination point: "))
            orig_dest = orig_pt + "-" + dest_pt
            
            if orig_dest in routes_km.keys():
                baraco_tix = (5*abs(routes_km[f"{orig_dest}"] - 7))
                baraco_tix = int(baraco_tix) + bool(baraco_tix % 1)

                print(f"\t>> The calculated distance from {baraco_stations[f'{orig_pt}']} to {baraco_stations[f'{dest_pt}']} is {routes_km[f'{orig_dest}']} kilometers.")
                break
            else:
                print("\t>> Invalid input. Please try again.")
                continue
    
        except ValueError:
            print("\t>> [ValueError] Invalid input. Please try again.")
            calc_dist(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
        except KeyError:
            print("\t>> [KeyError] Invalid input. Please try again.")
            calc_dist(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)

    while True:
        try:
            choice = str(input("\n> Would you like to go back to the main menu? (Y/N) "))
            if choice == 'Y' or choice == 'y':
                main_menu(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                break
            elif choice == 'N' or choice == 'n':
                calc_dist(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                break
            else:
                print("\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\t>> [ValueError] Invalid input. Please try again.")
            calc_dist(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)

def view_receipts(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc):
    print("_" * 150, "\n")
    rcp_title = "View BARACO Receipts"
    print(rcp_title.center(150))

    while True:
        try:
            rcp_no = str(input("\n> Kindly enter the reference number of the receipt that you would like to check: "))

            if rcp_no in baraco_rcp.keys():
                print("_" * 75, "\n")
                receipt_title = "BARACO Official Receipt"
                print(receipt_title.center(75))
                rline1 = "Batangas Railway Corporation"
                print(rline1.center(75))
                rline2 = f"Reference No.: {rcp_no}"
                print(rline2.center(75))
                rline3 = f"Date and Time: {baraco_rcp[rcp_no]['rcp_datetime']}"
                print(rline3.center(75))
                rline4 = f"Conductor: {baraco_rcp[rcp_no]['rcp_cond']}"
                print(rline4.center(75))
                rline5 = f"From: {baraco_stations[baraco_rcp[rcp_no]['rcp_orig']]}"
                print(rline5.center(75))
                rline6 = f"To: {baraco_stations[baraco_rcp[rcp_no]['rcp_dest']]}"
                print(rline6.center(75))
                rline7 = f"Regular: Php {baraco_rcp[rcp_no]['rcp_tix']:.2f}"
                print(rline7.center(75))
                rline8 = f"Discount: Php {baraco_rcp[rcp_no]['rcp_disc']:.2f}"
                print(rline8.center(75))
                
                if 'rcp_tix_disc' in baraco_rcp[rcp_no]:
                    rline9 = f"Total Amount: Php {baraco_rcp[rcp_no]['rcp_tix_disc']:.2f}"
                    print(rline9.center(75))
                else:
                    rline9 = f"Total Amount: Php {baraco_rcp[rcp_no]['rcp_tix']:.2f}"
                    print(rline9.center(75))
                
                print("_" * 75)
            
            else:
                print("\t>> Reference number not found. Please try again.")
                continue

            break

        except ValueError:
            print("\t>> [ValueError] Invalid input. Please try again.")
            view_receipts(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
        except KeyError:
            print("\t>> [KeyError] Invalid input. Please try again.")
            view_receipts(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)

    while True:
        try:
            choice = str(input("\n> Would you like to go back to the main menu? (Y/N) "))
            if choice == 'Y' or choice == 'y':
                main_menu(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                break
            elif choice == 'N' or choice == 'n':
                view_receipts(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                break
            else:
                print("\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\t>> [ValueError] Invalid input. Please try again.")
            view_receipts(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)

def view_stats(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc):
    print("_" * 150, "\n")
    stats_title = "View BARACO Statistics"
    print(stats_title.center(150))
    stats_sub = "All data recorded below are refreshed upon the initialization of the application."
    print(stats_sub.center(150))

    print("\n> Total distance traveled:")
    total_km = sum(total_routes)
    print(f"\t>> {total_km:.2f} kilometers")

    print("\n> Total amount of ticket sales:")
    total_tix_sales = sum(total_sales)
    print(f"\t>> Php {total_tix_sales:.2f}")

    print("\n> Conductors:")
    if len(baraco_rcp) == 0:
        print("\t>> None")
    else:
        list_names = []
        
        for ref in baraco_rcp:
            list_names.append(baraco_rcp[ref]['rcp_cond'])
        
        new_list_names = []

        for names in list_names:
            if names not in new_list_names:
                new_list_names.append(names)
        
        for new_names in new_list_names:
            print(f"\t>> {new_names}")
    
    print("\n> Tally of bookings on routes:")
    sort_routes = sorted(routes_qty.items(), key = lambda x: x[1], reverse = True)
    for routes in sort_routes:
        print(f"\t>> {routes[0].replace('1', 'Batangas City').replace('2', 'Ibaan').replace('3', 'Rosario').replace('4', 'San Juan').replace('5', 'Lobo').replace('-', ' to ')}: {routes[1]}")

    while True:
        try:
            choice = str(input("\n> Would you like to go back to the main menu? (Y/N) "))
            if choice == 'Y' or choice == 'y':
                main_menu(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                break
            elif choice == 'N' or choice == 'n':
                view_stats(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                break
            else:
                print("\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\t>> [ValueError] Invalid input. Please try again.")
            view_stats(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)

def main_menu(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc):
    print("_" * 150, "\n")
    menu_title = "Welcome to BARACO!"
    print(menu_title.center(150))
    print("\nBatangas Railway Corporation or BARACO is the prospect of the province’s land transportation profile. The blueprint of the BARACO application ")
    print("is tested via Python, with inputs and outputs likewise displayed in the console. This application serves its purpose as an instrument for train ")
    print("conductors to calculate the ticketing fares of passengers to their destination points.")

    print("\nIn the early version of BARACO, only five (5) stations are built throughout the province to evaluate how its novelty impacts public transport users. ")
    print("These stations are located at Batangas City, Ibaan, Rosario, San Juan, and Lobo, in view of its circumferential geography.")

    print("\nDirectory")
    print("1. View BARACO Stations")
    print("2. Select BARACO Route")
    print("3. Calculate Distance")
    print("4. View BARACO Receipts")
    print("5. View BARACO Statistics")
    print("6. Exit")

    while True:
        try:
            choice = int(input("\n> Kindly select the numerical input corresponding to your choice: "))
            if choice == 1:
                view_stations(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                return
            elif choice == 2:
                select_route(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                return
            elif choice == 3:
                calc_dist(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                return
            elif choice == 4:
                view_receipts(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                return
            elif choice == 5:
                view_stats(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)
                return
            elif choice == 6:
                exit()
            else:
                print("\t>> Invalid input. Please choose from the directory above.")
                continue
        except ValueError:
            print("\t>> [ValueError] Invalid input. Please try again.")
            main_menu(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)

main_menu(ref_no, date_time, cond_name, orig_dest, orig_pt, dest_pt, baraco_tix, baraco_disc, baraco_tix_disc)