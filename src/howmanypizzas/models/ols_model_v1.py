#from statsmodels.regression.linear_model import OLSResults

def predict_pizza_v1():
    result = None
    try:
        registrations = int(input("Enter the number of registrations as of 2 days before the event: "))
        if registrations < 0:
            raise ValueError("Enter a non-negative number")

        #loaded_model = OLSResults.load("ols_model_v1.pickle")
        #result = loaded_model.predict([1, registrations]).round(2).astype("float")[0]

        ## Coefficients from the OLS model in howmanypizzas/data-exploration/exploration.ipynb
        result = int(29.7414 + 0.5560 * registrations)    
        result_lower_bound = int(17.825820 + 0.352351 * registrations)
        result_upper_bound = int(41.656931 + 0.759745 * registrations)

    except ValueError as e:
        print("Enter a valid value. {}".format(e))

    if result is not None:    
        print("\nYou can expect {result:0d} check ins, with a 95% confidence interval between {result_lower_bound:0d} and {result_upper_bound:0d} check ins.".format(result=result, result_lower_bound=result_lower_bound, result_upper_bound=result_upper_bound))
        print("\nIf each person eats 1/6th of a large pizza, then you should order {result:0d} pizzas, or between {result_lower_bound:0d} and {result_upper_bound:0d} pizzas".format(result=int(result/6), result_lower_bound=int(result_lower_bound/6), result_upper_bound=int(result_upper_bound/6)))

if __name__ == '__main__':
    predict_pizza_v1()