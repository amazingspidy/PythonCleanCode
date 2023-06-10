#Bad case
#문제점1: UserDict에서 필요하지 않은 기능들까지 다 포함. 
#문제점2: TransactionalPolicy라는 이름만 보고 dictionary type임을 알수가 없다.

import collections 
import datetime

class TransactionalPolicy(collections.UserDict):
  def change_in_policy(self, customer_id, **new_policy_data):
    self[customer_id].update(**new_policy_data)

policy = TransactionalPolicy({
  "client001": {
    "fee": 1000.0,
    "expiration_date": datetime.date(2023,6,5),
  }
})

#print(policy["client001"])
#policy.change_in_policy("client001", expiration_date = datetime.date(2023, 10, 9))
#print(policy["client001"])


#Good Case
#Using composition
class TransactionalPolicy_2:
  def __init__(self, policy_data, **extra_data):
    self._data = {**policy_data, **extra_data}

  def change_in_policy(self, customer_id, **new_policy_data):
    self._data[customer_id].update(**new_policy_data)

  def __getitem__(self, customer_id):
    return self._data[customer_id]

  def __len__(self):
    return len(self._data)

policy2 = TransactionalPolicy({
  "client001": {
    "fee": 1000.0,
    "expiration_date": datetime.date(2023,6,5),
  }
})
#print(policy2["client001"])
#policy2.change_in_policy("client001", expiration_date = datetime.date(2023, 10, 9))
#print(policy2["client001"])


class BaseTokenizer:
  def __init__(self, str_token):
    self.str_token = str_token 

  def __iter__(self):
    yield from self.str_token.split("-")

tk = BaseTokenizer("9890-132daf-qweo-ocvolx")
print(list(tk))

class UpperIterableMixin:
  def __iter__(self):
    return map(str.upper, super().__iter__())

class Tokenizer(UpperIterableMixin, BaseTokenizer): #mixin 하는 순서도 중요.
  """BaseTokenizer, UpperIterableMixin 순서로 하면 upper로 변환이 안됨."""
  pass 

tc = Tokenizer("12830-adfc-iweqw-zcxaf")
print(list(tc))

tu = UpperIterableMixin("abcd-iee")
print(list(tu))
