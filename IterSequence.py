from datetime import timedelta, date

class DateRangeIterable:
  def __init__(self, start_date, end_date):
    self.start_date = start_date
    self.end_date = end_date 
    self._present_day = start_date 

  def __iter__(self):
    current_day = self.start_date 
    while current_day < self.end_date:
      yield current_day 
      current_day += timedelta(days=1)
      
  def __next__(self):
    if self._present_day >= self.end_date:
      raise StopIteration()
    today = self._present_day
    self._present_day += timedelta(days=1)
    return today 

#r1 = DateRangeIterable(date(2023,6,4), date(2023, 8,13))
#print(", ".join(map(str, r1)))
#print(max(r1))

class DateRangeSequence:
  def __init__(self, start_date, end_date):
    self.start_date = start_date 
    self.end_date = end_date 
    self._range = self._create_range() 

  def _create_range(self):
    days = []
    current_day = self.start_date 
    while current_day < self.end_date:
      days.append(current_day)
      current_day += timedelta(days=1)
    return days 

  def __getitem__(self, day_no):
    return self._range[day_no] 

  def __len__(self):
    return len(self._range)

s1 = DateRangeSequence(date(2023,6,4), date(2023,7,6))
for day in s1:
  print(day)
