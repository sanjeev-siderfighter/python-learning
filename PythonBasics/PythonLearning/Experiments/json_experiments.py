import json


def verify_response(request, response, api_name, compulsory_parameter, *optional_parameters):
    print(optional_parameters)
    json_obj = json.loads(response)
    try:
        if len(optional_parameters) == 2:
            condition = json_obj[compulsory_parameter] and json_obj[optional_parameters[0]][optional_parameters[1]]
        else:
            condition = json_obj[compulsory_parameter]

        print(json_obj[optional_parameters[0]][optional_parameters[1]])
        print(json_obj[compulsory_parameter])
        # if condition:
        #     print(f"{api_name} is successful", '\n')
        #     return True
        # elif json_obj[compulsory_parameter] is False:
        #     print(f"{api_name} is failure, '{compulsory_parameter}' = false")
        #     print(f"{api_name} request:-\n", request)
        #     print(f"{api_name} repsonse:-\n", response)
        #     return False
    except:
        print(f"{api_name} request:-\n", request)
        print(f"{api_name} repsonse:-\n", response)
        print(f"Looking for '{compulsory_parameter}' in response but not found")
        return False

# some JSON:
x = '{"cart":{"cart_change_error":null,"items":[{"id":"62-64-477","name":"25% OFF + Extra 25% Credits","pricable_id":477,"quantity":1,"cost":148.0,"item_cost":148.0,"remark":"","customizations":[],"marked_price":48,"brand_id":1,"brand_name":"Box8 Desi Meals","type":"MenuItem","unavailable":"false","unavailability_type":"none"}],"outlet_service_charges":[{"name":"SGST@2.5%","amount":1.2,"code":"SGST101"},{"name":"CGST@2.5%","amount":1.2,"code":"CGST101"}],"total_payable":50,"no_of_items":1,"net_total":48,"discount_applied":false,"total_payable_without_discount":155,"gross_total":148,"allowed_cashback":0,"cart_session":"f5b70f6c-f7e0-4608-8131-5a61f35cbacd","cashback_amount":0,"discount":-100,"round_off":0.0,"discount_code":"Slashed Price Discount","payment_methods":[],"is_promo_camp_id":false,"is_ola_offer":false,"outlet_timings":null,"applicable_subscription_id":null,"upgrade_subscription_savings":[],"subscription_message":null,"cart_updated":null,"discount_details":[{"code":"Slashed Price Discount","amount":-100}],"tip_amount":0,"currency_applicable_with_coupon":true},"meta":{"code":200,"status":"OK","message":"Everything is fine","error":false,"version":"1.0","copyright":"Copyright 2015 Box8"}}'
mobikwik = '{"linked":false,"eligible":true,"data":{},"message":"User not linked.", "success":true}'
# parse x:
y = json.loads(mobikwik)

# the result is a Python dictionary:
# print(y["meta"]["code"], type(y["meta"]["code"]))
print(y["linked"], type(y["linked"]))
try:
    if y["success"]:
        print("yo")
except:
    print("Need to use try-except")

booler = verify_response("hello", x, "api name", "cart", "meta", "code")

# if (y["success"]) is None:
#     print("yes, working")
# assert y["data"]["url"], "yahoo"
