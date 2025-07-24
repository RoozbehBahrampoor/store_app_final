-- Save User
insert into admins
    (code, name, family, email, username, password, locked)
values
    (3, 'yousef', 'yousefi', 'yousef_sh','yousef456','yousef123', 0);
-- Search - Find
select *
from admins
where code = 1;

-- Edit
update admins set name=?, family=?, email=?, username=?, password=?, locked=?
where code=?;
-- Delete
delete from admins where code =1;