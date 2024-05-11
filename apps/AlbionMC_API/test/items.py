from colorama import Fore, Style

from src.factory.item_factory import Adepts_Soldier_Boots
from src.service.calculator.items import selector


def testItems():
    print(Fore.MAGENTA, selector(Adepts_Soldier_Boots()), Style.RESET_ALL)

if __name__ == "__main__":
    testItems()