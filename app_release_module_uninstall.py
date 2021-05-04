from install.views.x_app_release_view import uninstall_x_app_release_view
from install.menus.x_app_release_menu import uninstall_x_app_release_menu
from install.actions.x_app_release_action import uninstall_x_app_release_action
from install.models.x_app_release import uninstall_x_app_release


if __name__ == "__main__":
    # Remove views
    uninstall_x_app_release_view()

    # Remove menus
    uninstall_x_app_release_menu()

    # Remove actions
    uninstall_x_app_release_action()

    # Remove models
    uninstall_x_app_release()
