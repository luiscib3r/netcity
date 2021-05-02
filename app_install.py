

from install.models.x_rent_house import install_x_rent_house
from install.models.x_telegram_user import install_x_telegram_user

from install.actions.x_rent_house_action import install_x_rent_house_action
from install.actions.x_telegram_user_action import install_x_telegram_user_action

from install.menus.netcity_menu import install_netcity_menu
from install.menus.x_rent_house_menu import install_x_rent_house_menu
from install.menus.x_telegram_user_menu import install_x_telegram_user_menu

from install.views.x_rent_house_view import install_x_rent_house_view
from install.views.x_telegram_user_view import install_x_telegram_user_view

if __name__ == "__main__":
    # Install models
    install_x_telegram_user()
    install_x_rent_house()

    # Install actions
    install_x_telegram_user_action()
    install_x_rent_house_action()

    # Install menus
    install_netcity_menu()
    install_x_telegram_user_menu()
    install_x_rent_house_menu()

    # Install views
    install_x_telegram_user_view()
    install_x_rent_house_view()
