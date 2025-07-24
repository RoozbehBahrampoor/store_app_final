from model.entity.admin import Admin
from model.repository.admin_repository import AdminRepository

admin_1 = Admin(1, "ali", "hosseini", "alihosseini123", "ali456", "alii1234", )

admin_1.name = "reza"

print(admin_1)

admin_repo = AdminRepository()
admin_repo.save(admin_1)
