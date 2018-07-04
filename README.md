# InspireNCMemberDatabase

**current work is occurring in the db folder**

go to:
127.0.0.1:8000/accounts
OR
localhost:8000/accounts

##TO SEE ADDED ACCOUNTS SORTED ALPHABETICALLY

navigate in cmd to **InspireNCMemberDatabase/db** ~~ex/examplesite~~

enter: **python manage.py runserver**

open browser and search **localhost:8000/db** to view accounts

##TO EDIT LIST:

GOTO: admin page

~~ex/examplesite/accounts/views.py~~ (Use this file to edit accounts)

##TO ADD SUPERUSER: _this is necessary for admin access_

navigate in cmd to **InspireNCMemberDatabase/db**

enter: **python manage.py createsuperuser**

##TO ADD ACCOUNT(using shell):

**InspireNCMemberDatabase/db** ~~ex/examplesite~~

enter: **python manage.py shell**

```
from accounts.models import Account

#to create account:
  myAccount = Account()

#to modify attributes
  myAccount.first_name = "John"
  myAccount.last_name = "Doe"
  myAccount.SlugField = "john-doe"

#After modifying account details
  account.save()

#to view all ACCOUNTS
  Account.objects.all()

```

##FOR ADMINS:

In browser: **localhost:8000/db/admin**

This can be used for a more UI friendly view method
