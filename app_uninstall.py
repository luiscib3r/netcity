from install.models.x_rent_house import uninstall_x_rent_house
from install.models.x_telegram_user import uninstall_x_telegram_user

from install.actions.x_rent_house_action import uninstall_x_rent_house_action
from install.actions.x_telegram_user_action import uninstall_x_telegram_user_action

from install.menus.netcity_menu import uninstall_netcity_menu
from install.menus.x_rent_house_menu import uninstall_x_rent_house_menu
from install.menus.x_telegram_user_menu import uninstall_x_telegram_user_menu

from install.views.x_rent_house_view import uninstall_x_rent_house_view
from install.views.x_telegram_user_view import uninstall_x_telegram_user_view

if __name__ == "__main__":
    # Remove views
    uninstall_x_rent_house_view()
    uninstall_x_telegram_user_view()

    # Remove menus
    uninstall_x_rent_house_menu()
    uninstall_x_telegram_user_menu()
    uninstall_netcity_menu()

    # Remove actions
    uninstall_x_rent_house_action()
    uninstall_x_telegram_user_action()

    # Remove models
    uninstall_x_rent_house()
    uninstall_x_telegram_user()
