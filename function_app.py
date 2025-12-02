import azure.functions as func
import datetime
import json
import logging
import math

app = func.FunctionApp()

@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    number = req.params.get('number')
    if not number:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            number = req_body.get('number')

    if number:
        # Convert number to integer
        num = int(number)

        response = analyze_number(num)
        
        return func.HttpResponse(json.dumps(response))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a number in the query string or in the request body.",
             status_code=200
        )


# TODO: Implement the analyze_number function
# You will only make modifications to the function below
def analyze_number(num):
    # TODO 1: Code Logic to handle number validation
    if not isinstance(num, int):
        return {
            'error': 'please enter a valid number'
        }
    
    if num <= 0:
        return {
            'error': 'please enter a number greater than 0'
        }

    # TODO 2: Code Logic to find the sum of numbers
    sum_of_digits = sum(int(digit) for digit in str(num))

    # TODO 3: Code Logic to check whether number is prime

    if num <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

    # TODO 4: Code Logic to check whether number is odd

    is_odd = num % 2 != 0


    # TODO 5: Code Logic to check whether number is perfect
    
    if num == 1:
        is_perfect = False
    else:
        divisor_sum = 1
        limit = int(math.sqrt(num))

        for i in range(2, limit + 1):
            if num % i == 0:
                divisor_sum += i
                if i != num // i:
                    divisor_sum += num // i

        is_perfect = divisor_sum == num

    # TODO 6: Replace default values below with the results of the calculations from
    # TODOs 2-5.

    response = {
        "sum_of_digits": sum_of_digits,
        "is_prime": is_prime,
        "is_odd": is_odd,
        "is_perfect": is_perfect
    }

    return response

