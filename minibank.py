from typing import Union

# Global variables
name: Union[str, None] = None
balance: Union[float, None] = None

def open_account() -> None:
    """Opens a new account.

    Prompts the user to enter their name and initializes the account balance to 0.0.
    """
    global name, balance
    name = input("name = ")
    balance = 0.0

def check_account() -> bool:
    """Checks if the account is open.

    Returns:
        bool: True if the account exists (name and balance are not None), otherwise False.
    """
    return name is not None and balance is not None

def deposit() -> None:
    """Adds funds to the current balance.

    Prompts the user to enter the amount they wish to deposit and updates the balance.

    Raises:
        ValueError: If the input cannot be converted to a float.
    """
    global balance
    amount = float(input("Qo'shiladigan summani kiriting: "))
    balance += amount

def withdraw() -> None:
    """Withdraws funds from the current balance.

    Prompts the user to enter the amount they wish to withdraw and updates the balance.

    Raises:
        ValueError: If the input cannot be converted to a float.
    """
    global balance
    amount = float(input("Yechiladigan summani kiriting: "))
    balance -= amount

def check_balance() -> None:
    """Displays the current balance."""
    print(f"Hozirgi balans: {balance} so'm")

def main() -> None:
    """Main function to run the ATM menu system.

    Provides a simple text-based interface for account creation, balance checking,
    deposits, and withdrawals.
    """
    while True:
        print("\n=== ATM Menyusi ===")
        print("0 - Account yaratish")
        print("1 - Balansni ko'rish")
        print("2 - Pul qo'shish (deposit)")
        print("3 - Pul yechish (withdraw)")
        print("4 - Chiqish")

        tanlov = input("Amalni tanlang (0-4): ")

        if tanlov == "0":
            open_account()
        elif tanlov == "1":
            if check_account():
                check_balance()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "2":
            if check_account():
                deposit()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "3":
            if check_account():
                withdraw()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "4":
            print("Dasturdan chiqildi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov! Iltimos, qaytadan urinib ko'ring.")

# Dastur ishga tushiriladi
main()

 