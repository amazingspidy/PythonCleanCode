from collections.abc import Mapping


class Event:

  def __init__(self, raw_data):
    self.raw_data = raw_data

  @staticmethod
  def meets_condition(event_data: dict) -> bool:
    return False

  @staticmethod
  def validate_precondition(event_data: dict):
    '''event_data 파라미터가 적절한 형태인지 유효성 검사'''

    if not isinstance(event_data, Mapping):
      raise ValueError(f"{event_data!r} dict 데이터 타입이 아님!")
    for moment in ("before", "after"):
      if moment not in event_data:
        raise ValueError(f"{event_data}에 {moment} 정보가 없음!")

      if not isinstance(event_data[moment], Mapping):
        raise ValueError(f"event_data[{moment!r}] dict 데이터 타입이 아님!")


class UnknownEvent(Event):
  '''데이터만으로 식별할 수 없는 이벤트'''


class TransactionEvent(Event):
  '''시스템에서 발생한 트랜잭션 이벤트'''

  @staticmethod
  def meets_condition(event_data: dict) -> bool:
    return event_data["after"].get("transaction") is not None


class LoginEvent(Event):

  @staticmethod
  def meets_condition(event_data: dict):
    return (event_data["before"]["session"] == 0
            and event_data["after"]["session"] == 1)


class LogoutEvent(Event):

  @staticmethod
  def meets_condition(event_data: dict):
    return (event_data["before"]["session"] == 1
            and event_data["after"]["session"] == 0)


class SystemMonitor:
  '''시스템에서 발생한 이벤트 분류'''

  def __init__(self, event_data):
    self.event_data = event_data

  def identify_event(self):
    Event.validate_precondition(self.event_data)
    event_cls = next(
      (event_cls for event_cls in Event.__subclasses__()
       if event_cls.meets_condition(self.event_data)),
      UnknownEvent,
    )
    return event_cls(self.event_data)


l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
print(l1.identify_event().__class__.__name__)
l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
print(l2.identify_event().__class__.__name__)
l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
print(l3.identify_event().__class__.__name__)
l4 = SystemMonitor({"before": {}, "after": {"transaction": "Tx001"}})
print(l4.identify_event().__class__.__name__)
