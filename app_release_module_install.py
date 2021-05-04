from install.models.x_app_release import install_x_app_release
from install.actions.x_app_release_action import install_x_app_release_action
from install.menus.x_app_release_menu import install_x_app_release_menu
from install.views.x_app_release_view import install_x_app_release_view

if __name__ == "__main__":
    # Install models
    install_x_app_release()

    # Install actions
    install_x_app_release_action()

    # Install menus
    install_x_app_release_menu()

    # Install views
    install_x_app_release_view()
