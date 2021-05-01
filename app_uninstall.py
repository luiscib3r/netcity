from install.models.x_rent_house import uninstall_x_rent_house
from install.actions.x_rent_house_action import uninstall_x_rent_house_action
from install.menus.x_rent_house_menu import uninstall_x_rent_house_menu
from install.views.x_rent_house_view import uninstall_x_rent_house_view

if __name__ == "__main__":
    # Remove views
    uninstall_x_rent_house_view()

    # Remove menus
    uninstall_x_rent_house_menu()

    # Remove actions
    uninstall_x_rent_house_action()

    # Remove models
    uninstall_x_rent_house()
