from controller.admin_controller import AdminController
from model.entity.admin import Admin
from model.repository.admin_repository import AdminRepository

#
# admin_1 = Admin(1, "parsa", "hosseini", "alihosseini123", "ali456", "alii1234", 1)

# print(admin_1)
admin_controller = AdminController()
# admin_repo = AdminRepository()

# Test Passed
# admin_repo.save(admin_1)
# status, message = (admin_controller.save(2, "akbar", "ahmadi", "akbarahmadi45", "akbar_ah14", "alii1234", 1))

# Test Passed
# admin_repo.edit(admin_1)
# status, message = (admin_controller.edit(2, "akbar", "ahmadi", "akbarahmadi45", "akbar_ah14", "alii1234", 1))

# Test Passed
# admin_repo.delete(1)
# status, message = (admin_controller.delete(2))

# Test Passed
# print(admin_repo.find_all())

# Test Passed
# print(admin_repo.find_by_code(55))

# Not Working
# print(admin_repo.find_by_username("alihosseini123"))

# Not Working
# print(admin_repo.find_by_username("reza"))

# Test Passed
# print(admin_repo.find_by_username_and_password("ahmad222", "ahmad456"))
