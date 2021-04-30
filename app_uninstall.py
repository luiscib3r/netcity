from install.models.x_rent_house import uninstall_x_rent_house
from install.actions.x_rent_house_action import uninstall_x_rent_house_action

if __name__ == "__main__":
    # Remove models
    uninstall_x_rent_house()

    # Remove actions
    uninstall_x_rent_house_action()
