import math
from statsmodels.regression.linear_model import OLSResults

try:
    registrations = int(input("Enter the number of registrations as of 2 days before the event: "))

    loaded_model = OLSResults.load("ols_model_v1.pickle")

    result = loaded_model.predict([1, registrations]).round(0).astype("int")[0]

    print("You can expect {} check ins based on the number of registrations. If each person eats a quarter pizza, you should order {} pizzas.".format(result, math.ceil(result/4)))

except ValueError:
    print("Please enter a valid value.")