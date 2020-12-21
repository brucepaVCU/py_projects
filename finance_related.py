def display_as_percentage(val):
    #below we use whats in {} to put the value in percentage form for interest rates
  return '{:.1f}%'.format(val * 100)

# Write code here
def calculate_simple_return(start_price, end_price, dividend = 0):
  return