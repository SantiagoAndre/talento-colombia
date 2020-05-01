

def is_company_user(user):
  return user.is_superuser or user.is_company
  
