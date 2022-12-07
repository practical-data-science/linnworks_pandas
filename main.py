import settings_local as settings
from linnworks_pandas import auth
from linnworks_pandas import query

# Configure API credentials
auth.set_application_id(settings.APPLICATION_ID)
auth.set_application_secret(settings.APPLICATION_SECRET)
auth.set_token(settings.TOKEN)

# Fetch an authentication token
token = auth.authenticate()

# Run the "Get Order Totals Between Dates" Query Data report
df_order_totals = query.get_order_totals_between_dates('2022-12-06', '2022-12-06', verbose=False)
print(df_order_totals)

# Run the "Get Order Between Dates" Query Data report
df_orders = query.get_orders_between_dates('2022-12-06', '2022-12-06', verbose=False)
print(df_orders.head(3))

# Run the "Get Order Details Between Dates" Query Data report
df_order_details = query.get_order_details_between_dates('2022-12-06', '2022-12-06', verbose=False)
print(df_order_details.head(3))


