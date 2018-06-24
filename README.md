# InspireNCMemberDatabase

ignore intial commit folder

go to:
127.0.0.1:8000/accounts
OR
localhost:8000/accounts

##TO SEE ADDED ACCOUNTS SORTED ALPHABETICALLY
navigate in cmd to **ex/examplesite**
enter: **python manage.py runserver**
open browser and search **localhost:8000/accounts** to view accounts


##TO EDIT LIST:
ex/examplesite/accounts/views.py (Use this file to edit accounts)

##TO ADD ACCOUNT:
ex/examplesite
enter: **python manage.py shell**

```
from accounts.models import Account

#to create account:
  myAccount = Account()

#to modify attributes
  myAccount.last_name = "Doe"

#After modifying account details
  account.save()

#to view all ACCOUNTS
  Account.objects.all()

```
