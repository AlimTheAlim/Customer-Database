import os
import Customer_list


class Admin_menu:
    def administrative_menu(customer_database):
        choice = ''
        while choice.lower() != 'q':
            print('Please enter option:')
            print('1. A to Add customer')
            print('2. R to Remove customer')
            print('3. E to Edit customer')
            print('4. S to Save customer list to file')
            print('5. Enter Q to quit')
            choice = input()

            try:
                if choice.lower() == 'a':
                    print('Please enter information, or type Q to go back')
                    new_name = input('Input name: ')
                    if new_name.lower() == 'q':
                        continue
                    new_phone = input('Input phone: ')
                    new_email = input('Input email: ')
                    new_customer = Customer_list.Customer(new_name, new_email, new_phone)
                    customer_database.add_customer(new_customer)
                    print("Customer added successfully!")

                elif choice.lower() == 'r':
                    print('Choose what value to look for?\n1. N for name\n2. P for phone\n3. E for email\n4. Q for back')
                    remove_choice = input('Enter what value you will look for: ')
                    if remove_choice.lower() == 'q':
                        continue
                    elif remove_choice.lower() == 'n':
                        remove_look_by_name = input('Enter name: ')
                        for customer in customer_database.customer_list:
                            if customer.get_customer_name() == remove_look_by_name:
                                customer_database.remove_customer(customer)
                                print("Customer removed successfully!")
                                break
                    elif remove_choice.lower() == 'p':
                        remove_look_by_phone = input('Enter phone: ')
                        for customer in customer_database.customer_list:
                            if customer.get_customer_phone() == remove_look_by_phone:
                                customer_database.remove_customer(customer)
                                print("Customer removed successfully!")
                                break
                    elif remove_choice.lower() == 'e':
                        remove_look_by_email = input('Enter email: ')
                        for customer in customer_database.customer_list:
                            if customer.get_customer_email() == remove_look_by_email:
                                customer_database.remove_customer(customer)
                                print("Customer removed successfully!")
                                break
                    else:
                        print('Non-existing option')

                elif choice.lower() == 'e':
                    print('Choose what value to look for?\n1. N for name\n2. P for phone\n3. E for email\n4. Q for back')
                    edit_choice = input('Enter what value you will look for? ')
                    if edit_choice.lower() == 'q':
                        continue
                    elif edit_choice.lower() == 'n':
                        edit_look_by_name = input('Enter name: ')
                        for customer in customer_database.customer_list:
                            if customer.get_customer_name() == edit_look_by_name:
                                new_name = input('Enter new name: ')
                                customer_database.edit_customer(customer, name=new_name)
                                print("Customer edited successfully!")
                                break
                    elif edit_choice.lower() == 'p':
                        edit_look_by_phone = input('Enter phone: ')
                        for customer in customer_database.customer_list:
                            if customer.get_customer_phone() == edit_look_by_phone:
                                new_phone = input('Enter new phone: ')
                                customer_database.edit_customer(customer, phone=new_phone)
                                print("Customer edited successfully!")
                            break
                    elif edit_choice.lower() == 'e':
                        edit_look_by_email = input('Enter email: ')
                        for customer in customer_database.customer_list:
                            if customer.get_customer_email() == edit_look_by_email:
                                new_email = input('Enter new email: ')
                                customer_database.edit_customer(customer, email=new_email)
                                print("Customer edited successfully!")
                                break
                    else:
                        print('Non-existing option')

                elif choice.lower() == 's':
                    customer_database.save_to_file()
                    print("Customer list saved successfully!")

                elif choice.lower() == 'q':
                    break
                else:
                    print('Non-existing option')
            except Exception as e:
                print('An error occurred:', e)


class User_menu:
    def user_menu(customer_database):
        customer_database.print_customer_list()


class Menu(User_menu, Admin_menu):
    def menu(customer_database):
        try:
            menu_choice = ''
            while menu_choice != 'q':
                menu_choice = input('Enter A for administrative mode, U for user, or Q for quit: ')
                if menu_choice.lower() == 'a':
                    Admin_menu.administrative_menu(customer_database)
                elif menu_choice.lower() == 'u':
                    User_menu.user_menu(customer_database)
                elif menu_choice.lower() == 'q':
                    break
                else:
                    print('Non-existing option')
        except Exception as e:
            print('An error occurred:', e)

if __name__ == '__main__':
    print('Welcome to the customer database system')
    Menu.menu(Customer_list.Customer_list())
