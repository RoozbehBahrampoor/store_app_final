from model.entity.admin import Admin
from model.repository.admin_repository import AdminRepository


class AdminController:

    def save(self, code, name, family, email,  username, password, locked):
        try:
            admin = Admin(code, name, family, email, username, password, locked)
            admin_repo = AdminRepository()
            admin_repo.save(admin)
            return True, f"Admin saved {admin}"
        except Exception as e:
            return False, "Error saving admin {e}"


    # def edit(self, admin):

    # def delete(self, code):

    # def find_all(self):


    # def find_by_code(self, code):


    # def find_by_name_family(self, name, family):


    # def find_by_username(self, username):


    # def find_by_username_and_password(self, username, password):

