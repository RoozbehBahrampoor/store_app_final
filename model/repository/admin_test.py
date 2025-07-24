from model.entity.admin import Admin
from model.repository.admin_repository import AdminRepository

admin_1 = Admin(1, "parsa", "hosseini", "alihosseini123", "ali456", "alii1234",1)


# print(admin_1)

admin_repo = AdminRepository()

# Test Passed
# admin_repo.save(admin_1)

# Test Passed
# admin_repo.edit(admin_1)

# Test Passed
# admin_repo.delete(1)

# Test Passed
# print(admin_repo.find_all())

# Test Passed
# print(admin_repo.find_by_code(55))

print(admin_repo.find_by_username("alihosseini123"))

