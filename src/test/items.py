from colorama import Fore, Style

from ..backend.factory.item_factory import Adepts_Soldier_Boots
from ..backend.service.item_service import selector

def testItems():
    print(Fore.MAGENTA, selector(Adepts_Soldier_Boots()), Style.RESET_ALL)

if __name__ == "__main__":
    testItems()