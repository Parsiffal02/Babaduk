def validate_password(password):
  if len(password)<7:
    return 
  has_uppercase = False
  has_lowercase = False
  has_digit = False

  for char in password:
    if char.isupper():
      has_uppercase = True
    elif char.islower():
      has_lowercase = True
    elif char.isdigit():
      has_digit = True

  conditions_not_met = []
  if not has_uppercase:
    conditions_not_met.append('Пароль должен содержать хотя бы одну букву в верхнем регистре.')
  if not has_lowercase:
    conditions_not_met.append('Пароль должен содержать хотя бы одну букву в нижнем регистре.')
  if not has_digit:
    conditions_not_met.append('Пароль должен содержать хотя бы одну цифру.')

  if conditions_not_met:
    return conditions_not_met
  else:
    return "Пароль верный!"

user_password=input('Введите пароль: ')

result = validate_password(user_password)

if isinstance(result, str):
  print(result)
else:
  print('Пароль не удовлетворяет следующим требованиям:')
  for condition in result:
    print(condition)