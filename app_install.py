

from install.models.x_rent_house import install_x_rent_house
from install.actions.x_rent_house_action import install_x_rent_house_action
from install.menus.x_rent_house_menu import install_x_rent_house_menu

if __name__ == "__main__":
    # Install models
    install_x_rent_house()

    # Install actions
    install_x_rent_house_action()

    # Install menus
    install_x_rent_house_menu()
