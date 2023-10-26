import pytd

# Define your Treasure Data API credentials
api_key = 'YOUR_API_KEY'
api_endpoint = 'https://api.treasuredata.com'

# Create a Treasure Data client
client = pytd.Client(api_endpoint=api_endpoint, apikey=api_key)

# Define the list of variable values you want to use in the query
variable_values = [1, 2, 3]

# Loop through the variable values and execute the query for each value
for value in variable_values:
    query = f"SELECT * FROM your_table WHERE id = {value}"

    # Execute the Presto query
    result = client.query('your_database', query)

    # Fetch and print the results
    for row in result.iterdict():
        print(row)

# Close the client
client.close()
